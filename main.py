'''
Main file for flask to run.
Runs a local server on 127.0.0.1.

Only the necessary packages/functions are imported
'''

from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from lib.dashboard import fileDashboard
from lib.logParser import parseFile
from lib.query import cloudQuery
from time import perf_counter
from lib.query import plotter
from lib import redshift
from os.path import join
from threading import *
from json import dumps
import datetime
import pyodbc
import json
import os


app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'tmp'
global fname
fname="thisfile.html"

#Internal Use - The dynamically generated file is remove after the request is done. 
'''***IMPORTANT*** - Required for getting correct output and removing the generated file since its one-time use only'''
@app.after_request
def afterRequest(response):
    if os.path.exists(os.path.dirname(os.path.abspath(__file__))+"\\templates\\"+globals()['fname']) == True:
       os.remove(os.path.dirname(os.path.abspath(__file__))+"\\templates\\"+globals()['fname'])
       globals()['fname']="thisfile.html"
    return response

#Returns the home page
@app.route("/")
def returnHome():
    print(os.path.dirname(os.path.abspath(__file__))+"\\templates\\"+globals()['fname'])
    return render_template("home.html")

#FileQuery with upload
@app.route('/filequery') 
def returnFileQuery():
    return render_template('filequery.html')

#FileQuery with previously parsed file
@app.route('/filequerypage', methods=['GET']) 
def returnQueryPage():
    return render_template("filequerypage.html")

#FileDashboard
@app.route('/filedashboard', methods=['GET']) 
def returnFileDashboard():
    return render_template("filedashboard.html")

#FileDashboard with previously parsed file
@app.route('/filedashboardpage', methods=['GET']) 
def returnFileDashboardPage():
    globals()['fname']=fileDashboard()
    return render_template(globals()['fname'])

#CloudDashsboard
@app.route('/clouddashboard', methods=['GET']) 
def returnCloudDashboard():
    return render_template("clouddashboard.html")

#CloudQuery
@app.route('/cloudquerypage', methods=['GET']) 
def returnCloudQueryPage():
    return render_template("cloudquery.html")

#Purge
@app.route('/purge', methods=['GET']) 
def returnPurgeQueryPage():
    return render_template("purge.html")

''' Functions below this line is only for internal use by the application. 
These are accessed by the client side HTML files returned by the above functions on request'''

#Internal Use - Cloud querying
@app.route('/cloudquery', methods=['POST']) 
def CQuery():
    jsonObj = dict()

    for key, value in request.form.items():
        if value != '':
            jsonObj[key] = value
    del jsonObj['submit2']
    # filtering the necessary key value pairs
    jsonObj = dumps(jsonObj, indent=2)
    # plots the table and dashboard on a new page
    globals()['fname']=cloudQuery(jsonObj)
    return render_template(globals()['fname'])

#Internal Use - File dashboard
@app.route('/filedashoutput', methods=['POST']) 
def filedash():
    f=request.files['file']
    f.save(os.path.dirname(os.path.abspath(__file__)) + "\\" +app.config['UPLOAD_FOLDER'] + "\\" + secure_filename(f.filename))
    parseFile(request.files['file'].filename)
    globals()['fname']=fileDashboard()
    return render_template(globals()['fname'])

#Internal use - Cloud Dashboard
@app.route('/json', methods=['GET']) 
def returnJSON():
    #Time is used to provide results upto the time to maintain consistency among the results
    redshift.time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    start =  datetime.datetime.now()
    T = [Thread(redshift.yearCount()),
    Thread(redshift.monthCount()),
    Thread(redshift.dateCount()),
    Thread(redshift.hourCount()),
    Thread(redshift.requestTypeCount()),
    Thread(redshift.statusCodeCount()),
    Thread(redshift.APICount()),
    Thread(redshift.responseSizeStatistics()),
    Thread(redshift.responseTimeStatistics()),
    Thread(redshift.userLogins()),
    Thread(redshift.browserAnalysis()),
    Thread(redshift.osAnalysis()),
    Thread(redshift.deviceAnalysis())]

    for i in T:
        i.start()
        i.join()
 
    return json.dumps(redshift.obj)

#Internal use - File Query (File saving and Parsing)
@app.route('/query', methods=['POST']) 
def query():
    '''
    Converts the input file from .log to .csv.
    the log file is stored in tmp folder.
    You can clear the tmp folder regularly if the log files are taking too much space.
    the csv file is stored in output file
    '''
    # Checks the validity of input file-name
    try:
        f = request.files['file']
    except:
        return redirect('http://127.0.0.1:5000')
    if f.filename == '' or f.filename.split('.')[-1] != 'log':
        return redirect('http://127.0.0.1:5000')

    x = perf_counter()
    # Saves to tmp folder
    f.save(os.path.dirname(os.path.abspath(__file__)) + "\\" + app.config['UPLOAD_FOLDER'] + "\\" + secure_filename(f.filename))
    print(f'{perf_counter()-x}s for saving the file.')

    parseFile(f.filename)
    return render_template('filequerypage.html')


#Internal use - File Querying and results returning
@app.route('/output', methods=['POST']) 
def output():
    '''
    Plotting the graph using query from lib folder
    '''
    jsonObj = dict()
    

    for key, value in request.form.items():
        if value != '':
            jsonObj[key] = value
    del jsonObj['submit2']
    # filtering the necessary key value pairs
    jsonObj = dumps(jsonObj, indent=2) 
    globals()['fname'] = plotter(jsonObj)
    # plots the table and dashboard on a new page
    return render_template(globals()['fname'])

#Internal use - File Querying and results returning
@app.route('/purgewarehouse', methods=['POST']) 
def purge():
    for key, value in request.form.items():
        redshift.purgeData(value)
        break
    return "OK"



if __name__ == "__main__":
    app.run()



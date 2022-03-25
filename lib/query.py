'''
Library for querying for File and Cloud
'''

from plotly import graph_objects as go
from flask import render_template
from pandas import read_csv
from copy import deepcopy
from lib import redshift
from os.path import join
from json import loads
from lib import html
import pandas as pd
import datetime
import random
import os

def plotter(obj):
    print(os.getcwd())
    '''
    Shows a table with the query that the user sent on another page.
    '''
    name = "file"+str(random.random())+".html"

    if os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\filtered_output.csv") == True:
        os.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\filtered_output.csv")

    dataObj = read_csv(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\logfile.csv")

    jsondict = loads(obj)
    querystr = ""
    # Query on the dataframe
    for key, value in jsondict.items():
        if key in ['Day','Month','Year','HH']:
             querystr = querystr + " " + key + " == " + value + " and"
        if key in ['Bytes','ResponseTime']:
            querystr = querystr + " " + key + " " + value[:2] + " " + value[2:] + " and"
        else:
            querystr = querystr + " " + key + " == '" + value + "' and"
    querystr = querystr[:len(querystr)-4]

    dataObj.query(querystr,inplace=True)
    # Writing the filtered output to an output CSV file in outputFiles directory
    dataObj.drop(['RemoteLogName','UserID'],axis=1,inplace=True)
    dataObj.to_csv(join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\filtered_output.csv"),index=False)
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(dataObj.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[dataObj.IPAddress, dataObj.Day, dataObj.Month, dataObj.Year, dataObj.HH, dataObj.RequestType, dataObj.API, dataObj.StatusCode, dataObj.Bytes, dataObj.Refferer, dataObj.UserAgent, dataObj.ResponseTime,dataObj.Browser,dataObj.Os,dataObj.Device],
                   fill_color='lavender',
                   align='left'))
    ])

    redshift.obj['yearvscount']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(dataObj.Year.value_counts()).keys()]))
    redshift.obj['yearvscount']['data']['y'] = [k for k in dict(dataObj.Year.value_counts()).values()]
    redshift.obj['requesttypecount']['data']['x'] = [k for k in dict(dataObj.RequestType.value_counts()).keys()]
    redshift.obj['requesttypecount']['data']['y'] = [k for k in dict(dataObj.Year.value_counts()).values()]
    redshift.obj['statuscodes']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(dataObj.StatusCode.value_counts()).keys()]))
    redshift.obj['statuscodes']['data']['y'] = [k for k in dict(dataObj.StatusCode.value_counts()).values()]
    redshift.obj['datewiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(dataObj.Day.value_counts()).keys()]))
    redshift.obj['datewiselogin']['data']['y'] = [k for k in dict(dataObj.Day.value_counts()).values()]

    redshift.obj['hourwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(dataObj.HH.value_counts()).keys()]))
    redshift.obj['hourwiselogin']['data']['y'] = list([k for k in dict(dataObj.HH.value_counts()).values()])
    
    redshift.obj['monthwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(dataObj.Month.value_counts()).keys()]))
    redshift.obj['monthwiselogin']['data']['y'] = [k for k in dict(dataObj.Month.value_counts()).values()]
    redshift.obj['apicount']['data']['y'] = [k for k in dict(dataObj.API.value_counts()).keys()]
    redshift.obj['apicount']['data']['x'] = [k for k in dict(dataObj.API.value_counts()).values()]
    redshift.obj['responsesize'] = [dataObj.Bytes.min(),dataObj.Bytes.max(),dataObj.Bytes.mean()]
    redshift.obj['responsetime'] = [dataObj.ResponseTime.min(),dataObj.ResponseTime.max(),dataObj.ResponseTime.mean()]
    redshift.obj['ulogins'] = [len(dataObj)]

    redshift.obj['browseranalysis']['data']['x'] = [k for k in dict(dataObj.Browser.value_counts()).keys()]
    redshift.obj['browseranalysis']['data']['y'] = [k for k in dict(dataObj.Browser.value_counts()).values()]
    
    redshift.obj['deviceanalysis']['data']['x'] = [k for k in dict(dataObj.Device.value_counts()).keys()]
    redshift.obj['deviceanalysis']['data']['y'] = [k for k in dict(dataObj.Device.value_counts()).values()]

    redshift.obj['osanalysis']['data']['labels'] = [k for k in dict(dataObj.Os.value_counts()).keys()]
    redshift.obj['osanalysis']['data']['values'] = [k for k in dict(dataObj.Os.value_counts()).values()]
    
    outputhtml = html.HTML()
    outputhtml = outputhtml.format(div=fig.to_html(),objectpl=redshift.obj) 
    out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\templates\\"+name,"w")
    out.write(outputhtml)
    out.close()

    return name

def cloudQuery(obj):
   
    name = "file"+str(random.random())+".html"
    jsondict = loads(obj)
    string="SELECT IPAddress, Day, Month, Year, HH, RequestType, API, StatusCode, Bytes, Refferer, UserAgent, ResponseTime, Browser, Os, Device FROM WEBLOGS WHERE "

    # Query on the dataframe
    for key, value in jsondict.items():
        if key in ["Day","Month","Year","HH","StatusCode"]:
           string=string+key+"="+value+" AND "
        if key in ["Bytes","ResponseTime"]:
           string=string+key+value+" AND "
        else:
           string=string+key+"='"+value+"' AND "
    string = string + " timestamps <= '"+datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") +  "'"
    string = pd.read_sql(string,redshift.cnxn)
    

    redshift.obj['yearvscount']['data']['x'] = [k for k in dict(string.year.value_counts()).keys()]
    redshift.obj['yearvscount']['data']['y'] = [k for k in dict(string.year.value_counts()).values()]

    redshift.obj['hourwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(string.hh.value_counts()).keys()]))
    redshift.obj['hourwiselogin']['data']['y'] = [k for k in dict(string.hh.value_counts()).values()]

    redshift.obj['requesttypecount']['data']['x'] = [k for k in dict(string.requesttype.value_counts()).keys()]
    redshift.obj['requesttypecount']['data']['y'] = [k for k in dict(string.requesttype.value_counts()).values()]
    redshift.obj['statuscodes']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(string.statuscode.value_counts()).keys()]))
    redshift.obj['statuscodes']['data']['y'] = [k for k in dict(string.statuscode.value_counts()).values()]
    redshift.obj['datewiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(string.day.value_counts()).keys()]))
    redshift.obj['datewiselogin']['data']['y'] = [k for k in dict(string.day.value_counts()).values()]
    redshift.obj['monthwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(string.month.value_counts()).keys()]))
    redshift.obj['monthwiselogin']['data']['y'] = [k for k in dict(string.month.value_counts()).values()]
    redshift.obj['apicount']['data']['y'] = [k for k in dict(string.api.value_counts()).keys()]
    redshift.obj['apicount']['data']['x'] = [k for k in dict(string.api.value_counts()).values()]
    redshift.obj['responsesize'] = [string.bytes.min(),string.bytes.max(),string.bytes.mean()]
    redshift.obj['responsetime'] = [string.responsetime.min(),string.responsetime.max(),string.responsetime.mean()]
    redshift.obj['ulogins'] = [len(string)]

    redshift.obj['browseranalysis']['data']['x'] = [k for k in dict(string.browser.value_counts()).keys()]
    redshift.obj['browseranalysis']['data']['y'] = [k for k in dict(string.browser.value_counts()).values()]
    
    redshift.obj['deviceanalysis']['data']['x'] = [k for k in dict(string.device.value_counts()).keys()]
    redshift.obj['deviceanalysis']['data']['y'] = [k for k in dict(string.device.value_counts()).values()]

    redshift.obj['osanalysis']['data']['labels'] = [k for k in dict(string.os.value_counts()).keys()]
    redshift.obj['osanalysis']['data']['values'] = [k for k in dict(string.os.value_counts()).values()]

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(string.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[string.ipaddress, string.day, string.month, string.year, string.hh, string.requesttype, string.api, string.statuscode, string.bytes, string.refferer, string.useragent, string.responsetime,string.browser,string.os,string.device],
                   fill_color='lavender',
                   align='left'))
    ])
    fig.update_layout(height=500)

    outputhtml = html.HTML()
    outputhtml = outputhtml.format(div=fig.to_html(),objectpl=redshift.obj)
    out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\templates\\"+name,"w")
    out.write(outputhtml)
    out.close()
    
    return name


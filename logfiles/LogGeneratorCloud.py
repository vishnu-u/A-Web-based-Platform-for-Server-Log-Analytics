from datetime import date
import random
from random import randint, choice
import sys
import time
import faker
from datetime import datetime
import pyodbc 
#cnxn = pyodbc.connect('Driver={Amazon Redshift (x64)}; Server=redshift-cluster-1.cm0ud4kbfug7.us-east-2.redshift.amazonaws.com; Database=dev; UID=awsuser; PWD=Root0399; Port=5439',timeout=10)
cnxn = pyodbc.connect('Driver={Amazon Redshift (x64)}; Server=redshift-cluster-project.cm0ud4kbfug7.us-east-2.redshift.amazonaws.com; Database=dev; UID=awsuser; PWD=Root0399; Port=5439')
cursor = cnxn.cursor()	

fak = faker.Faker()


dictionary = {'request': ['GET', 'POST', 'PUT', 'DELETE'], 'endpoint': ['/usr', '/usr/admin', '/usr/admin/developer', '/usr/login', '/usr/register'], 'statuscode': [
    '303', '404', '500', '403', '502', '304','200'], 'username': ['james', 'adam', 'eve', 'alex', 'smith', 'isabella', 'david', 'angela', 'donald', 'hilary'],
    'ua' : ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
            'Mozilla/5.0 (Android 10; Mobile; rv:84.0) Gecko/84.0 Firefox/84.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4380.0 Safari/537.36 Edg/89.0.759.0',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.12.4.5121',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.329',
            'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_9 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1'],
            'referrer' : ['-',fak.uri()]}


#f.write('%s - - [%s %s] "%s %s HTTP/1.0" %s %s "%s" "%s" %s\n' % 
        #(fak.ipv4(),random_date("01/Jan/2018:12:00:00","01/Jan/2020:12:00:00", random.random()),datetime.now(local).strftime('%z'),
         #choice(dictionary['request']),choice(dictionary['endpoint']),choice(dictionary['statuscode']),str(int(random.gauss(5000,50))),choice(dictionary['referrer']),choice(dictionary['ua']),random.randint(1,5000)))

browser = ""
os = ""
ua = ""
device = ""
for w in range(50001):
    print(w)
    dat = datetime.utcnow()
    ua = choice(dictionary['ua'])


    if str.find(ua,"Mozilla") >= 0 and str.find(ua,"Firefox") >= 0:
       browser="Mozilla"
    elif str.find(ua,"OPR") >= 0:
       browser = "Opera"
    elif str.find(ua,"Mozilla") >= 0 and str.find(ua,"Chrome") >=0 and str.find(ua,"OPR") == -1 and str.find(ua,"Edg") == -1:
       browser = "Chrome"
    elif str.find(ua,"Mozilla") >= 0 and str.find(ua,"Safari") >= 0 and str.find(ua,"Chrome") == -1:
       browser = "Safari"
    elif str.find(ua,"Mozilla") >= 0 and str.find(ua,"MSIE") >= 0:
       browser = "IE"
    else:
       browser = "Others"

    
    if str.find(ua,"Windows") >= 0:
       os="Windows"
    if str.find(ua,"iPhone") >= 0:
       os="iOS"
    if str.find(ua,"Linux") >= 0:
       os="Linux"
    if str.find(ua,"Macintosh") >= 0:
       os="Mac OS" 
    
    if str.find(ua,"Mobile") >= 0:
       device="Mobile"
    else:
       device="Others"

    cursor.execute("INSERT INTO WEBLOGS VALUES('{}','{}','{}',{},{},{},{},'{}','{}',{},{},'{}','{}',{},'{}','{}','{}','{}');".format(fak.ipv4(),
    "-",
    "-",
    dat.day,
    dat.month,
    dat.year,
    dat.hour,
    choice(dictionary['request']),  
    choice(dictionary['endpoint']),
    choice(dictionary['statuscode']),
    int(random.gauss(5000,50)),
    choice(dictionary['referrer']),
    ua,
    random.randint(1,5000),
    dat.strftime("%Y-%m-%d %H:%M:%S"),
    browser,
    os,
    device
    ))
    cnxn.commit()
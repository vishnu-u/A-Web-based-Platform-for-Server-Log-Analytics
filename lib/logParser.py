'''
Library for parsing Log files converting it to csv and saving it
'''
import lib.redshift as redshift
from time import perf_counter
from datetime import datetime
from os.path import join
from lib import html
import pandas as pd
import csv
import re
import os

def parseBrowser(ua):
    browse=""
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
    return browser

def parseOS(ua):
  os=""
  if str.find(ua,"Windows") >= 0:
       os="Windows"
  if str.find(ua,"iPhone") >= 0:
       os="iOS"
  if str.find(ua,"Macintosh") >= 0:
       os="Mac OS"
  if str.find(ua,"Android") >= 0 or str.find(ua,"Linux") >= 0:
       os="Linux"
  return os

def parseDevice(ua):
  device=""
  if str.find(ua,"Mobile") >= 0:
       device="Mobile"
  else:
       device="Others"
  return device

def parseFile(input_log):
    rows = []
    
    f = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\tmp\\"+input_log, "r+") 
    
    if os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\filtered_output.csv") == False:
      out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\filtered_output.csv", "w")
      out.close()

    if os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\logfile.csv") == False:
      out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\logfile.csv", "w")
      out.close()


    out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\logfile.csv", "r+", newline='')
    out.truncate(0) 
    csvwriter = csv.writer(out)
    
    fields = ['IPAddress', 'RemoteLogName', 'UserID', 'Day','Month','Year','HH','RequestType','API','StatusCode','Bytes','Refferer','UserAgent','ResponseTime','Browser','Os','Device'] 
    csvwriter.writerow(fields)

    regex = "(?P<ip>.*) (?P<remote_log_name>.*) (?P<userid>.*) \[(?P<date>.*)(?= ) (?P<timezone>.*?)\] \"(?P<request_method>.*) (?P<path>.*)(?P<request_version> HTTP/.*)\" (?P<status>.*) (?P<length>.*) \"(?P<referrer>.*)\" \"(?P<user_agent>.*)\" (?P<generation_time_micro>.*)"
    
    j=1
    for i in f.readlines(): 
      res = re.findall(regex, i) 
      rows.append([str(res[0][0]),\
      "-",\
      "-",\
      datetime.strptime(res[0][3],"%d/%b/%Y:%H:%M:%S").day,\
      datetime.strptime(res[0][3],"%d/%b/%Y:%H:%M:%S").month,\
      datetime.strptime(res[0][3],"%d/%b/%Y:%H:%M:%S").year,\
      datetime.strptime(res[0][3],"%d/%b/%Y:%H:%M:%S").hour,\
      res[0][5],\
      res[0][6].split("?")[0],\
      int(res[0][8]),\
      int(res[0][9]),\
      res[0][10],\
      res[0][11],\
      int(res[0][12]),\
      parseBrowser(res[0][11]),\
      parseOS(res[0][11]),\
      parseDevice(res[0][11])])

      if len(rows) == 100000: 
        csvwriter.writerows(rows)
        rows = []

    csvwriter.writerows(rows)
    out.close()
    f.close()
    for items in os.listdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\tmp\\"):
       os.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\tmp\\" + items)



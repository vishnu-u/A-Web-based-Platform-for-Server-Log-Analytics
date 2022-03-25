'''
Library for generating file dashboard and saving the results in dictionary
'''
from lib import redshift
from lib import html
import pandas as pd
import random
import os

def fileDashboard():
    name = "file"+str(random.random())+".html"
    out = pd.read_csv(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\outputFiles\\logfile.csv")
    
    redshift.obj['yearvscount']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(out.Year.value_counts()).keys()]))
    redshift.obj['yearvscount']['data']['y'] = [k for k in dict(out.Year.value_counts()).values()]
    redshift.obj['hourwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(out.HH.value_counts()).keys()]))
    redshift.obj['hourwiselogin']['data']['y'] = [k for k in dict(out.HH.value_counts()).values()]
    redshift.obj['requesttypecount']['data']['x'] = [k for k in dict(out.RequestType.value_counts()).keys()]
    redshift.obj['requesttypecount']['data']['y'] = [k for k in dict(out.Year.value_counts()).values()]
    redshift.obj['statuscodes']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(out.StatusCode.value_counts()).keys()]))
    redshift.obj['statuscodes']['data']['y'] = [k for k in dict(out.StatusCode.value_counts()).values()]
    redshift.obj['datewiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(out.Day.value_counts()).keys()]))
    redshift.obj['datewiselogin']['data']['y'] = [k for k in dict(out.Day.value_counts()).values()]
    redshift.obj['monthwiselogin']['data']['x'] = list(map(redshift.modifyList,[k for k in dict(out.Month.value_counts()).keys()]))
    redshift.obj['monthwiselogin']['data']['y'] = [k for k in dict(out.Month.value_counts()).values()]
    redshift.obj['apicount']['data']['y'] = [k for k in dict(out.API.value_counts()).keys()]
    redshift.obj['apicount']['data']['x'] = [k for k in dict(out.API.value_counts()).values()]
    redshift.obj['responsesize'] = [out.Bytes.min(),out.Bytes.max(),out.Bytes.mean()]
    redshift.obj['responsetime'] = [out.ResponseTime.min(),out.ResponseTime.max(),out.ResponseTime.mean()]
    redshift.obj['ulogins'] = [len(out)]

    redshift.obj['browseranalysis']['data']['x'] = [k for k in dict(out.Browser.value_counts()).keys()]
    redshift.obj['browseranalysis']['data']['y'] = [k for k in dict(out.Browser.value_counts()).values()]
    
    redshift.obj['deviceanalysis']['data']['x'] = [k for k in dict(out.Device.value_counts()).keys()]
    redshift.obj['deviceanalysis']['data']['y'] = [k for k in dict(out.Device.value_counts()).values()]

    redshift.obj['osanalysis']['data']['labels'] = [k for k in dict(out.Os.value_counts()).keys()]
    redshift.obj['osanalysis']['data']['values'] = [k for k in dict(out.Os.value_counts()).values()]
    
    outhtml = html.dashHTML()
    outhtml = outhtml.format(objectpl=redshift.obj)
    out = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\templates\\"+name,"w")
    out.write(outhtml)
    out.close()
    return name



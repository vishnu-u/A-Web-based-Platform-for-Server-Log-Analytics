'''
Library for connecting to Cloud Data Warehouse and fetching results for queries
'''
import pyodbc
import pandas as pd
from datetime import datetime
cnxn = pyodbc.connect('Driver={Amazon Redshift (x64)}; Server=redshift-cluster-project.cm0ud4kbfug7.us-east-2.redshift.amazonaws.com; Database=dev; UID=awsuser; PWD=Root0399; Port=5439')
cursor = cnxn.cursor()

obj = dict({
	"yearvscount" : 
		{
          "data" : {
		"x" : [],
		"y" : [],
		"type" : "bar"
	     },
		"layout" : {"title" : "Year vs Count","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)},"xaxis" :{"tickformat" : ",d"}}
		},
	
	"requesttypecount" : 
	{
		"data" : {
			"x" : [],
			"y" : [],
			"type" : "bar"
		},
		"layout" : {"title" : "Request Type Count","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)}}
		},

      "statuscodes" : 
	{
		"data" : {
			"x" : [],
			"y" : [],
			"type" : "bar"
		},
		"layout" : {"title" : "Status Code Count","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)},"xaxis" :{"tickformat" : ",d"}}
		},
		
		"datewiselogin" : 
	{
		"data" : {
			"x" : [],
			"y" : [],
			"type" : "bar"
		},
		"layout" : {"title" : "Date wise Requests","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)},"xaxis" :{"tickformat" : ",d"}}
		},

		
		"hourwiselogin" : 
	{
		"data" : {
			"x" : [],
			"y" : [],
			"type" : "bar"
		},
		"layout" : {"title" : "Hour wise Requests","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)}}
		},

		"monthwiselogin" : 
	{
		"data" : {
			"x" : [],
			"y" : [],
		    "type" : "bar"
		},
		"layout" : {"title" : "Month wise Requests","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)}}
		},


		"apicount" : 
		{
				"data" : {
					"y" : [],
					"x" : [],
					"type" : "bar",
					"orientation" : 'h',
				},
				"layout" : {"title" : "API Count","margin": {"t": str(40), "b": str(40), "l": str(150), "r": str(40)}}
				},
		"responsetime" : [],
		"responsesize" : [],
		"ulogins" : [],
		
		"browseranalysis" : 
		{
				"data" : {
					"x" : [],
					"y" : [],
					"type" : "bar",
				},
				"layout" : {"title" : "Browser Analysis","margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)}}
				},

		"deviceanalysis" : 
		{
						"data" : {
							"x" : [],
							"y" : [],
							"type" : "bar",
						},
						"layout" : {"title" : "Device Analysis","margin" : {"t": str(40), "b": str(40), "l": str(40), "r": str(40)}}
						},
		"osanalysis" : 
		{
						"data" : {
							"labels" : [],
							"values" : [],
							"type" : "pie",
								},
						"layout" : {"title" : "OS Analysis", "margin": {"t": str(40), "b": str(40), "l": str(40), "r": str(40)},}
		},
})


time = 0

#Time Series Analysis
def yearCount():
   res = pd.read_sql("""SELECT DISTINCT(Year), COUNT(Year) from WEBLOGS WHERE timestamps <='{}' group by Year""".format(time),cnxn)
   obj['yearvscount']['data']['x'] = ["(" + str(x) +  ")" for x in res['year'].values]
   obj['yearvscount']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def monthCount():
   res = pd.read_sql("""SELECT DISTINCT(Month),COUNT(Month) from WEBLOGS WHERE timestamps <='{}' group by Month""".format(time),cnxn) 
   obj['monthwiselogin']['data']['x'] = list(map(modifyList,list(res['month'].values)))
   obj['monthwiselogin']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def dateCount():
   res =  pd.read_sql("""SELECT DISTINCT(Day),COUNT(Day) from WEBLOGS WHERE timestamps <='{}' group by Day""".format(time),cnxn) 
   obj['datewiselogin']['data']['x'] = list(map(modifyList,list(res['day'].values)))
   obj['datewiselogin']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def hourCount():
   res =  pd.read_sql("""SELECT DISTINCT(HH),COUNT(HH) from WEBLOGS WHERE timestamps <='{}' group by HH""".format(time),cnxn) 
   obj['hourwiselogin']['data']['x'] = list(map(modifyList,list(map(str,list(res['hh'].values)))))
   obj['hourwiselogin']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

#Request Analysis
def requestTypeCount():
   res =  pd.read_sql("""SELECT DISTINCT(RequestType),COUNT(RequestType) from WEBLOGS WHERE timestamps <='{}' group by RequestType""".format(time),cnxn) 
   obj['requesttypecount']['data']['x'] = list(res['requesttype'].values)
   obj['requesttypecount']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def modifyList(val):
   return "(" + str(val) + ")"
def statusCodeCount():
   res =  pd.read_sql("""SELECT DISTINCT(StatusCode),COUNT(StatusCode) from WEBLOGS WHERE timestamps <='{}' group by StatusCode""".format(time),cnxn) 
   obj['statuscodes']['data']['x'] = list(map(modifyList,res['statuscode'].values))
   obj['statuscodes']['data']['y'] = list(map(str,list(res['count'].values)))

def APICount():
   res = pd.read_sql("""SELECT DISTINCT(API),COUNT(API) from WEBLOGS WHERE timestamps <='{}' group by API""".format(time),cnxn)
   obj['apicount']['data']['y'] = list(res['api'].values)
   obj['apicount']['data']['x'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def responseSizeStatistics():
   res = pd.read_sql("""SELECT MIN(Bytes),MAX(Bytes),AVG(Bytes) from WEBLOGS WHERE timestamps <='{}'""".format(time),cnxn)
   obj['responsesize'] = [str(list(res['min'].values)[0]),str(list(res['max'].values)[0]),str(list(res['avg'].values)[0])]
   #cnxn.commit()

def responseTimeStatistics():
    res = pd.read_sql("""SELECT MIN(ResponseTime),MAX(ResponseTime),AVG(ResponseTime) from WEBLOGS WHERE timestamps <='{}'""".format(time),cnxn)
    obj['responsetime'] = [str(list(res['min'].values)[0]),str(list(res['max'].values)[0]),str(list(res['avg'].values)[0])]
    #cnxn.commit()

def userLogins():
   res = pd.read_sql("""SELECT COUNT(*) from WEBLOGS WHERE timestamps <='{}'""".format(time),cnxn)
   obj['ulogins'] = str(list(res['count'].values)[0])
   #cnxn.commit()

#Browser and Device Analysis
def browserAnalysis():
   res = pd.read_sql("""SELECT DISTINCT(Browser),COUNT(Browser) from weblogs where timestamps <= '{}' group by browser """.format(time),cnxn)
   obj['browseranalysis']['data']['x'] = list(res['browser'].values)
   obj['browseranalysis']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def deviceAnalysis():
   res = pd.read_sql("""SELECT DISTINCT(Device),COUNT(Device) from weblogs  WHERE timestamps <='{}' group by device""".format(time),cnxn)
   obj['deviceanalysis']['data']['x'] = list(res['device'].values)
   obj['deviceanalysis']['data']['y'] = list(map(str,list(res['count'].values)))
   #cnxn.commit()

def osAnalysis():
   res = pd.read_sql("""SELECT DISTINCT(Os),COUNT(Os) from weblogs where timestamps <= '{}' group by Os""".format(time),cnxn)
   obj['osanalysis']['data']['labels'] = list(res['os'].values)
   obj['osanalysis']['data']['values'] = list(map(str,list(res['count'].values)))
   cnxn.commit()

def purgeData(t):
	cursor.execute("""DELETE from weblogs where timestamps <= '{}'""".format(t))
	cnxn.commit()


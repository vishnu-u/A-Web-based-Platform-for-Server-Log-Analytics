obj ={'yearvscount': {'data': {'x': ['2018', '2019', '2020'], 'y': [2496829, 2499791, 3380], 'type': 'bar'}, 'layout': {'title': 'Year vs Count', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}, 'requesttypecount': {'data': {'x': ['PUT', 'GET', 'POST', 'DELETE'], 'y': [1249754, 1252383, 1248658, 1249205], 'type': 'bar'}, 'layout': {'title': 'Request Type Count', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}, 'datewiselogin': {'data': {'x': [29, 8, 17, 10, 24, 20, 7, 14, 28, 12, 27, 1, 16, 18, 2, 25, 13, 23, 31, 4, 26, 11, 21, 3, 5, 6, 15, 19, 22, 30, 9], 'y': [150554, 164711, 164692, 163454, 164082, 164285, 164284, 164682, 164839, 164990, 163239, 164513, 165021, 164227, 163548, 163651, 164934, 164713, 95857, 163930, 164634, 164504, 164756, 164849, 164686, 164563, 163748, 164760, 164419, 150285, 164590], 'type': 'bar'}, 'layout': {'title': 'Date wise Requests', 'margin': {'t': 40, 'b': 40, 'l': 40, 
'r': 40}}}, 'monthwiselogin': {'data': {'x': [12, 3, 7, 11, 5, 1, 6, 9, 2, 4, 8, 10], 'y': [424390, 426243, 423919, 410953, 424788, 423585, 411791, 410309, 384174, 411370, 423499, 424979], 'type': 'bar'}, 'layout': {'title': 'Month wise Requests', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}, 'apicount': {'data': {'y': ['/usr/admin', '/usr', '/usr/admin/developer', '/usr/register', '/usr/login'], 'x': [1000916, 999246, 999159, 1000484, 1000195], 'type': 'bar', 'orientation': 'h'}, 'layout': {'title': 'API Count', 'margin': {'t': 40, 'b': 40, 'l': 150, 'r': 40}}}, 'responsetime': [1, 5000, 2501], 'responsesize': [4754, 5241, 4999], 'ulogins': 5000000, 'browseranalysis': {'data': {'x': ['Others', 'Safari', 'Chrome', 
'Opera', 'Mozilla'], 'y': [1000222, 1001265, 999582, 999495, 999436], 'type': 'bar'}, 'layout': {'title': 'Browser Analysis', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}, 'deviceanalysis': {'data': {'x': ['Others', 'Mobile'], 'y': [2500012, 2499988], 'type': 'bar'}, 'layout': {'title': 'Device Analysis', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}, 'osanalysis': {'data': {'labels': ['Windows', 'Linux', 'Mac OS', 'iOS', 'Others'], 'values': [2000137, 1498267, 499875, 501390, 500331], 'type': 'pie'}, 'layout': {'title': 'OS Analysis', 'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40}}}};
function yearVsLogin()
{
Plotly.newPlot('graph1', [obj.yearvscount.data], obj.yearvscount.layout);
}



function requestTypeCount()
{
Plotly.newPlot('g4-1', [obj.requesttypecount.data], obj.requesttypecount.layout);
}



function apiCount()
{
Plotly.newPlot('g4-2',[obj.apicount.data], obj.apicount.layout);
}



function browserAnalysis()
{
Plotly.newPlot('graph6',[obj.browseranalysis.data], obj.browseranalysis.layout);
}



function deviceAnalysis()
{
Plotly.newPlot('graph7',[obj.deviceanalysis.data],obj.deviceanalysis.layout);
}



function monthWiseLogin()
{
Plotly.newPlot('graph2', [obj.monthwiselogin.data], obj.monthwiselogin.layout);
}


function dateWiseLogin()
{
Plotly.newPlot('graph3',[obj.datewiselogin.data],obj.datewiselogin.layout);
}


function osAnalysis()
{
Plotly.newPlot('graph8', [obj.osanalysis.data], obj.osanalysis.layout);
}

function setStatistics()
{
	document.getElementById("g5-1").getElementsByTagName("p")[0].innerText="Min Response Time : " + obj.responsetime[0] + " ns";
	document.getElementById("g5-1").getElementsByTagName("p")[1].innerText="Max Response Time : " + obj.responsetime[1] + " ns";
	document.getElementById("g5-1").getElementsByTagName("p")[2].innerText="Avg Response Time : " + obj.responsetime[2] + " ns";

	document.getElementById("g5-2").getElementsByTagName("p")[0].innerText="Min Response Time : " + obj.responsetime[0] + " bytes";
	document.getElementById("g5-2").getElementsByTagName("p")[1].innerText="Max Response Time : " + obj.responsetime[1] + " bytes";
	document.getElementById("g5-2").getElementsByTagName("p")[2].innerText="Avg Response Time : " + obj.responsetime[2] + " bytes";

	document.getElementById("g5-3").getElementsByTagName("p")[0].innerText="Total User Logins : " + obj.ulogins;
}

yearVsLogin()
dateWiseLogin()
monthWiseLogin()
requestTypeCount()
apiCount()
setStatistics()
browserAnalysis()
deviceAnalysis()
osAnalysis()
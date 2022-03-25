function yearVsLogin()
{
Plotly.newPlot('graph1',[obj.yearvscount.data],obj.yearvscount.layout);
}

function requestTypeCount()
{
Plotly.newPlot('g4-1',[obj.requesttypecount.data],obj.requesttypecount.layout);
}

function statusCodes()
{
Plotly.newPlot('g4-1-1', [obj.statuscodes.data], obj.statuscodes.layout);
}


function apiCount()
{
Plotly.newPlot('g4-2',[obj.apicount.data],obj.apicount.layout);
}

function browserAnalysis()
{
Plotly.newPlot('graph6',[obj.browseranalysis.data],obj.browseranalysis.layout);
}

function deviceAnalysis()
{
Plotly.newPlot('graph7',[obj.deviceanalysis.data],obj.deviceanalysis.layout);
}

function monthWiseLogin()
{
Plotly.newPlot('graph2',[obj.monthwiselogin.data],obj.monthwiselogin.layout);
}

function dateWiseLogin()
{
Plotly.newPlot('graph3-1',[obj.datewiselogin.data],obj.datewiselogin.layout);
}

function hourWiseLogin()
{
Plotly.newPlot('graph3-2',[obj.hourwiselogin.data],obj.hourwiselogin.layout);
}

function osAnalysis()
{
Plotly.newPlot('graph8',[obj.osanalysis.data],obj.osanalysis.layout);
}

function setStatistics()
{
	document.getElementById('g5-1').getElementsByTagName('p')[0].innerText="Min Response Time : "+obj.responsetime[0]+" ns";
	document.getElementById('g5-1').getElementsByTagName('p')[1].innerText="Max Response Time : "+obj.responsetime[1]+" ns";
	document.getElementById('g5-1').getElementsByTagName('p')[2].innerText="Avg Response Time : "+parseInt(obj.responsetime[2])+" ns";

	document.getElementById('g5-2').getElementsByTagName('p')[0].innerText="Min Response Size : "+obj.responsesize[0]+" bytes";
	document.getElementById('g5-2').getElementsByTagName('p')[1].innerText="Max Response Size : "+obj.responsesize[1]+" bytes";
	document.getElementById('g5-2').getElementsByTagName('p')[2].innerText="Avg Response Size : "+parseInt(obj.responsesize[2])+" bytes";

	document.getElementById('g5-3').getElementsByTagName('p')[0].innerText='Total User Logins : '+obj.ulogins;
}

function loadJSON()
{
    //obj=JSON.parse(this.response);
    yearVsLogin();
    dateWiseLogin();
    hourWiseLogin();
    monthWiseLogin();
    requestTypeCount();
    statusCodes();
    apiCount();
    setStatistics();
    browserAnalysis();
    deviceAnalysis();
    osAnalysis();
}
    
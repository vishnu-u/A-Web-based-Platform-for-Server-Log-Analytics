'''
Library for returning HTML content for query and dashboard output
The data is inserted with Python and written to generated file for rendering
'''
def HTML():
    return str("<!DOCTYPE html>\
<html>\
<head>\
<title>\
Web Log Analytics Platform\
</title>\
<script type='text/javascript'>obj={objectpl};</script>\
<link rel='stylesheet' href='/static/outstyle.css' />\
<script src='https://cdn.plot.ly/plotly-latest.min.js'></script>\
<script type='text/javascript' src='/static/outjs.js'></script>\
</head>\
<body onload='loadJSON()'>\
{div}\
<!--TimeSeriesAnalysis-->\
<div class='flex-div'>\
<div class='g1'id='graph1'></div>\
<div class='g2'id='graph2'></div>\
</div>\
 <div class='flex-last'>\
<div class='g3-1' id='graph3-1'></div>\
<div class='g3-2' id='graph3-2'></div>\
</div>\
\
<!--RequestAnalysis-->\
  <div class='flex-div-2'>\
<div class='inside-flex'>\
<div class='g4-1' id='g4-1'></div>\
<div class='g4-1-1' id='g4-1-1'></div>\
</div>\
<div class='g4-2' id='g4-2'></div>\
<div class='flex-div-2-1'>\
<div class='g5-1' id='g5-1'>\
<h2>Response Time Statistics</h2>\
<p></p>\
<p></p>\
<p></p>\
</div>\
<div class='g5-2' id='g5-2'>\
<h2>Response Size Statistics</h2>\
<p></p>\
<p></p>\
<p></p>\
</div>\
<div class='g5-3' id='g5-3'>\
<h2>Total Logins</h2>\
<p></p>\
</div>\
</div>\
</div>\
\
<!--BrowserandDeviceAnalysis-->\
<div class='flex-div-3'>\
<div class='g6' id='graph6'></div>\
\
<div class='flex-div-3-2'>\
<div class='g7' id='graph7'></div>\
<div class='g8' id='graph8'></div>\
</div>\
</div>\
</body>\
\
</script>\
</html>")

def dashHTML():
    return str("<!DOCTYPEhtml>\
<html>\
<head>\
<title>\
WebLogAnalyticsPlatform\
</title>\
<script type='text/javascript'>obj={objectpl};</script>\
<link rel='stylesheet' href='/static/outstyle.css' />\
<script src='https://cdn.plot.ly/plotly-latest.min.js'></script>\
<script type='text/javascript' src='/static/outjs.js'></script>\
</head>\
<body onload='loadJSON()'>\
<!--TimeSeriesAnalysis-->\
<div class='flex-div'>\
<div class='g1'id='graph1'></div>\
<div class='g2'id='graph2'></div>\
</div>\
<div class='flex-last'>\
<div class='g3-1' id='graph3-1'></div>\
<div class='g3-2' id='graph3-2'></div>\
</div>\
\
<!--RequestAnalysis-->\
  <div class='flex-div-2'>\
<div class='inside-flex'>\
<div class='g4-1' id='g4-1'></div>\
<div class='g4-1-1' id='g4-1-1'></div>\
</div>\
<div class='g4-2' id='g4-2'></div>\
<div class='flex-div-2-1'>\
<div class='g5-1' id='g5-1'>\
<h2>Response Time Statistics</h2>\
<p></p>\
<p></p>\
<p></p>\
</div>\
<div class='g5-2' id='g5-2'>\
<h2>Response Size Statistics</h2>\
<p></p>\
<p></p>\
<p></p>\
</div>\
<div class='g5-3' id='g5-3'>\
<h2>Total Logins</h2>\
<p></p>\
</div>\
</div>\
</div>\
\
<!--BrowserandDeviceAnalysis-->\
<div class='flex-div-3'>\
<div class='g6' id='graph6'></div>\
\
<div class='flex-div-3-2'>\
<div class='g7' id='graph7'></div>\
<div class='g8' id='graph8'></div>\
</div>\
</div>\
</body>\
\
</script>\
</html>")

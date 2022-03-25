function validation(){
    var result=true;
    var checkIP = /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/;  
    var checkStatusCode= /^\d{1,3}$/;         
    var i=document.getElementsByTagName("input");
    if(!(i[0].value.match(checkIP)) && i[0].value.length>0)
        alert("Invalid IP");
    if(!(i[2].value.match(checkStatusCode)) && i[2].value.length>0)
        alert("Invalid Status Code");
}
var myname = document.getElementById("firstname").value;
if((myname != '' && myname != null )  || !document.getElementById("submit").checked
)
{
document.getElementById("submit").disable =true
}

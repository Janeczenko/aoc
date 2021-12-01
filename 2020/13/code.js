var input=`1000434
17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,983,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,397,x,x,x,x,x,37,x,x,x,x,x,x,13`;
input=input.replace("\n",",");
data=input.split(",");
data1=data.filter(function(val){return /\d+/.test(val);});
data2=data.slice(1);



//ZADANIE 1
var waitTimes=[];
for(let i=1;i<data1.length;i++)
{
	waitTimes.push(data1[i]-data1[0]%data1[i]);
}
var firstBusIndex=waitTimes.indexOf(Math.min.apply(Math,waitTimes));
document.write(waitTimes[firstBusIndex]*data1[firstBusIndex+1]+"<br>");



//ZADANIE 2
var buses=[];
for(let i=0;i<data2.length;i++)
{
	if(/\d+/.test(data2[i]))buses.push(parseInt(data2[i]));
}
var lbi=buses.indexOf(Math.max.apply(Math,buses));
for(var i=data2[lbi]-lbi;true;i+=data2[lbi])
{
	var isGood=true;
	for(let j=0;j<buses.length;j++)
	{
		if(i%buses[j]!=data2.indexOf(buses[j]))isGood=false;
	}
	if(isGood)break;
}
document.write(i);
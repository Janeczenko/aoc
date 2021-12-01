var tekst=prompt("Podaj tekst, a ja policzę, ile w nim występuje donych znaków.");
var wynik=[];

function findLetter(n)
{
	for(let j=0;j<wynik.length;j++)
	{
		if(wynik[j][0]==tekst[n])return j;
	}
	return -1;
}
function sortArray(a,b)
{
	return(a[1]>b[1])?1:-1;
}


for(let i=0;i<tekst.length;i++)
{
	if(findLetter(i)==-1)
	{
		wynik.push([tekst[i],1]);
	}
	else
	{
		wynik[findLetter(i)][1]++;
	}
}

wynik.sort(sortArray);
for(let i=0;i<wynik.length;i++)
{
	document.write("Znak \""+wynik[i][0]+"\" wystąpił "+wynik[i][1]+" razy.<br>");
}
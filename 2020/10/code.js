var input=`153
17
45
57
16
147
39
121
75
70
85
134
128
115
51
139
44
65
119
168
122
72
105
31
103
89
154
114
55
25
48
38
132
157
84
71
113
143
83
64
109
129
120
100
151
79
125
22
161
167
19
26
118
142
4
158
11
35
56
18
40
7
150
99
54
152
60
27
164
78
47
82
63
46
91
32
135
3
108
10
159
127
69
110
126
133
28
15
104
138
160
98
90
144
1
2
92
41
86
66
95
12`;
var data=input.split("\n");

data.push(0);
data.sort((a,b)=>a-b);
for(let i=0;i<data.length;i++)data[i]=parseInt(data[i]);
data.push(data[data.length-1]+3);

//ZADANIE 1

var diff1=0;
var diff3=0;
for(let i=1;i<data.length;i++)
{
	if(data[i]-data[i-1]==1)diff1++;
	if(data[i]-data[i-1]==3)diff3++;
}
document.write(diff1*diff3+"<br>");


//ZADANIE 2
var combs=1;
function diff1Span(n)
{
	if(data[n+1]-data[n]==1)return(diff1Span(n+1)+1);
	else return 1;
}
function combinations(n)
{
	if(n==0)return 0;
	if(n==1||n==2)return 1;
	else return(combinations(n-1)+combinations(n-2)+combinations(n-3));
}
let i=0;
while(i<data.length)
{
	combs*=combinations(diff1Span(i));
	i+=diff1Span(i);
}
document.write(combs);
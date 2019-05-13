
[General]
Version=1

[Preferences]
Username=
Password=2778
Database=
DateFormat=
CommitCount=0
CommitDelay=0
InitScript=

[Table]
Owner=CHABANY
Name=COSTUMERSERVICE
Count=100000

[Record]
Name=PRIORITY
Type=NUMBER
Size=2
Data=Random(1,4)
Master=

[Record]
Name=STATUS
Type=VARCHAR2
Size=10
Data=List('Done', 'Irrlevant', 'OnProgress','waiting','new')
Master=

[Record]
Name=COSTUMERID
Type=NUMBER
Size=
Data=Random(100000000,100020000)
Master=

[Record]
Name=TYPE
Type=VARCHAR2
Size=10
Data=List('COMPLAIN','FEED_BACK','ADORE','IMPROVE', '')
Master=

[Record]
Name=REQUESTID
Type=NUMBER
Size=
Data=
Master=

[Record]
Name=DETAILES
Type=VARCHAR2
Size=300
Data=
Master=


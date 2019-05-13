
[General]
Version=1

[Preferences]
Username=
Password=2663
Database=
DateFormat=
CommitCount=0
CommitDelay=0
InitScript=

[Table]
Owner=CHABANY
Name=ORDERDRIVING
Count=200000

[Record]
Name=DATEORDER
Type=DATE
Size=10
Data=Random(01/01/19, 30/12/25)
Master=

[Record]
Name=ORDERID
Type=NUMBER
Size=9
Data=Sequence(1, [Inc], [WithinParent])
Master=

[Record]
Name=COSTUMERID
Type=NUMBER
Size=9
Data=Random(10000000, 10020000)
Master=

[Record]
Name=STATIONIDON
Type=NUMBER
Size=3
Data=Random(1,200)
Master=

[Record]
Name=STATIONIDOFF
Type=NUMBER
Size=3
Data=Random(1,200)
Master=


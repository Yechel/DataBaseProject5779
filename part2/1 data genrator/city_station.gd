
[General]
Version=1

[Preferences]
Username=
Password=2140
Database=
DateFormat=
CommitCount=0
CommitDelay=0
InitScript=

[Table]
Owner=CHABANY
Name=CITY_STATIONS
Count=180

[Record]
Name=STATIONID
Type=NUMBER
Size=10
Data=Sequence(21, [Inc], [WithinParent])
Master=

[Record]
Name=STATIONNAME
Type=VARCHAR2
Size=20
Data=Address1
Master=

[Record]
Name=CITYID
Type=NUMBER
Size=9
Data=Random(1, 37)
Master=


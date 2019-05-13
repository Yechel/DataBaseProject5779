
[General]
Version=1

[Preferences]
Username=
Password=2378
Database=
DateFormat=
CommitCount=0
CommitDelay=0
InitScript=

[Table]
Owner=CHABANY
Name=COSTUMERS
Count=20000

[Record]
Name=COSTUMERID
Type=NUMBER
Size=
Data=Sequence(10000000)
Master=

[Record]
Name=TYPE
Type=VARCHAR2
Size=10
Data=List('Regular','Vip','under18','70Club','Frequent','BlackList')
Master=

[Record]
Name=FRISTNAME
Type=VARCHAR2
Size=20
Data=FirstName
Master=

[Record]
Name=LASTNAME
Type=VARCHAR2
Size=20
Data=LastName
Master=


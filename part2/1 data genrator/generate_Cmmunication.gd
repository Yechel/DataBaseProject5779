
[General]
Version=1

[Preferences]
Username=
Password=2255
Database=
DateFormat=
CommitCount=0
CommitDelay=0
InitScript=

[Table]
Owner=CHABANY
Name=COMMUNICATIONS
Count=200000

[Record]
Name=ADRESS
Type=VARCHAR2
Size=20
Data=Address1
Master=

[Record]
Name=PHONENUMBER
Type=VARCHAR2
Size=11
Data= 0 + Random(2, 8) + [0] +  [0]+[0]+[0]+[0]+[0]+[0]+[0]
Master=

[Record]
Name=EMAIL
Type=VARCHAR2
Size=20
Data=Email
Master=

[Record]
Name=COSTUMERID
Type=NUMBER
Size=7
Data=Sequence(10000000, [Inc], [WithinParent])
Master=


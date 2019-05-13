import random;
from datetime import datetime;
from datetime import timedelta;

def a():
    fi = open('info_before.txt', 'r') 
    fh = open('info_after.txt', 'a+') 
    i = 1;
    print("start")
    while (i < 15002):
        
        line = fi.readline()
        if (line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('") != -1):
            t1 = line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('")
            print(line)
            k1 =line[t1-22:t1-3]
            k2 = line[t1+35:t1+54]
             
            print (k1)
            m = datetime.strptime(k1,"%d-%m-%Y %H:%M:%S") + timedelta(minutes=10)
            n = datetime.strftime(m,'%d-%m-%Y %H:%M:%S')
            print (n)
            ab = line.split(k2)
            fh.write(ab[0] + n+ab[1])
            '''ctype = random.choice(costumerType)
            fh.write(f"INSERT INTO Costumers (Costumers.Costumerid, Costumers.Type,Costumers.Fristname,Costumers.Lastname) VALUES ({ i},'{ctype}','{fnid}','{ lnid}');\n")
            print(f"INSERT INTO Costumers (Costumers.Costumerid, Costumers.Type,Costumers.Fristname,Costumers.Lastname) VALUES ({ i},{ ctype},{fnid },{ lnid});")
            '''
        else:
            fh.write(line)
        i+=1
    fh.write('commit;')
    fh.close
    fi.close
    print('Done')


def b():
    fi = open('info_before.txt', 'r') 
    fh = open('info_after.txt', 'a+') 
    i = 1;
    print("start")
    while (i < 10):
        
        line = fi.readline()
        if (line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('") != -1):
            t1 = line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('")
            print(line)
            k1 =line[t1-22:t1-3]
            k2 = line[t1+35:t1+54]
             
            print (k1)
            d = random.randint(0, 6) -1
            h = random.randint(0, 24) -1
            mnts = random.randint(0, 60) -1
            m = datetime.strptime(k1,"%d-%m-%Y %H:%M:%S") + timedelta(minutes=mnts) +  timedelta(hours=h) + timedelta(days=d)
            n = datetime.strftime(m,'%d-%m-%Y %H:%M:%S')
            print (n)
            ab = line.split(k2)
            fh.write(ab[0] + n+ab[1])
            '''ctype = random.choice(costumerType)
            fh.write(f"INSERT INTO Costumers (Costumers.Costumerid, Costumers.Type,Costumers.Fristname,Costumers.Lastname) VALUES ({ i},'{ctype}','{fnid}','{ lnid}');\n")
            print(f"INSERT INTO Costumers (Costumers.Costumerid, Costumers.Type,Costumers.Fristname,Costumers.Lastname) VALUES ({ i},{ ctype},{fnid },{ lnid});")
            '''
        else:
            fh.write(line)
        i+=1
    fh.write('commit;')
    fh.close
    fi.close
    print('Done')


def c():
    fi = open('info_before.txt', 'r') 
    fh = open('info_after1.txt', 'a+') 
    i = 1;
    print("start")
    while (i < 10):
        
        line = fi.readline()
        if (line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('") != -1):
            t1 = line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('")
            k1 =line[t1-22:t1-3]
            k2 = line[t1+35:t1+54]
            d = random.randint(0, 6) -1
            h = random.randint(0, 24) -1
            mnts = random.randint(0, 60) -1
            m = datetime.strptime(k1,"%d-%m-%Y %H:%M:%S") + timedelta(minutes=mnts) +  timedelta(hours=h) + timedelta(days=d)
            n = datetime.strftime(m,'%d-%m-%Y %H:%M:%S')
            ab = line.split(k2)
            abc =ab[0] + n+ab[1]
            s = abc.split(',')
            output = s[0]+'|'+s[1]+'|'+s[2]+'|'+s[3]+'|'+s[4]+','+s[5]+'|'+s[6]+','+s[7]+'|'+s[8]+'|'+s[9]
            print(output[8:-3])
            fh.write(output[8:-3] + '\n')
        i+=1
    fh.write('commit;')
    fh.close
    fi.close
    print('Done')


def d():
    fi = open('info_before.txt', 'r') 
    fh = open('info_after1.txt', 'a+') 
    i = 1;
    print("start")
    while (i < 10):
        
        line = fi.readline()
        if (line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('") != -1):
            t1 = line.find("'dd-mm-yyyy hh24:mi:ss'), to_date('")
            k1 =line[t1-22:t1-3]
            k2 = line[t1+35:t1+54]
            d = random.randint(0, 6) -1
            h = random.randint(0, 24) -1
            mnts = random.randint(0, 60) -1
            m = datetime.strptime(k1,"%d-%m-%Y %H:%M:%S") + timedelta(minutes=mnts) +  timedelta(hours=h) + timedelta(days=d)
            n = datetime.strftime(m,'%d-%m-%Y %H:%M:%S')
            ab = line.split(k2)
            abc =ab[0] + n+ab[1]
            s = abc.split(',')
            output = s[0]+'|'+s[1][2:-1]+'|'+s[2][2:-1]+'|'+s[3]+'|'+s[4][10:-1]+'|'+s[6][10:-1]+'|'+s[8]+'|'+s[9][2:-1]+'|' + s[10]
            print(output[8:-3])
            fh.write(output[8:-3] + '\n')
        i+=1
    fh.write('commit;')
    fh.close
    fi.close
    print('Done')    

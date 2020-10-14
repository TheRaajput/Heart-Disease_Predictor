import sqlite3

con = sqlite3.connect("dataset.db")
print('Database Opened')

con.execute("create table Heartdisease(SrNo INTEGER PRIMARY KEY AUTOINCREMENT,age INTEGER,gender INTEGER,chestPain INTEGER,bloodPressure INTEGER,cholestrol INTEGER,bsugar INTEGER,ecg INTEGER,heartRate INTEGER,cPain INTEGER,STdepression INTEGER,slopeST INTEGER,majorVessel INTEGER,ThalScore INTEGER, result INTEGER)")
            
print("Table created")
# cur = con.cursor()

# cur.execute("SELECT * from Heartdisease")

# result = cur.fetchall()
# print(result)

con.close()
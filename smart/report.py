import pandas as pd
import mysql.connector 

db = mysql.connector.connect(user ="root",database="recognition")
cursor = db.cursor()

query = "select name, date, time, status from report"
cursor.execute(query)
myallData = cursor.fetchall()

all_name = []
all_date =[]
all_time =[]
all_status =[]

for name, date, time, status in myallData:
    all_name.append(name)
    all_date.append(date)
    all_time.append(time)
    all_status.append(status)
    
dic = {'name': all_name, 'date': all_date, 'time': all_time, 'status': all_status}
df = pd.DataFrame(dic)
df_csv = df.to_csv('D:/SeniorProject/smart/Attendance_Details/attendance.csv')


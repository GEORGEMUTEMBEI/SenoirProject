import csv
import cv2
class Mark_Attendance:
    def __init__(self,csv_filename):
        self.csv_filename = csv_filename

    
    def write_csv_header(self,id,date,student_name,time,status):
        self.id = id
        self.date = date
        self.student_name = student_name
        self.time = time
        self.status = status
        f = open(self.csv_filename, "w+",newline='')
        writer = csv.DictWriter(f, fieldnames=[self.id,self.date,self.student_name,self.time,self.status])
        writer.writeheader()
        f.close()

    def append_csv_rows(self,records):
        self.records = records
        with open(self.csv_filename, 'a+',newline='') as f_object: 
            # Pass this file object to csv.writer() and get a writer object 

            writer_object = csv.writer(f_object) 
        
            # Pass the list as an argument into the writerow() 
            writer_object.writerow(self.records) 
        
            #Close the file object 
            f_object.close() 
'''import pandas as pd
import mysql.connector 
class Mark_Attendance:
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
        df_csv = df.to_csv('D:/smart-attendance-system/smart/Attendance_Details/attendance.csv')


    
    

'''
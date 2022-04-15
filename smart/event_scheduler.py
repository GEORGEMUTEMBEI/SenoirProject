from apscheduler.schedulers.background import BackgroundScheduler
import pymysql
from datetime import datetime
import smtplib
from mark_attendance import Mark_Attendance
from email.message import EmailMessage

def getall_students():
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
    cur = conn.cursor()
    cur.execute("select sid,email_address from attendance")
    data = cur.fetchall()
    all_students = {}
    if len(data) != 0:
        for(id,email) in data:
            all_students[id] = email
    conn.close()
    return all_students

def registered_vs_absent_students(all_students):
    dt = datetime.now()
    dt = dt.strftime("%Y-%m-%d %I:%M:%S")
    date = str(dt).split(' ')[0]
    time = str(dt).split(' ')[1]
    time_hour = time.split(':')[0]
    time_minute = time.split(':')[1]
    start_hour = 1
    end_hour = 11
    # start_minute = 0
    # end_minute = 0
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
    cur = conn.cursor()
    cur.execute("select id,time from report where date=%s ",(date))
    output = cur.fetchall()
    if len(output)!= 0:
        registered_student_ids = []
        for(x,y) in output:
            y_hour = y.split(":")[0]
            y_minute = y.split(":")[1]
            if(int(y_hour) >= start_hour and int(y_hour) <= end_hour):
                registered_student_ids.append(int(x))
        absent_student_ids = []
        all_student_ids = list(all_students.keys())
        for x in all_student_ids:
            if x not in registered_student_ids:
                absent_student_ids.append(x)
    else:
        absent_student_ids = list(all_students.keys())
    conn.close()
    return absent_student_ids

def absent_emails():
    all_students = getall_students()
    absent_student_ids = registered_vs_absent_students(all_students)
    absent_student_emails = []
    for item in absent_student_ids:
        email = all_students[item]
        absent_student_emails.append(email)
    return absent_student_emails

def get_lecture_email():
    mojar = "lecture"
    conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
    cur = conn.cursor()
    cur.execute("select email_address from attendance where mojar=%s ",(mojar))
    data = cur.fetchall()
    if len(data) != 0:
        lecture_email = data[0][0]
    conn.close()
    return lecture_email

def generate_attendance_sheet():
    dt = datetime.now()
    date = str(dt).split(' ')[0]
    csv_name = 'Attendance_Details/attendance{}.csv'.format(date)
    mark_attendance_obj = Mark_Attendance(csv_filename=csv_name)
    conn = pymysql.connect(host = 'localhost', user = 'root', password ='', database = 'recognition')
    cur = conn.cursor()
    cur.execute('select * from report where date = %s ', (date))
    mydata = cur.fetchall()
    if len(mydata) < 1:
        print("No data found in database")
    else:
        mark_attendance_obj.write_csv_header(id ='Id',student_name='Student_Name',date='Date',time='Time',status='Status')
        for items in mydata:
            attendance_record = list(items)
            mark_attendance_obj.append_csv_rows(records=attendance_record)
    return csv_name


def send_mail():
    all_students = getall_students()
    absent_student_ids = registered_vs_absent_students(all_students)
    absent_student_emails = absent_emails()
    print(absent_student_emails)
    dt = datetime.now()
    dt = dt.strftime("%Y-%m-%d %I:%M:%S")
    date = str(dt).split(' ')[0]
    time = str(dt).split(' ')[0]
    for id in absent_student_ids:
        status = "Absent"
        conn = pymysql.connect(host = "localhost", user = "root", password = "", database = "recognition")
        cur1 = conn.cursor()
        cur1.execute("select fname from attendance where sid=%s ",id)
        output = cur1.fetchone()
        (name,) = output
        cur2 = conn.cursor()
        cur2.execute("insert into report(id,name,date,time,status) VALUES (%s,%s,%s,%s,%s)", (id,
                                                                                              name,
                                                                                              date,
                                                                                              time,
                                                                                              status))
        conn.commit()
        conn.close()
        print("Attendance for absent students has been recorded successfully")

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('mutembeig8@gmail.com','Eng123.GM')
    for email in absent_student_emails:
        server.sendmail('mutembeig8@gmail.com',
                    email,
                    'Hello Dear Student, You are absent on class today.\n\n\nThis is an auto generated message, please do not reply.\n George Mutembei')

    print("Email sent successfully")

    lecture_email = get_lecture_email()
    msg = EmailMessage()
    msg['Subject'] = 'Attendance Details'
    msg['From'] = 'mutembeig8@gmail.com'
    msg['To'] = lecture_email
    msg.set_content('Attendance Report Attached')

    '''csv_name = generate_attendance_sheet()
    with open(csv_name,'rb') as f:
        file_data = f.read()
        file_type = 'csv'
        file_name = f.name'''


    msg.add_attachment('D:/SenoirProject/smart/Attendance_Details/attendance.csv')
    attach = ('Attendance_Details/attendance.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login('mutembeig8@gmail.com','Eng123.GM')
        smtp.send_message(msg)

    print("Report sent successfully")


sched = BackgroundScheduler(daemon=True)
sched.add_job(send_mail,'cron',day_of_week='mon-sun', hour=13, minute=42)
sched.start()



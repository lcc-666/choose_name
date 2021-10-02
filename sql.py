import pymysql

# def getxinxi(file):
#     clase=file.split(".")[0]
#     f=open(file,"r")
#     for line in f.readlines()[1:-1]:
#         print(line)
#         #list=line.split(",")
#         #insert(clase,list[1],list[2].replace("\n",""))
#
#
#
# def creat(clase):
#     db=pymysql.connect(host='www.chaogezuishuai.top',
#                        user="root",
#                        port=3306,
#                        db="name",
#                        password="NRAHbsqt941",
#                        charset="utf8")
#     mycursor = db.cursor()
#     sql="CREATE TABLE %s(id bigint(50),name char(20));" %clase
#     mycursor.execute(sql)
#     mycursor.close()
#     db.close()
#
# def insert(clase,id,name):
#     con = pymysql.connect(host='www.chaogezuishuai.top',
#                          user="root",
#                          port=3306,
#                          db="name",
#                          password="NRAHbsqt941",
#                          charset="utf8")
#     cur=con.cursor()
#     values = (id, name)
#     table = clase
#     sql = "insert into " + table + "(id,name) values(%s,'%s');" % values
#     cur.execute(sql)
#     con.commit()
#     cur.close()
#     con.close()


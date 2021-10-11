import pymysql

# def tongxue(file):
#     db=pymysql.connect(host='www.chaogezuishuai.top',
#                        user="root",
#                        port=3306,
#                        db="name",
#                        password="NRAHbsqt941",
#                        charset="utf8")
#     cursor = db.cursor()
#     sql="SELECT `姓名` FROM `%s`;"%file
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     cursor.close()
#     db.close()
#     ls=[]
#     for i in data:
#         ls.append(i[0])
#     return ls

# def update(clas,name):
#     db=pymysql.connect(host='www.chaogezuishuai.top',
#                        user="root",
#                        port=3306,
#                        db="name",
#                        password="NRAHbsqt941",
#                        charset="utf8")
#     cursor = db.cursor()
#     sql="SELECT `缺课` FROM `%s` WHERE `姓名`='%s';"%(clas,name)
#     cursor.execute(sql)
#     data=cursor.fetchone()
#     data=str(int(data[0])+1)
#     sql="UPDATE `大数据2001` SET `缺课`='%s' WHERE `姓名`='%s';"%(data,name)
#     cursor.execute(sql)
#     db.commit()
#     cursor.close()
#     db.close()
#     return data

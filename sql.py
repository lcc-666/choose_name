import pymysql

def tongxue(file):
    db=pymysql.connect(host='www.chaogezuishuai.top',
                       user="root",
                       port=3306,
                       db="name",
                       password="NRAHbsqt941",
                       charset="utf8")
    cursor = db.cursor()
    sql="SELECT `姓名` FROM `%s`;"%file
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    ls=[]
    for i in data:
        ls.append(i[0])
    return ls



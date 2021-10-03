import pandas as pd
import pymysql
from sqlalchemy import create_engine
def getdata(file):
    df = pd.read_excel(file)[['学号', '姓名']]
    df['缺课']=''
    # 建立连接，username替换为用户名，passwd替换为密码，test替换为数据库名
    conn = create_engine('mysql+pymysql://root:NRAHbsqt941@121.196.244.215:3306/name', encoding='utf8')
    # 写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
    file=file.split("/")[-1].split(".")[0]
    pd.io.sql.to_sql(df, file, conn, if_exists='replace')


def classes(file):
    f=open("classes.txt","r",encoding="utf8")
    clas = file.split("/")[-1].split(".")[0]
    ls=[]

    for line in f.readlines():
        ls.append(line.replace("\n",""))
    f.close()
    if clas in ls:
        return 0
    else:
        f = open("classes.txt", "a+", encoding="utf8")
        f.write(clas+"\n")
        getdata(file)

def get_class():
    f=open("classes.txt","r",encoding="utf-8")
    ls=[]

    for line in f.readlines():
        ls.append(line.replace("\n",""))
    return ls
# file='/home/chaoge/github/choose_name/大数据20asd1.xlsx'
#
# classes(file)
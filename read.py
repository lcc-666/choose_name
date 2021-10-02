import pandas as pd
#file="/home/chaoge/github/choose_name/体育选课学生名单.xlsx"
def getdata(file):
    df = pd.read_excel(file)[['学号', '姓名']]
    df.to_csv('out.csv')

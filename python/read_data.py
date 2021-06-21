import mysql.connector
import pandas as pd

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()


cnx = mysql.connector.connect(
    user='root',  # ユーザー名
    password='password',  # パスワード
    host='mysql_db',  # ホスト名(IPアドレス）
    port=3306,
    database='dse-interview'  # データベース名
)

cursor = cnx.cursor()

df = pd.read_sql("SELECT * FROM sample_data", cnx)


print(df.head(6))


df.to_csv('sample_data_sql', index=True)
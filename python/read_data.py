import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(
    user='root',  
    password='password',  
    host='mysql_db',  
    port=3306,
    database='dse-interview'  
)

cursor = cnx.cursor()

df = pd.read_sql("SELECT * FROM sample_data", cnx)


print(df.head(6))


df.to_csv('sample_data_sql.csv', index=True)
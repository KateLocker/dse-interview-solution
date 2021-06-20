import pandas as pd
import mysql.connector

# Import CSV
data = pd.read_csv ('sample_data.csv', index_col=0)   
df = pd.DataFrame(data)


#df2 = df.where((pd.notnull(df)), None)
df2 = df.astype(object).where(pd.notnull(df), None)

# Connect to SQL Server
cnx = None

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='password',  # パスワード
        host='mysql_db',  # ホスト名(IPアドレス）
        database='dse-interview'  # データベース名
    )

    cursor = cnx.cursor()

#---------------------------------------------------------------------------
    mySql_insert_query = '''
                    INSERT INTO sample_data (
                            SeriousDlqin2yrs, 
                            RevolvingUtilizationOfUnsecuredLines, 
                            age, 
                            NumberOfTime3059DaysPastDueNotWorse,
                            DebtRatio,
                            MonthlyIncome,
                            NumberOfOpenCreditLinesAndLoans,
                            NumberOfTimes90DaysLate,
                            NumberRealEstateLoansOrLines,
                            NumberOfTime6089DaysPastDueNotWorse,
                            NumberOfDependents)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    '''

    records_to_insert = []
    for row in df2.itertuples():
        records_to_insert.append((row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],row[11]))


#-----------------------------------------------------------------------------

    # Insert DataFrame to Table
    cursor.executemany(mySql_insert_query, records_to_insert)
    cnx.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

    cursor.close()


except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
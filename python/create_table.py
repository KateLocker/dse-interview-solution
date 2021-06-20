import mysql.connector

cnx = None

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='password',  # パスワード
        host='mysql_db',  # ホスト名(IPアドレス）
        database='dse-interview'  # データベース名
    )

    cursor = cnx.cursor()

    cursor.execute("DROP TABLE IF EXISTS sample_data")

    cnx.commit() # コミット. (2, koro) のデータは問題なく書き込める．


    sql = '''
    CREATE TABLE sample_data (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        SeriousDlqin2yrs INT, 
        RevolvingUtilizationOfUnsecuredLines DECIMAL(20, 10),
        age INT,
        NumberOfTime3059DaysPastDueNotWorse INT,
        DebtRatio DECIMAL(20, 10),
        MonthlyIncome INT,
        NumberOfOpenCreditLinesAndLoans INT,
        NumberOfTimes90DaysLate INT,
        NumberRealEstateLoansOrLines INT,
        NumberOfTime6089DaysPastDueNotWorse INT,
        NumberOfDependents INT
    )'''
    cursor.execute(sql)

    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()
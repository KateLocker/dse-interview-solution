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

    # cursor.execute("DROP TABLE IF EXISTS student")

    sql = '''
    CREATE TABLE sample_data (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        SeriousDlqin2yrs
        RevolvingUtilizationOfUnsecuredLines
        age
        NumberOfTime30-59DaysPastDueNotWorse
        DebtRatio
        MonthlyIncome
        NumberOfOpenCreditLinesAndLoans
        NumberOfTimes90DaysLate
        NumberRealEstateLoansOrLines
        NumberOfTime60-89DaysPastDueNotWorse
        NumberOfDependents



       student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(50) NULL,
       last_name VARCHAR(50) NULL,
       birthday DATE NULL,
       gender ENUM('F','M')
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
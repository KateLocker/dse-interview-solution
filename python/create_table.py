import mysql.connector

cnx = None

try:
    cnx = mysql.connector.connect(
        user='root', 
        password='password', 
        host='mysql_db', 
        database='dse-interview'  
    )

    cursor = cnx.cursor()

    cursor.execute("DROP TABLE IF EXISTS sample_data")

    cnx.commit() 


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
# Solution to the DSE Assignment

The solution to the assignment is as followed.

* Build the environment for the PoC [docker-compose.yml](docker-compose.yml) in docker (python and mysql).
* Create data structure in 'sample_data' table in 'dse-interview' database in the created mysql server.
* Insert data from the provided csv file [sample_data.csv](python/sample_data.csv) to the 'sample_data' table.
* Access data and create some stats and visualizations.












# Instruction and Memo

## 1. download from gitlab
```
git clone https://gitlab.com/Kate_L/dse-interview.git
```

## 2. Build and run your app with Compose
```
$ docker compose up --build -d
```

## 3. run a command in 'python3' container
```
$ docker compose exec python3 bash
```

### 3-1. create table=sample_data in database=dse-interview
```
$ python3 create_table.py
```
### 3-2. insert data from csv to mysql server 
```
$ python3 insert_data.py
```
### 3-3. read data from mysql server and save a local file
```
$ python3 read_data.py
```
### 3-4. read data from mysql server in Tableau
```127.0.0.1:6603```


### python library
```
$ python -m pip install numpy
$ python -m pip install pandas
$ python -m pip install matplotlib
```

## 4. run a command in 'mysql_db' container
```
$ docker compose exec mysql_db bash
mysql -u root -p
password
```
### Got a package bigger than
```
SET GLOBAL max_allowed_packet=1000000000;
```

### show number of rows and columns in table
```
SELECT COUNT(*) AS num_rows FROM sample_data;
SELECT COUNT(*) AS num_columns FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dse-interview' AND TABLE_NAME = 'sample_data';
```

## 5. hostname
```
hostname -i
```
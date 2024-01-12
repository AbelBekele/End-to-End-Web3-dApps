import pandas as pd
import json
import os
import psycopg2
from psycopg2 import sql, Error
from dotenv import load_dotenv

TRAINEE = "trainee.sql"

cwd = os.getcwd()

load_dotenv()

def DBConnect(dbName=None):
    load_dotenv()

    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    port = os.getenv('DB_PORT')

    if None in (host, user, password, port, dbName):
        raise ValueError("One or more database credentials are missing.")

    conn = psycopg2.connect(host=host, user=user, password=password, dbname=dbName, port=port)
    cur = conn.cursor()
    return conn, cur

def createDB(dbName: str) -> None:
    conn = psycopg2.connect(
        host='192.168.137.236',
        user='postgres',
        password='1001'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{dbName}'")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {dbName}")
    cur.close()
    conn.close()

def createTable(dbName: str, table_schema: str) -> None:
    conn, cur = DBConnect(dbName)
    fd = open(f"{cwd}/scripts/{table_schema}", 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return

def insert_to_table(dbName: str, json_stream: json, table_name: str) -> None:
    conn, cur = DBConnect(dbName)
    insert_data = json.dumps([json.loads(json_stream)])
    df = pd.read_json(insert_data)

    for _, row in df.iterrows():
        sqlQuery = sql.SQL(f"""INSERT INTO {table_name} (trainee, email, asset, status,hashed) VALUES(%s,%s,%s,%s,%s);""")
        data = (row[0], row[1], row[2], row[3], row[4])

        try:
            cur.execute(sqlQuery, data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error: ", e)

    print("All Data Inserted Successfully")
    return

def update_table(dbName: str, json_stream: json, table_name: str) -> None:
    conn, cur = DBConnect(dbName)
    update_data = json.dumps([json.loads(json_stream)])
    df = pd.read_json(update_data)
    for _, row in df.iterrows():
        sqlQuery = sql.SQL(f"""
        UPDATE {table_name} SET asset = %s, status = %s, hashed= %s WHERE email = %s;
        """)

        data = (int(row[0]), str(row[1]), str(row[3]), str(row[2]))

        try:
            cur.execute(sqlQuery, data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error: ", e)

    print("All Data Updated Successfully")
    return

def optin_update(dbName: str, json_stream: json, table_name: str) -> None:
    conn, cur = DBConnect(dbName)
    update_data = json.dumps([json.loads(json_stream)])
    df = pd.read_json(update_data)
    for _, row in df.iterrows():
        sqlQuery = sql.SQL(f"""
        UPDATE {table_name} SET status = %s, remark = %s WHERE asset = %s;
        """)

        data = ((row[0]), (row[1]), int(row[2]))

        try:
            cur.execute(sqlQuery, data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error: ", e)

    print("All Data Updated Successfully")
    return

def db_get_values(dbName: str="trainee"):
    conn, cur = DBConnect(dbName)
    sqlQuery = 'SELECT * FROM trainee;'
    try:
        cur.execute(sqlQuery)
        result = cur.fetchall()
        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        print("Error: ", e)

def db_get_values_by_asset(asset: str, dbName: str="trainee"):
    conn, cur = DBConnect(dbName)
    sqlQuery = sql.SQL(f'SELECT remark,email,hashed FROM trainee WHERE asset = {asset};')
    try:
        cur.execute(sqlQuery)
        result = cur.fetchall()
        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        print("Error: ", e)

def db_get_values_by_addr(addr: str, dbName: str="trainee"):
    conn, cur = DBConnect(dbName)
    sqlQuery = sql.SQL(f'SELECT asset,status,hashed FROM trainee WHERE remark = {addr};')
    try:
        cur.execute(sqlQuery)
        result = cur.fetchall()
        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        print("Error: ", e)

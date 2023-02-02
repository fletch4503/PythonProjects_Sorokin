"""
Connect to database on the host 37.46.131.241
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

#  Надо посмотреть использование модуля MySQL
import mysql.connector
from mysql.connector import Error

# Объявляем функцию подключения к базе
def create_connection(host_name, db_name, user_name, user_password):
    conn_db = None
    try:
        conn_db = mysql.connector.connect(
            host=host_name,
            port=3306,
            db=db_name,
            # Default Port
            user=user_name,
            passwd=user_password
            #      ssl={'ca': '~/.mysql/root.crt'})
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn_db

# Функция запроса в БД
def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
        return cursor
    except Error as e:
        print(f"The error '{e}' occurred")

# Функция выбора и чтения записей из БД
def execute_read_query(conn, query):
    cursor = conn.cursor()
    # result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Теперь подключаемся к БД
connection = create_connection("37.46.131.241", "yc_project", "fletch4503", "Manta_50174416")
# Сюда будем передавать команды для обращения к БД
cursorcmd = "SELECT * FROM mtst WHERE rg_rg_id = 3;"
# cur = conn.cursor()
# cur.execute(cursorcmd)
# Запрашиваем базу
# cur = execute_query(connection, cursorcmd)
# Забираем результат запроса и приводим к читаемому виду
rows = execute_read_query(connection, cursorcmd)
for row in rows:
    print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}')

# Вставляем данные в Таблицу проектов
cursorcmd = """
INSERT INTO 
  `project` 
  (`project_classifier_id`, `project_req_date`, `project_presale_id`, `project_cust_code`, 
   `project_cust_name`,`project_cust_inn`, `project_short_descr`, `project_mtst_id`, 
   `project_region_id`, `project_total_amount`, `project_ktn`, `project_grossprofit`, 
   `project_items_no`, `project_sed_id`, `project_delivery_month`, `project_status_id`, 
   `project_comments`, `project_offer_date`, `Tender`, `TenderDate`, 
   `project_cust_feedback`, `supplier_id`, `suppliername`, `supplieroffertotal_usd`)
VALUES
  (26, '2023-01-28', 4, 951156, 'Сити Сентер Инвестмент Б.В.',
  '9909123302', 'Сборные сервера - 4 + 2шт', 14, 1, 138420,
  1.10, 13842, 'N/A', 'ЗД-402707', '2023-02-15',
  2, 'Сборные сервера - 4 + 2шт', '2023-01-30', 1, '2023-02-02',
  'Wait For Feedback', 1, 'Прайм 24', 15000);
"""
cur = execute_query(connection, cursorcmd)
# m_list = []
# cur = conn.cursor()
# # cur.execute('SELECT version()')
# # print(cur.fetchone()[0])
# mtstlist = cur.execute('SELECT MTST_surname FROM mtst WHERE rg_rg_id = 1;')
# for result in mtstlist:    m_list.append(result[0])
# print(m_list)
connection.close()

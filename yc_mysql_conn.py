"""
Connect to database on the host 37.46.131.241
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

#  Надо посмотреть использование модуля MySQL
import mysql.connector

conn = mysql.connector.connect(
      host="37.46.131.241",
      port=3306,
      db="yc_project",
      user="fletch4503",
      passwd="Manta_50174416")
#      ssl={'ca': '~/.mysql/root.crt'})

cur = conn.cursor()
cur.execute('SELECT version()')

print(cur.fetchone()[0])

conn.close()

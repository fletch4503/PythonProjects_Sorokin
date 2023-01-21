# !/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(
      host="rc1b-no79rbf5nj9c81i3.mdb.yandexcloud.net",
      port=3306,
      db="fletch_db1",
      user="fletch4503",
      passwd="Manta_50174416",
      ssl={'ca': '~/.mysql/root.crt'})

cur = conn.cursor()
cur.execute('SELECT version()')

print(cur.fetchone()[0])

conn.close()
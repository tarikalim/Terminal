import os
from dotenv import load_dotenv
import psutil
import psycopg2
from datetime import datetime

load_dotenv()

host = os.getenv('QUESTDB_HOST')
port = os.getenv('QUESTDB_PORT')
dbname = os.getenv('QUESTDB_DBNAME')
user = os.getenv('QUESTDB_USER')
password = os.getenv('QUESTDB_PASSWORD')

conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password
)
cur = conn.cursor()

cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent
timestamp = datetime.now()

cur.execute(
    "INSERT INTO system_metrics (time, cpu_usage, memory_usage) VALUES (%s, %s, %s);",
    (timestamp, cpu_usage, memory_usage)
)
conn.commit()

cur.close()
conn.close()

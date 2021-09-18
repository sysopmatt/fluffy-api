import pyodbc
import confuse

config = confuse.Configuration('fluffy-api', __name__)

connection = pyodbc.connect(
    server=config['sql']['server'].get(),
    database=config['sql']['database'].get(),
    user=config['sql']['user'].get(),
    tds_version='7.4',
    password=config['sql']['password'].get(),
    port=1433,
    driver='/usr/local/lib/libtdsodbc.so'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM TW")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()


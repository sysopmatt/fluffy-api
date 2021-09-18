import pyodbc
import confuse
import secrets

config = confuse.Configuration('fluffy-api', __name__)

connection = pyodbc.connect(
    driver='{PostgreSQL Unicode}',
    server=config['sql']['server'].get(),
    user=config['sql']['user'].get(),
    password=config['sql']['password'].get(),
    database=config['sql']['user'].get(),
    port=5432
)
cursor = connection.cursor()

installconfirm = input("Would you like to proceed with installation?  All existing SQL configurations will be rest. \
(y/n): ")
if installconfirm.upper()[0:1] == 'Y':
    username = input("Enter your username (email address): ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name (surname): ")
    apikey = secrets.token_hex(16)

    queries = ("""DROP TABLE IF EXISTS FluffyUsers""",
               """
               CREATE TABLE FluffyUsers (
                    ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
                    , Username varchar(255) NOT NULL 
                    , FirstName varchar(255) NULL 
                    , LastName varchar(255) NULL 
                    , ApiKey varchar(255) NULL 
                    , Hash varchar(32) NULL 
               );
               """,
               """
               INSERT INTO FluffyUsers (Username,FirstName,LastName,ApiKey,Hash) 
               SELECT '""" + username + """','""" + firstname + """','""" + lastname + """', '""" + apikey + """', null; 
               """)
    for query in queries:
        cursor.execute(query)
        connection.commit()
    cursor.close()
    connection.close()

    print("!! DO NOT LOSE THIS !!\nYour API key is: " + apikey + "\n !! DO NOT LOSE THIS !!")


else:
    print("Doing nothing.  Goodbye!")

import mysql.connector
def sql(query):
    con = mysql.connector.connect(
        user = "root",
        host = "localhost",
        database = "trail",
        password = "Pragathees@2004"
    )
    cur = con.cursor()
    cur.execute(query)
    print("query executed")
    res = cur.fetchall()
    return res
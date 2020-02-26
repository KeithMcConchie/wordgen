hostname = 'localhost'
username = 'root'
password = 'cassword'
database = 'menagerie'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT owner FROM pet" )

    for owner in cur.fetchall() :
        print(owner)


# print("Using MySQLdb…")
# import MySQLdb
# myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()

# print("Using pymysql…")
# import pymysql
# myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()

print("Using mysql.connector…")
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
import MySQLdb




# Connect to the database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="test"   # IF NO TEST DATABASE CREATE ONE NIGGA
)

def getTuition():  # REMEMBER IMPORT THIS NIGGA
    cursor = db.cursor()

    query = "SELECT value FROM responses WHERE name = `tuition`"   #REMEMBER TO SET TUITION VALUE COLUMN TO INT BERI IMPORTANT NIGGER


    results = cursor.execute(query)

    return results[0]   #This is balyu of tuition fee. each row is represent by tuple. [0] means first column of the row which is the tuition value
   
                        # use from get_tuition import getTuition()  and then call getTuition() function like this cost_per_unit = getTuition()



        #mwah mwah chup chup
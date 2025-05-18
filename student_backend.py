import mysql.connector

def studentData():
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id INT PRIMARY KEY AUTO_INCREMENT,
            StdID TEXT,
            Firstname TEXT,
            Surname TEXT,
            DoB TEXT,
            Age TEXT,
            Gender TEXT,
            Address TEXT,
            Mobile TEXT
        )
    """)
    con.commit()
    con.close()

def addStdRec(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)",
                (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    con.commit()
    con.close()

def searchData(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM student WHERE
        StdID=%s OR Firstname=%s OR Surname=%s OR DoB=%s OR Age=%s OR Gender=%s OR Address=%s OR Mobile=%s
    """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(id, StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Naveen@26", database="catalog")
    cur = con.cursor()
    cur.execute("""
        UPDATE student SET StdID=%s, Firstname=%s, Surname=%s, DoB=%s, Age=%s, Gender=%s, Address=%s, Mobile=%s
        WHERE id=%s
    """, (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()

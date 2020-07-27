import sqlite3

con = sqlite3.connect('mycompany.db')
cObj = con.cursor()

#cObj.execute("CREATE TABLE agent(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT,position TEXT)")
#con.commit()
cObj.execute("CREATE TABLE IF NOT EXISTS agent(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT,position TEXT)")
con.commit()

#cObj.execute("INSERT INTO agent VALUES(1,'Saideepthi', 75000, 'Python', 'Developer')")
#con.commit()
def insert_value(id, name, salary, department, position):
    cObj.execute("INSERT INTO agent VALUES(?,?,?,?,?)",(id, name, salary, department, position))
    con.commit()

#cObj.execute("INSERT INTO agent VALUES(2,'Surya', 95000, 'Java', 'Developer')")
#con.commit()
#cObj.execute("INSERT INTO agent VALUES(?,?,?,?,?)", (3, 'Hello', 55000, 'JS', 'Developer'))
#con.commit()

#cObj.execute("UPDATE agent SET department='PHP' where name='Hello'")
#con.commit()
def update_value(dep, id):
    cObj.execute("UPDATE agent SET department=? where id=?",(dep, id))
    con.commit()

#cObj.execute("SELECT * from agent")
#result = cObj.fetchall()
#print(result)
def sql_fetch():
    cObj.execute("SELECT * from agent")
    result = cObj.fetchall()
    print(result)

#cObj.execute("DELETE FROM AGENT")
#con.commit()
def delete_all():
    cObj.execute("DELETE FROM AGENT")
    con.commit()

#insert_value(1,"saideepthi",75000,"python","developer")
delete_all()

cObj.close()
con.close()
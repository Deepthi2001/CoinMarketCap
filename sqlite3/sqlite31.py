import sqlite3

con = sqlite3.connect('mycompany.db')
cObj = con.cursor()

#cObj.execute("CREATE TABLE agent(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT,position TEXT)")
#commit()

#cObj.execute("INSERT INTO agent VALUES(1,'Saideepthi', 75000, 'Python', 'Developer')")
#con.commit()

#cObj.execute("INSERT INTO agent VALUES(2,'Surya', 95000, 'Java', 'Developer')")
#con.commit()

#cObj.execute("INSERT INTO agent VALUES(?,?,?,?,?)", (3, 'Hello', 55000, 'JS', 'Developer'))
#con.commit()

#cObj.execute("UPDATE agent SET department='PHP' where name='Hello'")
#con.commit()

#cObj.execute("SELECT * from agent")
#result = cObj.fetchall()
#print(result)

cObj.execute("DELETE FROM AGENT")
con.commit()

cObj.close()
con.close()
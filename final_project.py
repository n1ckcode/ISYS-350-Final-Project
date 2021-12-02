
import sqlite3

conn = sqlite3.connect('menu.db')

c = conn.cursor()

# name text, price real, type integer

#all the items that cost $13.95

c.execute("SELECT  * FROM items WHERE price = 13.95")
items = c.fetchall()
print("Answer for Part 1:")
for item in items:
     print(item[0])
#all the items that is less than $9.95

c.execute("SELECT  * FROM items WHERE price < 9.95")
items = c.fetchall()
print("\nAnswer for Part 2:")
for item in items:
     print(item[0])
#all desserts that cost between 4.5 and 8.95

c.execute("SELECT  * FROM items WHERE type = 3 AND price >= 4.5 AND price <= 8.95")
items = c.fetchall()
print("\nAnswer for Part 3:")
for item in items:
     print(item[0])

#all entrees whose cost in not in the range of 9.95 and 12.95

c.execute("SELECT  * FROM items WHERE type = 2 AND price < 9.95 OR price > 12.95")
items = c.fetchall()
print("\nAnswer for Part 4:")
for item in items:
     print(item[0])

#all appetizers in alphabetical order
c.execute("SELECT * FROM items ORDER BY name ASC ")
items = c.fetchall()
print("\nAnswer for Part 5:")
for item in items:
    if item[2] == 1:
        print(item[0])

#The most expensive meal (appetizer).
print("\nAnswer for Part 6:")
print("Most Expensive meal")
print("-------------------")
c.execute("SELECT MAX(price), * FROM items WHERE type = 1")
app = c.fetchone()
formatedapp = "{:,.2f}".format(app[2])
print("Appetizer:", app[1] + "\t" +"$"+ formatedapp)
    

     

#The most expensive meal (entree)
c.execute("SELECT MAX(price), * FROM items WHERE type = 2")
entree = c.fetchone()
formatedentre = "{:,.2f}".format(entree[2])
print("Entree:", entree[1],"\t" + "$"+ formatedentre)

#The most expensive meal (dessert)
c.execute("SELECT MAX(price), * FROM items WHERE type = 3")
des = c.fetchone()
formateddes = "{:,.2f}".format(des[2])
print("Dessert:",des[1],"\t\t" + "$" + formateddes)

#total price
totalprice = app[2] + entree[2] + des[2]
formatedprice = "{:,.2f}".format(totalprice)
print("Total Price:" + "\t\t\t\t\t$" + formatedprice)












conn.commit()

conn.close()

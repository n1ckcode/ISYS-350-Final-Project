# ISYS-350-Final-Project
The program must take input from the table, items from database, menu.db. The database records will be in the format:

Item Name, Item Price, Item Category
Where Item name is of type string, Item Price is of type real (float), and Item Category is of type integer. The item category is an integer describing whether this item is an appetizer (1), an entree (2), or a dessert (3). 

Write a Python program that queries a SQLite database and prints out the following:

All items that cost $13.95.
All items that cost less than $9.95.
All desserts that cost between $4.50 and $8.95.
All entrees that whose cost is not in the range of $9.95 and $12.95.
All appetizers in alphabetical order.
The most expensive meal. The output format should be:

Most Expensive Meal
-------------------
Appetizer: Gran Misto di Fonghi Alla Griglia   $12.95
Entree: Spaghetti Al Filleto di Pomodoro       $19.95
Dessert: Tartufo Gelato al Ciocollate          $7.50
Total Price:                                   $40.40


Python Script By Nicholas Tang

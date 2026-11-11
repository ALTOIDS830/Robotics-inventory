import sqlite3

connection = sqlite3.connect("robotics.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Components(
     ComponentID INTEGER PRIMARY KEY,
    Name TEXT,
    Quantity INTEGER,
    Price REAL
)
""")
#--------------------------------------adding a new thing to the database----------------------------------------
def adding_a_component():
    name = input("Component Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit: "))

    accept = input(f"Name: {name} Quantity: {quantity} Price per unit: {price} is this correct").strip().upper()

    while accept != "Y":
        name = input("Component Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price per unit: "))
        accept = input(f"Name: {name} Quantity: {quantity} Price per unit: {price} is this correct").strip().upper()

    cursor.execute("""
    INSERT INTO Components (Name, Quantity, Price)
    VALUES (?, ?, ?)
    """, (name, quantity, price))

    print("Component added successfully")

    connection.commit()
#--------------------------------------updating an item on the database----------------------------------------
def updating_an_item():
    nameorquan = int(input("1 for quantity, 2 for name"))

    if nameorquan == 1:
        componentid = int(input("ComponentID: "))
        used = int(input("How many were used: "))
        accept = input(f"ComponentID: {componentiD} Used: {used}").strip().upper()
    
        while accept != "Y":
            componentid = int(input("ComponentID: "))
            used = int(input("How many were used: "))
            accept = input(f"ComponentID: {componentiD} Used: {used}").strip().upper()

        cursor.execute("""
        UPDATE Components
        SET Quantity = Quantity - ?
        WHERE ComponentID = ?
        AND Quantity >= ?
        """, (used, componentid, used,))
    
    elif nameorquan == 2:
        name = input("New name: ")
        compid = int(input("ComponentID: "))
        cursor.execute("""
        UPDATE Components
        SET Name = ?
        WHERE ComponentID = ?
        """, (name, compid,))
    
    
    connection.commit()
#--------------------------------------retrieving items from a database----------------------------------------
def retrieving():
    comname = input("Component Name: ")
    cursor.execute("""
    SELECT * FROM Components
    WHERE Name LIKE ?
    """, ("%" + comname + "%",))
    print(cursor.fetchall())
#--------------------------------------displaying the database----------------------------------------
def display():
    cursor.execute("SELECT * FROM Components")

    for component in cursor.fetchall():
        print(component)

#-----------------------------------------Menu------------------------------------
def menu():
    number = int(input("1 For adding a number, 2 for updating a component, 3 retrieving an item, 4 for displaying the full table"))
    while number not in (1, 2, 3, 4):
        number = int(input("Enter a valid number 1 though 4: "))

    if number == 1:
        number1 = int(input("How many new components do you want to add"))
        i = 0
        while i < number1:
            adding_a_component()
            i =+ 1
    elif number == 2:
        number2 = int(input("How many components do you to update: "))
        j = 0
        while j < number2:
            updating_an_item()
            j =+ 1
    elif number == 3:
        number3 = int(input("How many items would you like to retrieve: "))
        k = 0
        while k < number3:
            retrieving()
            k =+ 1
    elif number == 4:
        display()

menu()

connection.commit()
connection.close()



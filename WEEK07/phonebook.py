import csv
from connect import get_connection

# CREATE (вставка из CSV)
def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted from CSV")


# CREATE (ввод с консоли)
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added")


# READ (вывод всех)
def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# READ (фильтр по имени)
def search_by_name(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", ('%' + name + '%',))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# READ (по префиксу телефона)
def search_by_phone_prefix(prefix):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (prefix + '%',))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# UPDATE
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (or press enter): ")
    new_phone = input("New phone (or press enter): ")

    conn = get_connection()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE contacts SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE contacts SET phone=%s WHERE name=%s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Updated")


# DELETE
def delete_contact():
    choice = input("Delete by (1) Name or (2) Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM contacts WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM contacts WHERE phone=%s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")


# MENU
def menu():
    while True:
        print("\n--- PHONEBOOK ---")
        print("1. Insert from CSV")
        print("2. Add contact")
        print("3. Show all")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_by_name(input("Enter name: "))
        elif choice == "5":
            search_by_phone_prefix(input("Enter prefix: "))
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()
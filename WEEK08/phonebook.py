from connect import get_connection

conn = get_connection()
cur = conn.cursor()

# Вставка/обновление примера (можно пропустить, если уже есть)
cur.execute("CALL upsert_contact(%s, %s)", ('Amir', '87001234567'))
conn.commit()

# Вызов функции поиска всех контактов
cur.execute("SELECT * FROM search_contacts(%s)", ('',)) 
results = cur.fetchall()

print("Все контакты:")
for r in results:
    print(r)

cur.close()
conn.close()
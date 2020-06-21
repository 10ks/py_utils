import sqlite3

PATH_DB = "C:/Users/Aaa/Documents/Sqlite_DB/browser_test2.db"

conn = sqlite3.connect(PATH_DB)
c = conn.cursor()
c.execute("""
SELECT *
FROM pills
WHERE imprint like "%BU%"
 """)

result = c.fetchall()
# print(result)

for record in result:
    print("----")
    # print(record)
    print(f"name={record[1]}; imprint={record[2]}")


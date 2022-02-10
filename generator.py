from pathlib import Path
import os
import sqlite3

DB_FILE = "calc.db"
while True:
    try:
        min_num = int(input("Choose the minimum number to generate: "))
        max_num = int(input("Choose the max number to generate: "))
    except ValueError:
        print("Please enter a number.")
    else:
        break

if Path(DB_FILE).exists():
    os.remove(DB_FILE)

con = sqlite3.connect(DB_FILE)
cursor = con.cursor()
cursor.execute("CREATE TABLE math ("
               "rowID INTEGER PRIMARY KEY,"
               "a INTEGER NOT NULL, "
               "symbol TEXT NOT NULL, "
               "b INTEGER NOT NULL, "
               "answer TEXT NOT NULL"  # Setting answer as a text so we can give 0 / 0 = undefined
               ")")
for symbol in ["+", "-", "/", "*"]:
    for a in range(min_num, max_num + 1):
        for b in range(min_num, max_num + 1):
            try:
                answer = eval(f"{a}{symbol}{b}")
            except ZeroDivisionError:
                answer = "Cannot Divide by Zero"
            
            cursor.execute(f"INSERT INTO math "
                           f"(a, symbol, b, answer) VALUES ({a}, \"{symbol}\", {b}, \"{answer}\")"
                           )

        print(f"({a} / {max_num}) for {symbol}")
    con.commit()
cursor.close()
con.close()

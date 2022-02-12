from pathlib import Path
import os
import sqlite3

def custom_range(a, b, step):
    # Same as range, only this supports decimal steps
    # Note: This may have a rounding error, see here for more info -
    # https://stackoverflow.com/questions/477486/how-to-use-a-decimal-range-step-value
    i = a
    # Grabbing how many decimal places step is
    round_to = len(str(step)[2:])

    while i < b:
        yield i
        i = round(i + step, round_to)


DB_FILE = "calc.db"
while True:
    try:
        min_num = int(input("Choose the minimum number to generate: "))
        max_num = int(input("Choose the max number to generate: "))
        step_num = float(input("Choose the number to step by: "))
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
               "a REAL NOT NULL, "
               "symbol TEXT NOT NULL, "
               "b REAL NOT NULL, "
               "answer TEXT NOT NULL"  # Setting answer as a text so we can give 0 / 0 = undefined
               ")")
for symbol in ["+", "-", "/", "*"]:
    for a in custom_range(min_num, max_num + 1, step_num):
        for b in custom_range(min_num, max_num + 1, step_num):
            try:
                answer = eval(f"{a}{symbol}{b}")
            except ZeroDivisionError:
                answer = "Cannot Divide by Zero"
            
            cursor.execute(f"INSERT INTO math "
                           f"(a, symbol, b, answer) VALUES ({a}, \"{symbol}\", {b}, \"{answer}\")"
                           )
        print(f"({a} / {max_num}) for {symbol} ", end="\r")
    con.commit()
    print("")  # adding next line
cursor.close()
con.close()

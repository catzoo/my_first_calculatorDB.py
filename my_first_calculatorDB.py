import sqlite3

DB_FILE = "calc.db"
while True:
    a = input("Please choose the first value: ")
    symbol = input("Please choose a symbol (+, -, /, or *): ")
    b = input("Please choose the second value: ")

    con = sqlite3.connect(DB_FILE)
    cursor = con.cursor()

    cursor.execute("SELECT answer FROM math WHERE a=? AND b=? AND symbol=?", (a, b, symbol))
    answer = cursor.fetchone()
    
    if answer is not None:
        answer = answer[0]

    cursor.close()
    con.close()
    
    if answer is None:
        print(f"Sorry, I don't know the answer to, {a} {symbol} {b}")
    else:
        print(f"{a} {symbol} {b} = {answer}")
    print("")  # Adding another line

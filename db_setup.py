# Personal Finance Management Application

# Database Setup Module
def init_db():
    import sqlite3
    import os

    if not os.path.exists("finance_manager.db"):
        conn = sqlite3.connect("finance_manager.db")
        cursor = conn.cursor()
        # Create users table
        cursor.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL
                        )''')
        # Create transactions table
        cursor.execute('''CREATE TABLE transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER NOT NULL,
                            type TEXT NOT NULL,
                            category TEXT NOT NULL,
                            amount REAL NOT NULL,
                            date TEXT NOT NULL,
                            FOREIGN KEY(user_id) REFERENCES users(id)
                        )''')
        conn.commit()
        conn.close()
        print("Database initialized.")
    else:
        print("Database already exists.")

# User Registration Module
def register_user():
    import sqlite3

    conn = sqlite3.connect("finance_manager.db")
    cursor = conn.cursor()

    username = "test_user"  # Replace with predefined input or external input source
    password = "test_pass"  # Replace with predefined input or external input source

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please try a different one.")

    conn.close()

# User Login Module
def login_user():
    import sqlite3

    conn = sqlite3.connect("finance_manager.db")
    cursor = conn.cursor()

    username = "test_user"  # Replace with predefined input or external input source
    password = "test_pass"  # Replace with predefined input or external input source

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        print(f"Welcome, {username}!")
        return user[0]  # Return user ID
    else:
        print("Invalid username or password.")
        return None

    conn.close()

# Add Income or Expense Module
def add_transaction(user_id):
    import sqlite3

    conn = sqlite3.connect("finance_manager.db")
    cursor = conn.cursor()

    type = "Income"  # Replace with predefined input or external input source
    category = "Salary"  # Replace with predefined input or external input source
    amount = 5000.0  # Replace with predefined input or external input source
    date = "2024-12-28"  # Replace with predefined input or external input source

    cursor.execute('''INSERT INTO transactions (user_id, type, category, amount, date) 
                      VALUES (?, ?, ?, ?, ?)''', (user_id, type, category, amount, date))
    conn.commit()
    print(f"{type} of {amount} added under category '{category}'.")

    conn.close()

# View Transactions Module
def view_transactions(user_id):
    import sqlite3

    conn = sqlite3.connect("finance_manager.db")
    cursor = conn.cursor()

    cursor.execute("SELECT type, category, amount, date FROM transactions WHERE user_id = ?", (user_id,))
    transactions = cursor.fetchall()

    if transactions:
        print("\nYour Transactions:")
        for t in transactions:
            print(f"{t[0]} | {t[1]} | {t[2]} | {t[3]}")
    else:
        print("No transactions found.")

    conn.close()

# Main Function
def main():
    init_db()
    user_id = None

    while True:
        print("\n=== Personal Finance Manager ===")
        if not user_id:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = "2"  # Replace with predefined input or external input source

            if choice == "1":
                register_user()
            elif choice == "2":
                user_id = login_user()
            elif choice == "3":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("1. Add Income/Expense")
            print("2. View Transactions")
            print("3. Logout")
            choice = "1"  # Replace with predefined input or external input source

            if choice == "1":
                add_transaction(user_id)
            elif choice == "2":
                view_transactions(user_id)
            elif choice == "3":
                user_id = None
                print("Logged out successfully.")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

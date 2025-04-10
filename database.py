import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id TEXT UNIQUE,
            username TEXT,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(telegram_id, username, is_admin=0):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (telegram_id, username, is_admin) VALUES (?, ?, ?)", (telegram_id, username, is_admin))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()

def user_exists(telegram_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def is_admin(telegram_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT is_admin FROM users WHERE telegram_id=?", (telegram_id,))
    result = cursor.fetchone()
    conn.close()
    return result and result[0] == 1

def get_all_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username, telegram_id FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

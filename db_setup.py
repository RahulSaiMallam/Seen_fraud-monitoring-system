import sqlite3

def setup_database():
    conn = sqlite3.connect('monitoring_system.db')
    c = conn.cursor()

if __name__ == "__main__":
    setup_database()

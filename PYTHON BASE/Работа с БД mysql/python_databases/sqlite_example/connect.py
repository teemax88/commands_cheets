import sqlite3
from sqlite_example.config import config

# Open connection
connection = sqlite3.connect(config.DB_NAME)

# Creating table from predefined file
connection.cursor().execute(f"""
CREATE TABLE IF NOT EXISTS {config.TABLE}
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT DEFAULT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

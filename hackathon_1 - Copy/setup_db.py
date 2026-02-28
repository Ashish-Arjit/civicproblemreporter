import mysql.connector
import os
from dotenv import load_dotenv

# Load connection details (adjust if not using .env yet)
DB_CONFIG = {
    'host': 'mysql-75514dd-civicproblemreporterdemo1.j.aivencloud.com',
    'user': 'avnadmin',
    'password': 'AVNS_W9eVjuRHHtFDircSCkn',
    'database': 'defaultdb',
    'port': 14188
}

def setup_database():
    print("Connecting to Aiven MySQL...")
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        print("Reading init.sql...")
        with open('init.sql', 'r') as f:
            sql_commands = f.read().split(';')
            
        print("Executing commands...")
        for command in sql_commands:
            if command.strip():
                try:
                    cursor.execute(command)
                    print(f"Executed: {command.strip()[:50]}...")
                except Exception as e:
                    print(f"Error executing command: {e}")
        
        conn.commit()
        print("\n[SUCCESS] Database initialized successfully!")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"\n[ERROR] Failed to connect: {e}")

if __name__ == "__main__":
    setup_database()

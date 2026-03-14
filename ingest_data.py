import sys
import os

# allow python to access project folders
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser.ufdr_parser import parse_ufdr
from database import connect_db


def store_contacts(cursor, contacts):
    for contact in contacts:
        cursor.execute(
            """
            INSERT INTO contacts (name, phone)
            VALUES (%s, %s)
            """,
            (contact["name"], contact["number"])
        )


def store_messages(cursor, messages):
    for msg in messages:
        cursor.execute(
            """
            INSERT INTO messages (sender, receiver, message, timestamp)
            VALUES (%s, %s, %s, %s)
            """,
            (msg["sender"], msg["receiver"], msg["message"], msg["timestamp"])
        )


def store_calls(cursor, calls):
    for call in calls:
        cursor.execute(
            """
            INSERT INTO calls (caller, receiver, duration, timestamp)
            VALUES (%s, %s, %s, %s)
            """,
            (call["caller"], call["receiver"], call["duration"], call["timestamp"])
        )


def ingest_ufdr(file_path):

    contacts, messages, calls = parse_ufdr(file_path)

    conn = connect_db()
    cursor = conn.cursor()

    store_contacts(cursor, contacts)
    store_messages(cursor, messages)
    store_calls(cursor, calls)

    conn.commit()

    cursor.close()
    conn.close()

    print("UFDR data successfully stored in database!")


if __name__ == "__main__":
    ingest_ufdr("dataset/sample_ufdr.json")
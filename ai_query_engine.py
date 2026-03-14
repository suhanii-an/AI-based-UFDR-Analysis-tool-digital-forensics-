import spacy
from backend.database import connect_db

nlp = spacy.load("en_core_web_sm")

def process_query(query):

    conn = connect_db()
    cursor = conn.cursor()

    if "call" in query.lower():

        words = query.split()
        name = words[-1].replace("?", "")

        cursor.execute(
            """
            SELECT caller, receiver, duration, timestamp
            FROM calls
            WHERE caller=%s OR receiver=%s
            """,
            (name, name)
        )

        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return results

    elif "message" in query.lower():

        cursor.execute("SELECT sender, receiver, message FROM messages")

        results = cursor.fetchall()

        cursor.close()
        conn.close()

        return results

    else:
        cursor.close()
        conn.close()
        return ["Query not understood"]
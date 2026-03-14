from backend.database import connect_db


def most_contacted():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT caller, COUNT(*) as total
        FROM calls
        GROUP BY caller
        ORDER BY total DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    print("\nMost Contacted Person:")
    print(result)


def suspicious_messages():

    suspicious_words = ["meet", "money", "transfer", "secret"]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()

    print("\nSuspicious Messages Found:\n")

    for m in messages:
        message_text = m[3].lower()

        for word in suspicious_words:
            if word in message_text:
                print(m)

    cursor.close()
    conn.close()
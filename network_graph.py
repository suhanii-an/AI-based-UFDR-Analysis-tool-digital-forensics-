import networkx as nx
import matplotlib.pyplot as plt
from backend.database import connect_db


def build_network():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT caller, receiver FROM calls")
    calls = cursor.fetchall()

    cursor.execute("SELECT sender, receiver FROM messages")
    messages = cursor.fetchall()

    cursor.close()
    conn.close()

    G = nx.Graph()

    for c in calls:
        G.add_edge(c[0], c[1])

    for m in messages:
        G.add_edge(m[0], m[1])

    plt.figure(figsize=(8,6))

    nx.draw(
        G,
        with_labels=True,
        node_color="lightblue",
        node_size=3000,
        font_size=10
    )

    plt.title("Communication Network")

    plt.show()
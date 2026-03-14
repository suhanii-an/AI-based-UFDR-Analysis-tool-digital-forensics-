import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.ai_query_engine import process_query

query = input("Ask investigation question: ")

process_query(query)
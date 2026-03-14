import sys
import os

# add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser.ufdr_parser import parse_ufdr

contacts, messages, calls = parse_ufdr("dataset/sample_ufdr.json")

print(contacts)
print(messages)
print(calls)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analytics.forensic_insights import most_contacted, suspicious_messages

most_contacted()

suspicious_messages()
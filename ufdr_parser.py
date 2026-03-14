import json

def parse_ufdr(file_path):

    with open(file_path, "r") as file:
        data = json.load(file)

    contacts = data.get("contacts", [])
    messages = data.get("messages", [])
    calls = data.get("calls", [])

    print("Contacts Found:", len(contacts))
    print("Messages Found:", len(messages))
    print("Calls Found:", len(calls))

    return contacts, messages, calls
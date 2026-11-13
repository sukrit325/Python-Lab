contacts = []


def add_contact(name, phone):
  """Adds a new contact to the list."""
  contact = {"name": name, "phone": phone}
  contacts.append(contact)
  print(f"Contact '{name}' added successfully.")


def view_contacts():
  """Displays all available contacts."""
  if not contacts:
    print("No contacts found.")
    return
  print("\n--- Contact List ---")
  for i, c in enumerate(contacts, 1):
    print(
        f"{i}. Name: {c['name']} | Phone: {c['phone']}"
    )


def search_contact(name):
  """Searches for a contact by name."""
  for c in contacts:
    if c["name"].lower() == name.lower():
      print(
          f"Found -> Name: {c['name']}, Phone: {c['phone']}"
          f" {c['']}"
      )
      return c
  print(f"Contact '{name}' not found.")
  return None


def delete_contact(name):
  """Deletes a contact by name."""
  global contacts
  initial_len = len(contacts)
  contacts = [c for c in contacts if c["name"].lower() != name.lower()]
  if len(contacts) < initial_len:
    print(f"Contact '{name}' deleted successfully.")
  else:
    print(f"Contact '{name}' not found.")


if __name__ == "__main__":
  add_contact("Alice Smith", "555-0192")
  add_contact("Bob Jones", "555-0143")
  view_contacts()
  search_contact("Alice Smith")
  delete_contact("Bob Jones")
  view_contacts()
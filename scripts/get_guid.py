import uuid

def get_guid():
    """Generate a new GUID (Globally Unique Identifier)."""
    return uuid.uuid4()

if __name__ == "__main__":
    print("\n\nNew GUID:\n")
    print(get_guid())
    print("\n")
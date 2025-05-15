import sqlite3

# Database file path, ensure this matches the path used in your Flask application
DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def clear_test_contacts():
    """Clear only the test contacts from the database."""
    db = connect_db()
    # Assuming all test contacts follow a specific naming pattern
    cleanup_queries = [
        "DELETE FROM contacts WHERE name IS NULL OR phone IS NULL;",
        "DELETE FROM contacts WHERE name LIKE '%<%' OR phone LIKE '%<%';",
        "DELETE FROM contacts WHERE name LIKE '%script%' OR phone LIKE '%script%';",
        "DELETE FROM contacts WHERE name LIKE '%}}%' OR name LIKE '%{%';",
        "DELETE FROM contacts WHERE name LIKE '%alert%' OR phone LIKE '%alert%';",
        "DELETE FROM contacts WHERE name LIKE 'Test Name %';"
    ]
    for query in cleanup_queries:
        db.execute(query)
    
    db.commit()
    print('Test contacts have been deleted from the database.')
    db.close()

if __name__ == '__main__':
    clear_test_contacts()

import sqlite3

# Create database
conn = sqlite3.connect("complaints.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    subject TEXT,
    description TEXT,
    status TEXT
)
""")

conn.commit()


def add_complaint():
    name = input("Enter your name: ")
    subject = input("Enter complaint subject: ")
    description = input("Enter complaint description: ")

    cursor.execute("""
    INSERT INTO complaints (name, subject, description, status)
    VALUES (?, ?, ?, ?)
    """, (name, subject, description, "Pending"))

    conn.commit()
    print("\nComplaint submitted successfully!")


def view_complaints():
    cursor.execute("SELECT * FROM complaints")
    complaints = cursor.fetchall()

    print("\n----- ALL COMPLAINTS -----")

    if not complaints:
        print("No complaints found.")
        return

    for c in complaints:
        print("\nComplaint ID:", c[0])
        print("Name:", c[1])
        print("Subject:", c[2])
        print("Description:", c[3])
        print("Status:", c[4])


def update_status():
    complaint_id = input("Enter complaint ID: ")
    status = input("Enter new status (Pending/In Progress/Resolved): ")

    cursor.execute(
        "UPDATE complaints SET status=? WHERE id=?",
        (status, complaint_id)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Complaint status updated successfully!")
    else:
        print("Complaint not found.")


def main():
    while True:
        print("\n==============================")
        print(" ONLINE COMPLAINT MANAGEMENT")
        print("==============================")
        print("1. Submit Complaint")
        print("2. View Complaints")
        print("3. Update Complaint Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_complaint()

        elif choice == "2":
            view_complaints()

        elif choice == "3":
            update_status()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


main()

conn.close()
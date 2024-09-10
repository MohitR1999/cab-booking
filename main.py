from cab_booking import add_user, add_driver, make_booking, view_bookings
from db_connection import get_connection

def check_user_exists(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

def check_driver_exists(driver_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM drivers WHERE driver_id = %s", (driver_id,))
    driver = cursor.fetchone()
    cursor.close()
    conn.close()
    return driver is not None

def menu():
    print("\nCab Booking System")
    print("1. Add User")
    print("2. Add Driver")
    print("3. Make a Booking")
    print("4. View Bookings")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")
    return choice

def main():
    while True:
        choice = menu()
        
        if choice == "1":
            name = input("Enter user name: ")
            phone = input("Enter user phone: ")
            email = input("Enter user email: ")
            add_user(name, phone, email)
            print("User added successfully!")

        elif choice == "2":
            name = input("Enter driver name: ")
            phone = input("Enter driver phone: ")
            car_model = input("Enter car model: ")
            license_plate = input("Enter license plate: ")
            add_driver(name, phone, car_model, license_plate)
            print("Driver added successfully!")

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            if not check_user_exists(user_id):
                print(f"User with ID {user_id} does not exist!")
                continue

            driver_id = int(input("Enter driver ID: "))
            if not check_driver_exists(driver_id):
                print(f"Driver with ID {driver_id} does not exist!")
                continue

            pickup_location = input("Enter pickup location: ")
            dropoff_location = input("Enter dropoff location: ")
            make_booking(user_id, driver_id, pickup_location, dropoff_location)
            print("Booking made successfully!")

        elif choice == "4":
            print("\nBookings:")
            view_bookings()

        elif choice == "5":
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

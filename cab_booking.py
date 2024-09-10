from db_connection import get_connection

def add_user(name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    cursor.close()
    conn.close()

def add_driver(name, phone, car_model, license_plate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO drivers (name, phone, car_model, license_plate) VALUES (%s, %s, %s, %s)",
                   (name, phone, car_model, license_plate))
    conn.commit()
    cursor.close()
    conn.close()

def make_booking(user_id, driver_id, pickup_location, dropoff_location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (user_id, driver_id, pickup_location, dropoff_location) VALUES (%s, %s, %s, %s)",
                   (user_id, driver_id, pickup_location, dropoff_location))
    conn.commit()
    cursor.close()
    conn.close()

def view_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    for booking in cursor.fetchall():
        print(booking)
    cursor.close()
    conn.close()

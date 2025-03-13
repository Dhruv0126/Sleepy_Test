import mysql.connector

def get_db_connection():
    # Update these connection details as per your MySQL configuration.
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="sleepwell_db"
    )
    return connection

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(20),
        address VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Products Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        category VARCHAR(50),
        name VARCHAR(255),
        type VARCHAR(50),
        size VARCHAR(50),
        price DECIMAL(10,2),
        stock INT,
        description TEXT
    )
    """)
    
    # Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        product_id INT,
        size VARCHAR(50),
        quantity INT,
        total_price DECIMAL(10,2),
        status VARCHAR(50),
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)
    
    # Bookings Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        booking_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        product_id INT,
        size VARCHAR(50),
        status VARCHAR(50),
        order_id INT DEFAULT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)
    
    # Complaints Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        complaint_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        order_id INT,
        category VARCHAR(50),
        details TEXT,
        status VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
    )
    """)
    
    # Chat Responses Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_responses (
        intent_id INT AUTO_INCREMENT PRIMARY KEY,
        intent VARCHAR(50),
        sub_intent VARCHAR(50),
        response TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    connection.commit()
    cursor.close()
    connection.close()

# Run this module directly to create the tables.
if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")

import pymysql

# Establish DB connection
conn = pymysql.connect(host='localhost', user='root', password='password', database='ocr_data')
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patient_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);
""")

# Insert sample data
def insert_data(name, age):
    cursor.execute("INSERT INTO patient_data (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()

# Example usage
# insert_data("John Doe", 30)
# conn.close()

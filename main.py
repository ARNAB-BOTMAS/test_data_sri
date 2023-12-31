from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connect():
    conn = None
    try:
        conn = sqlite3.connect("person_data.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
    conn = db_connect()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = {
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'gender': row[3],
                'password': row[4]
            }
            users.append(user)

        if len(users) > 0:
            return jsonify(users)
        else:
            return 'No users found', 404
        
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        password = request.form['password']

        sql = """INSERT INTO users (id, name, email, gender, password)
                 VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, (id, name, email, gender, password))
        conn.commit()

        return f"Database updated successfully", 201
    

if __name__ == '__main__':
    app.run(debug=True)
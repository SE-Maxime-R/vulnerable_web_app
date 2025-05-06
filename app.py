from flask import Flask, request, render_template,send_file
import sqlite3,os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
   # New users table with username, password, and role
    conn.execute("DROP TABLE IF EXISTS users")
    conn.execute("""
        CREATE TABLE users (
            username TEXT,
            password TEXT,
            role INTEGER
        )
    """)
    conn.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'root', 1)")
    conn.execute("INSERT INTO users (username, password, role) VALUES ('user', 'noob', 0)")
    conn.execute("INSERT INTO users (username, password, role) VALUES ('isitRealySQLI', 'noWay1is1', 1)")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greetings.html")
def greetings():
    return render_template("greetings.html")

@app.route("/readfile")
def read_file():
    filename = request.args.get("file")  # User-supplied file path

    filepath = os.path.join("logs", filename) 

    try:
        return send_file(filepath)
    except Exception as e:
        return f"💥 Error reading file: {e}"

@app.route("/admin.html")
def admin_page():
    return render_template("admin.html")

@app.route("/admin", methods=["GET"])
def check_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    # 🚨 VULNERABLE SQL INJECTION
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print("Executing:", query)

    try:
        response = ''
        c.execute(query)
        result = c.fetchall()
        if result:
            for i in result:
                if len(result) > 1:
                    response += f"✅ User <b>{i}</b> exists in our complex DB<br>"
                else:
                    response += f"✅ User <b>{i[0]}</b> exists in our complex DB"
            return response
        else:
            return "❌ No such user."
    except Exception as e:
        return f"💥 SQL Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

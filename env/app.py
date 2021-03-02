from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flaskext.mysql import MySQL

import re

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/pets/")
def pets():
    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from pets")
    data = cursor.fetchall()

    return render_template("pets.html", data=data)

@app.route("/pets/add", methods=["GET"])
def pets_add():
    return render_template("pets_add.html")

@app.route("/pets/add", methods=["POST"])
def pets_add_post():
    name = request.form['petName']
    type = request.form['petType']
    family = request.form['familyName']

    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()
    sqlString = "INSERT INTO pets (Name, Type, Family) VALUES (%s, %s, %s)"
    insertTuple = (name, type, family)
    cursor.execute(sqlString, insertTuple)
    conn.commit()

    return redirect(url_for('pets'))

@app.route("/pets/delete", methods=["GET"])
def pets_delete():
    id = request.args["id"]

    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * from pets WHERE PersonID = %s", (id))
    data = cursor.fetchone()
   
    return render_template("pets_delete.html", data=data)

@app.route("/pets/delete", methods=["POST"])
def pets_delete_post():
    id = request.form['id']

    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()
    sqlString = "DELETE FROM pets WHERE PersonID = %s"
    insertTuple = (id)
    cursor.execute(sqlString, insertTuple)
    conn.commit()

    return redirect(url_for('pets'))

@app.route("/pets/edit", methods=["GET"])
def pets_edit():
    id = request.args["id"]

    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * from pets WHERE PersonID = %s", (id))
    data = cursor.fetchone()
   
    return render_template("pets_edit.html", data=data)

@app.route("/pets/edit", methods=["POST"])
def pets_edit_post():
    id = request.form['id']
    name = request.form['petName']
    type = request.form['petType']
    family = request.form['familyName']

    mysql = configMySql()

    conn = mysql.connect()
    cursor = conn.cursor()
    sqlString = "UPDATE pets SET Name = %s, Type = %s, Family = %s WHERE PersonID = %s"
    insertTuple = (name, type, family, id)
    cursor.execute(sqlString, insertTuple)
    conn.commit()

    return redirect(url_for('pets'))

def configMySql():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'user1'
    app.config['MYSQL_DATABASE_PASSWORD'] = '314159265Password!'
    app.config['MYSQL_DATABASE_DB'] = 'pet_info'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)
    return mysql
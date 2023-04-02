from flask import Flask, render_template, request, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

import pickle
model=pickle.load(open("model.pkl",'rb'))
app = Flask(__name__)

app.secret_key = 'Itsasecretkey'

# Database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'employee'

mysql = MySQL(app)
@app.route("/")
def main():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'Uname' in request.form and 'Passwd' in request.form:
        username = request.form['Uname']
        password = request.form['Passwd']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login WHERE Uname = %s AND Passwd = %s', (username, password))
        # Fetch the record and return result
        login = cursor.fetchone()
        # If account exists in accounts table in our database
        if login:
            session['loggedin'] = True
            session['Uname'] = login['Uname']
            return render_template('user.html', info='Logged in successfully!')
        
        else:
            #Account doesnt exist or username/password incorrect
            print('Incorrect username/password!')
            return render_template('login.html', info='Incorrect username/password!')
    

@app.route("/predict", methods=['Post'])
def pred():
    features=[float(i) for i in request.form.values()] 
    pred=model.predict([features]) 
    pred=round(pred[0],2)
    return render_template('success.html',data=pred) 

if __name__=='__main__':
    app.run(host='localhost',port=5000)

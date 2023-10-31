import bcrypt
from flask import Flask, render_template, url_for, redirect, session, request
import db

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.secret_key='secret_key'
salt = bcrypt.gensalt()

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('home.html', logged_in=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        error = None
        
        if request.method == 'POST':
            try:
                username = request.form['username']
                password = request.form['password']
            except KeyError:
                error='Missing form input'
                
            if (username == "" or password == ""):
                error = 'Please fill all the fields'
            else:    
                cxn = db.sqlite3.connect('credentials.db')
                cursor = cxn.cursor()
                cursor.execute('SELECT password_hash FROM users WHERE username = ?',(username,))
                result = cursor.fetchone()
                cxn.close()
                
                if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    session['username'] = username
                    return redirect(url_for('home'))
                else:
                    error = 'Invalid username or password'   
        return render_template('login.html', error=error, logged_in=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        error = None
        
        if request.method == 'POST':
            try:
                username = request.form['username']
                password = request.form['password']
            except KeyError:
                error = 'Missing form input'
                return render_template('register.html', error=error)           
            if (username == "" or password == ""):
                error = 'Please fill all the fields'
            else:
                cxn = db.sqlite3.connect('credentials.db')
                cursor = cxn.cursor()
                cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
                result = cursor.fetchone()
                if result:
                    error = 'User already exists'
                else:
                    password_hash= bcrypt.hashpw(password.encode('utf-8'), salt)
                    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
                    cxn.commit()
                    cxn.close()
                    session['username'] = username
                    return redirect(url_for('home'))
            
        return render_template('register.html', error=error)

@app.route('/about')
def about():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('about.html', logged_in=True)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
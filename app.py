from flask import Flask, render_template, url_for, redirect, session, request

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
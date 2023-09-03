from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__, template_folder='templates')  # Use 'templates' as the template folder

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new-game')
def new_game():
    print("Starting the game...")
    subprocess.Popen(['python', 'pygame_app.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()

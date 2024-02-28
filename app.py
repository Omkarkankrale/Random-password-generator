from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    length = len(password)
    
    if length < 8 or not (has_upper and has_lower and has_digit and has_special):
        return "Weak"
    elif length < 12:
        return "Good"
    else:
        return "Strong"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
        strength = evaluate_password_strength(password)
        return render_template('index.html', password=password, strength=strength)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
   
    if len(password) < 8:
        return False
    
    
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    
    if not any(char.isdigit() for char in password):
        return False
    
     
    special_chars = "!@#$%^&*()-_+=[]{}|;:,.<>?/~"
    if not any(char in special_chars for char in password):
        return False
    
    return True

@app.route('/')
def index():
    return render_template('passwordstrength.html', message='')

@app.route('/check-password', methods=['POST'])
def check_password():
    password = request.form['password']

   
    strength = check_password_strength(password)

   
    message = "Strong password!" if strength else "Weak password! Please ensure it meets the criteria."
    result_class = "strong" if strength else "weak"

    return render_template('passwordstrength.html', message=message, result_class=result_class)

    password = request.form['password']

    
    strength = check_password_strength(password)

    
    message = "Strong password!" if strength else "Weak password! Please ensure it meets the criteria."

    return render_template('passwordstrength.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

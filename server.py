from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "This is a fucking secret key in case somebody cares"

#Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    print(f'Charging {session["first_name"]} {session["last_name"]} for {session["total_fruits"]} fruits')
    return render_template('checkout.html')

@app.route('/fruits')
def fruits():
    return render_template('fruits.html')

@app.route('/process', methods=['POST'])
def process_info():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['strawberries'] = int(request.form['strawberry_quantity'])
    session['bananas'] = int(request.form['banana_quantity'])
    session['apples'] = int(request.form['apple_quantity'])
    session['total_fruits'] = session['strawberries']+session['bananas']+session['apples']
    return redirect('/checkout')



if __name__ == "__main__":
    app.run(debug=True)
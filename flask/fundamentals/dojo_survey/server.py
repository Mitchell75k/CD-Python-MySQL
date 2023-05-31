from flask import Flask, render_template, request, redirect, session #type: ignore
app = Flask(__name__)
app.secret_key = "ThisIsSecret" # you need to set a secret key for security purposes when using session variables

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST']) # here we post the data from the form to the '/process' route and then redirect to the '/result' route
def process():
    print("Got Survery Info")
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['name'] = session['first_name'] + " " + session['last_name']
    print(f"Here's request.form: {request.form}")
    return redirect("/result")

@app.route("/result")
def result():
    return render_template('result.html', name_on_template = session['name'], location_on_template = session['location'], language_on_template = session['language'], comment_on_template = session['comment'])
# we are rendering the result.html template and passing the 'name', 'location', 'comment', and 'language' variables to the template for it to display the information from the form
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5003)
from flask import Flask, render_template, request, redirect, session #type: ignore
app = Flask(__name__)
app.secret_key = "secret_monkey"

@app.route('/')
def index():
    if 'counter' in session: # if the key exists in the session dictionary, then we know that this is not the first time the user is visiting the site
        print('counter exists!')
    else:
        print("key 'counter' does NOT exist") 


    if 'counter' not in session: # if the counter key is not in the session dictionary, then we set the counter to 0
        session['counter'] = 0
    else:
        session['counter'] +=1 # if the counter key is in the session dictionary, then we know that this is not the first time the user is visiting the site and we can increment the counter by 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear() #if there were more cookies, we could use session.pop('counter') to remove only the key-value pair that we want to remove, which would be the counter key-value pair in this case
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['counter'] +=1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5003)
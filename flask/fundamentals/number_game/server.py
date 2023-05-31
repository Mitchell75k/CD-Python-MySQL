from flask import Flask, render_template, request, redirect, session #type: ignore
import random
app = Flask(__name__)
app.secret_key = "dolphin" # you need to set a secret key for security purposes when using session variables

@app.route('/')
def index():
    if 'number' not in session: # if there is no number in session, then create one. This also applies to the attempt_num and guess keys below
        session['number'] = random.randint(1, 100)
    print(f" The number is: {session['number']}")
    
    if 'attempt_num' not in session:
        session['attempt_num'] = 0
    else: # if there is an attempt_num in session, then add 1 to it
        session['attempt_num'] += 1
    print(f" Attempt: {session['attempt_num']}")
    
    if 'guess' in session: 
        print(f" Guess: {session['guess']}")
    print(f" Session: {session}") # this will print all the keys and values stored in session
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess']) # this is the guess that the user inputs, which is stored in session
    return redirect('/')
#    if session['guess'] == session['number']: #I attempted to use this if statement to redirect to the winner page that has a leaderboard, but it didn't work
#        return redirect('/win')
#    else:
#    return redirect('/')

#@app.route('/win')
#def win():
#    return render_template('winner.html')

#@app.route('/winner')
#def winner():
#    session['player'] = request.form['player']
#    return redirect('/win')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5004)
from flask import Flask, request, render_template, redirect # type: ignore
from newuser import User

app = Flask(__name__)
app.secret_key = 'red'
# Render the index page
@app.route('/')
def index():
    return redirect('/users')
# Render the users page
@app.route('/users')
def view_users():
    return render_template("Read(All).html",users=User.get_all())
# Render the new user page
@app.route('/users/new')
def new_user():
    return render_template('Create.html')
# Create a new user
@app.route('/users/create', methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')
# Update a user
@app.route('/users/<int:id>/edit')
def edit_user(id):
    return render_template('Update.html', user=User.get_one(id))
# Update a user
@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    form_data = {
        'id': id,
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
    }
    print("Form Data:", form_data)  # Print the form data for debugging purposes
    result = User.update(form_data)
    print("Update Result:", result)  # Print the update result for debugging purposes
    return redirect('/users')

# Delete a user
@app.route('/users/<int:id>/delete')
def delete_user(id):
    User.delete(id)
    return redirect('/users')
# View a user+
@app.route('/users/<int:id>')
def view_user(id):
    return render_template('Read(One).html', user=User.get_one(id))

if __name__ == '__main__':
    app.run(debug=True, port=5009)

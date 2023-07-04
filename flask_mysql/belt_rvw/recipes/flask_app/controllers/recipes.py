from flask_app import app
from flask import redirect, render_template, request , session, flash, url_for # type: ignore
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to continue")
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return redirect (url_for('success', id = data['id']))

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        flash("Log in to continue!")
        return redirect('/')
    return render_template('new_recipe.html')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'], 
        'under_30': request.form['under_30'],
        'user_id': session['user_id']
    }
    recipe = Recipe.save_recipe(data)
    print(f"Recipe created: {recipe}")
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show_recipe(id):
    if 'user_id' not in session:
        flash("Please log in to continue")
        return redirect('/')
    data = {
        'id': id
    }
    user_id = session['user_id']
    print(session['user_id'])
    user = User.get_by_id({'id': user_id})
    print(f"YOUR USER IS: {{{user}}}")
    return render_template('recipe_details.html', user = user, recipe=Recipe.get_recipes_by_id(data))

@app.route('/recipes/<int:id>/delete')
def delete_recipe(id):
    data = {
        'id': id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')


@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    if 'user_id' not in session:
        flash("Please log in to continue")
        return redirect('/')
    data = {
        'id': id
    }
    return render_template('edit_recipe.html', recipe=Recipe.get_recipes_by_id(data))

@app.route('/recipes/<int:id>/update', methods=['POST'])
def update_recipe(id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/{id}/edit')
    data = {
        'id': id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked': request.form['date_cooked'], 
        'under_30': request.form['under_30'],
        'user_id': session['user_id']
    }
    Recipe.update_recipe(data)
    return redirect('/dashboard')
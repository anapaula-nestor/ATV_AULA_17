from flask import Flask, render_template, request, redirect

from controllers.category_controller import CategoryController
from models.category import Category

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/category/<action>', methods=['GET', 'POST'])
def create_update_category(action):
    ca = None
    if request.method == 'POST':
        if action == 'Create':
            ca = Category(request.form['name'], request.form['description'])
            CategoryController().create(ca)
            return redirect("/list_category")
        elif action == 'Update':
            id_ = request.form['id']
            ca = CategoryController().read_by_id(int(id_))
            ca.name = request.form['name']
            ca.description = request.form['description']
            CategoryController().update(ca)
            return redirect('/list_category')
    return render_template('create_update_category.html', category=ca, action='Create')


@app.route('/list_category')
def list_category():
    list_category = CategoryController().read_all()
    return render_template('list_category.html', list=list_category)


@app.route('/update_category/<id>')
def update_category(id):
    ca = CategoryController().read_by_id(int(id))
    return render_template('create_update_category.html', category=ca, action='Update')


@app.route('/delete_category/<id>')
def delete_category(id):
    ca = CategoryController().read_by_id(int(id))
    CategoryController().delete(ca)
    return redirect('/list_category')


app.run(debug=True)
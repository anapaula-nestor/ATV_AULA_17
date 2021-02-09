from flask import Flask
from flask_restful import Api
from resources.category_resource import CategoryResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResource, '/api/category', endpoint='category')
api.add_resource(CategoryResource, '/api/category/<int:id>', endpoint='categories')



app.run(debug=True)
from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for
from flask_httpauth import HTTPBasicAuth

from app import app
from app.controller.UserController import UserController
from app.controller.RecipeController import RecipeController
from app.controller.CategoryController import CategoryController
from flask_jwt import JWT, jwt_required, current_identity

import jwt

user = UserController()
recipe = RecipeController()
category = CategoryController();
auth = HTTPBasicAuth()

#app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
  
jwt = JWT(app, user.authenticate, user.identity)



@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(name=username_or_token).first()
        if not user:
            return False
    g.user = user
    return True

email = "adelinetush@gmail.com"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adeline','email':email} 
    return render_template('index.html', title='Home', user=user)

@app.route('/')
@app.route('/signup')
def signup():
    return render_template('signup.html', title='SignUp')

@app.route('/categories')
def categories():
    user = {'username': 'Adeline','email':email} 
    return render_template('categories.html', title='Categories', user=user)

@app.route('/recipes')
def recipes():
    user = {'username':'Adeline', 'email': email}
    return render_template('recipes.html', title='Recipes', user=user)

@app.route('/createrecipe')
def createrecipe():
    user = {'username': 'Adeline','email':email} 
    return render_template('createrecipe.html', title='CreateRecipe',user=user)

@app.route('/createcategory')
def createcategory():
    user = {'username': 'Adeline','email':email} 
    return render_template('createcategory.html', title='CreateCategory', user=user)

@app.route('/allrecipes')
def allrecipes():
    return render_template('allrecipes.html', title='AllRecipes')

@app.route('/allcategories')
def allcategories():
    return render_template('allcategories.html', title='AllCategories')

@app.route('/allrecipescat')
def allrecipescat():
    return render_template('allrecipescat.html', title='AllRecipes')

@app.route('/editrecipe')
def editrecipe():
    user = {'username': 'Adeline','email':email} 
    return render_template('editrecipe.html', title='EditRecipe',  user=user)


@app.route('/editcategory')
def editcategory():
    user = {'username': 'Adeline','email':email} 
    return render_template('editcategory.html', title='EditCategory',  user=user)




#Saving and retrieving
@app.route("/auth/register")
def register():
    name = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    if email is None or password is None:
        abort(400)
    response = user.register(name, email, password)
    print(response)
    return jsonify(response)

@app.route("/auth/login")
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    response = user.login(email, password)
    return jsonify(response)

#Sample auth functions
@app.route("/api/resource")
@auth.login_required
def get_resource():
    return jsonify({'data':'Hello there, %s' % g.user.name})

@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


#Recipe Functions
@app.route("/qu")
@jwt_required()
def listUserRecipes():
    username = request.args.get("username")
    response = recipe.get_user_recipes(username)
    return jsonify(response)


@app.route("/q")
def listRecipes():
    name = request.args.get("name")
    response = recipe.get_recipe(name);
    return jsonify(response)

@app.route("/qr")
def searchRecipeByName():
    name = request.args.get("name")
    response = recipe.get_recipe_name(name);
    return jsonify(response)

@app.route("/qri")
def searchRecipeById():
    id = request.args.get("id")
    response = recipe.get_recipe_id(id);
    return jsonify(response)

@app.route("/qci",methods=['GET'])
def searchCategoryById():
    id = request.args.get("id")
    response = category.get_category_id(id);
    return jsonify(response)



@app.route("/qg")
def getRecipesForCategory():
    name = request.args.get("name")
    ir = int(name)
    response = recipe.get_recipe_category(ir);
    return jsonify(response)

@app.route("/ar",methods=['POST'])
def addRecipes():
    r = request.get_json()
    response = recipe.add_recipe(r)
    return jsonify(response)

@app.route("/ur",methods=['POST'])
def updateRecipe():
    r = request.get_json()
    response = recipe.update_recipe(r)
    return jsonify(response)

@app.route("/uc",methods=['POST'])
def updateCategory():
    r = request.get_json()
    response = category.update_category(r)
    return jsonify(response)

@app.route("/dr")
def delete_recipe():
    id = request.args.get('id')
    res = recipe.delete_recipe(id)
    return jsonify(res)

#Category Functions
@app.route("/ac",methods=['POST'])
def addCategory():
    r = request.get_json()
    response = category.add_category(r)
    return jsonify(response)


@app.route("/guc")
def get_user_category():
    email = request.args.get('email')
    res = category.get_user_category(email)
    return jsonify(res)

@app.route("/gac")
def get_all_category():
    res = category.get_all_category()
    return jsonify(res)

@app.route("/dc")
def delete_category():
    id = request.args.get('id')
    ir = int(id)
    res = category.delete_category(ir)
    return jsonify(res)

@app.route("/uc")
def update_category():
    cat = request.get_json()
    res = category.update_category(cat)
    return jsonify(res)
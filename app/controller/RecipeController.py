#from app.models.Recipe import Recipe
from app.models.model.Model import Recipe
from app.models import db


class RecipeController:
    def __init__(self):
        self.recipes = [];


    def add_recipe(self, rec):
        """Store Category to Database"""
        self.recipes = [];
        if not db.session.query(Recipe).filter(Recipe.name == rec['name']).count():
            r = Recipe(rec['category'],rec['name'],rec['email'],rec['description'],rec['ingredients']);
            db.session.add(r)
            db.session.commit()
        for rec in Recipe.query.filter(Recipe.email == rec['email']):
            self.recipes.append(rec.serialize())
        return self.recipes

    def get_recipe(self, name):
        li = [];
        for recipe in Recipe.query:
                li.append(recipe.serialize())
        return li

    def get_recipe_name(self, name):
        li = [];
        for recipe in Recipe.query:
            if name in recipe.name:
                li.append(recipe.serialize())
        return li

    def get_recipe_id(self, id):
        li = [];
        id = int(id)
        for recipe in Recipe.query:
            if id == recipe.id:
                li.append(recipe.serialize())
        return li

    def update_recipe(self, rec):
        id = rec['id']
        for recipe in Recipe.query.filter(Recipe.id == id):
            recipe.name = rec['name'];
            recipe.description = rec['name'];
            recipe.ingredients = rec['ingredients']
            recipe.description = rec['description']
            db.session.commit()
            return True
        return False

    def delete_recipe(self,id):
        id = int(id)
        for recipe in Recipe.query.filter(Recipe.id == id):
            db.session.delete(recipe)
            db.session.commit()
            return True;
        return False

    def get_recipe_category(self, cat):
        li = [];
        for recipe in Recipe.query.filter(Recipe.category==cat):
            li.append(recipe.serialize())
        return li;

    def get_user_recipes(self, email):
        li = [];
        for recipe in Recipe.query.filter(Recipe.email == email):
            if(recipe.email==email):
                li.append(recipe.serialize())
        return li
                

    def add_recipe_memory(self, rec):
        r = Recipe(rec['category'],rec['name'],rec['email'],rec['description'],rec['ingredients']);
        self.recipes.append(r.serialize())
        return self.recipes
    
    def get_recipe_memory(self, name):
        li = [];
        for recipe in self.recipes:
            if(name in recipe['name']):
                li.append(recipe)
        return li


    def get_user_recipes_memory(self, email):
        li = [];
        for recipe in self.recipes:
            if(recipe['email']==email):
                li.append(recipe)
        return li

    def get_user_recipe_memory(self, rec):
        li = [];
        for recipe in self.recipes:
            if(recipe['name']==rec['name']):
                recipe = rec
                li.append(recipe)
        return li
                

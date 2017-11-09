class Recipe:
    def __init__(self, category, name, email, description, ingredients):
        self.category = category;
        self.name = name
        self.email = email
        self.description = description
        self.ingredients = ingredients

    def set_name(self, name):
        self.name = name

    def set_category(self, category):
            self.category = category

    def get_ingredients(self):
        return self.ingredients

    def set_description(self, description):
        self.description = description

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def serialize(self):
            return {
            'category': self.category,
            'email':self.email,
            'name':self.name,
            'description':self.description,
            'ingredients': self.ingredients
    }
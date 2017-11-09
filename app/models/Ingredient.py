class Ingredient:
    def __init__(self, name, recipeId, description, quantity):
        self.name = name
        self.recipe_id = recipeId
        self.description = description
        self.quantity = quantity

    def setName(self, name):
        self.name = name
    
    def setRecipeId(self, recipe_id):
        self.recipe_id = recipe_id
    
    def setQuantity(self, quantity):
        self.quantity = quantity
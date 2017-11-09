from app.models.model.Model import Category
from app.models.model.Model import Recipe
#from app.models.model import Category
from app.models import db



class CategoryController:
    """Manage Category Controller"""
    def __init__(self):
        self.categories = [];
        self.count = 1


    def add_category(self, cat):
        """Store Category to Database"""
        self.categories = [];
        if not db.session.query(Category).filter(Category.name == cat['name']).count():
            c = Category(cat['email'],cat['name'],cat['description'])
            db.session.add(c)
            db.session.commit()
        for cat in Category.query.filter(Category.email == cat['email']):
            self.categories.append(cat.serialize())
        return self.categories

    def get_category_id(self, id):
        li = [];
        id = int(id)
        for category in Category.query:
            if id == category.id:
                li.append(category.serialize())
        return li

        '''
    def update_category(self, cat):
        id = cat['id']
        for category in Category.query.filter(Category.id == id):
            category.name = cat['name'];
            category.description = cat['description']
            db.session.commit()
            return True
        return False
        '''
    def get_user_category(self,email):
        guc = []
        for cat in Category.query.filter(Category.email == email):
            guc.append(cat.serialize())
        return guc

    def get_all_category(self):
        gac = []
        for cat in Category.query:
            gac.append(cat.serialize())
        return gac

    def update_category(self, cat):
        id = int(cat['id'])
        for category in Category.query.filter(Category.id == id):
            category.name = cat['name']
            category.description = cat['description']
            db.session.commit();
            return True
        return False;
        
    def delete_category(self, id):
        id = int(id)
        if(Category.query.filter(Category.id == id).count()>0):
            for cat in Category.query.filter(Category.id == id):
                for recipe in Recipe.query.filter(Recipe.category == id):
                    db.session.delete(recipe)
                    db.session.commit()
                db.session.delete(cat)
                db.session.commit()
            return True
        return False;

    def add_category_memory(self, cat):
        """Deprecated Store to Memory Functions"""
        c = None
        c = Category(cat['email'],cat['name'],cat['description'])
        self.count += 1
        self.categories.append(c.serialize())
        return self.categories

    def delete_category_memory(self,item):
        """Deprecated Store to Memory Functions"""
        for i in self.categories:
            if(i['name']==item['name']):
                i =  None
                return True
        return False
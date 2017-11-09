import unittest

from app.models.Recipe import Recipe

class test_recipe(unittest.TestCase):
    
    def test_add_recipe(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("flour")
        self.assertEqual((r.get_ingredients())[0],"flour")

    def test_get_ingredients_adds_value(self):
        r = Recipe(1,"Pumpkin Pie","adelinetush@gmail.com","Yummy",[])
        r.add_ingredient("Pumpkin");
        self.assertEqual(len(r.get_ingredients()),1)
        

if(__name__=='__main__'):
    unittest.main()
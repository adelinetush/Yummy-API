import unittest

from flask import render_template
from flask import request
from flask import jsonify, abort, request, jsonify, g, url_for

from app import app
from app.models import db
from app.models.model.Model import Category
from app.controller.CategoryController import CategoryController



category = CategoryController();

class test_category_controller(unittest.TestCase):
    
    def test_add_category_memory(self):
        r = dict()
        r['email'] = "adelinetush@gmail.com"
        r['name'] = 'test'
        r['description'] = 'test description'
        response = category.add_category_memory(r)
        self.assertGreater(len(response),0)

    def test_delete_category_memory(self):
        r = dict()
        r['email'] = "adelinetush@gmail.com"
        r['name'] = 'test'
        r['description'] = 'test description'
        response = category.add_category_memory(r)
        rm = category.delete_category_memory(r)
        self.assertEqual(rm, True)



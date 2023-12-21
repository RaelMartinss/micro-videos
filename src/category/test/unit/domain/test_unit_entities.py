from dataclasses import is_dataclass
from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name='Movies')
        self.assertEqual(category.name, 'Movies')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

        category = Category(
            name='Movies', 
            description='some description', 
            is_active=False, 
            created_at=datetime.now()
        )
        self.assertEqual(category.name, 'Movies')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, False)
        self.assertIsInstance(category.created_at, datetime)
    
    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie 1')
        category2 = Category(name='Movie 2')
        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )




#python -m unittest category.test.unit.domain.test_unit_entities
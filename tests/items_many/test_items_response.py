import unittest
from time import sleep
from ...run import app 
from ..config.db import db


class TestItemsResponse(BaseCase):
    def setUp(self):
        self.client = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def test_get_items_has_field_content_list(self):
        response = self.client.get('/v2/items')
        self.assertIn('content', response.json)
        self.assertEqual(type(response.json['content']), list)

    def test_get_items_has_json(self):
        response = self.client.get('/v2/items')
        self.assertEqual(type(response.json), dict)

    def test_get_items_has_id(self):
        response = self.client.get('/v2/items')
        for document in response.json['content']:
            print(document)
            #self.assertIn(document, '_id')

    def test_get_items_has_no_mongo_oid(self):
        response = self.client.get('/v2/items')
        for document in response.json['content']:
            self.assertNotIn(document['_id'], '$oid')

    def test_get_items_has_no_mongo_data(self):
        pass

    def test_get_items_success_has_field_result(self):
        pass

    def test_get_items_error_has_field_error(self):
        pass

    
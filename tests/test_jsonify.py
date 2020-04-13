import unittest
import jsonify.jsonify as jsonify


class JsonifyTestCase(unittest.TestCase):
    def test_load_dir(self):
        structure = jsonify.load_dir('./src')

        self.assertTrue('jsonify.py' in structure,
                        'jsonify.py absent in "src/" directory')
        self.assertEqual(structure['jsonify.py'], None,
                         'jsonify.py is not a file')

    def test_empty_structure_for_fake_path(self):
        structure = jsonify.load_dir('./src/hello')

        self.assertEqual(structure, {})

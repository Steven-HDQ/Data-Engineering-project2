import unittest
import os
import requests

class FlaskTests(unittest.TestCase):
	
	def setUp(self):
		os.environ['NO_PROXY'] = '0.0.0.0'
		self.text=""
		pass
		
	def test_1_index(self):
		responce = requests.get('http://localhost:5000')
		self.assertEqual(responce.status_code, 200)

	def test_2_test_text(self):
		params = {
			'text': self.text
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual('Similar Tweets:' in responce.text,False)

	def test_3_test_text(self):
		params = {
			'text': "make American great again"
		}
		responce = requests.post('http://localhost:5000', data=params)
		self.assertEqual(responce.status_code, 200)
		self.assertEqual('Similar Tweets:' in responce.text,True)

if __name__ == '__main__':
	unittest.main()		





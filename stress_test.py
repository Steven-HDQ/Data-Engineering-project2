import unittest
import os
import grequests
import requests
import time

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
	
	def test_4_test_text(self):
		start = time.time()
		test_num=1000
		success_num=0
		fail_num=0
		req_list = [grequests.get('http://localhost:5000') for i in range(test_num)]
		res_list = grequests.map(req_list)
		for res in res_list:
			if res.status_code==200:
				success_num+=1
			else:
				fail_num+=1
		end = time.time()
		print('Get Stress Test:')
		print('Test Number:',test_num)
		print('Success Number:',success_num)
		print('Fail Number:',fail_num)
		print('Time used:',end-start)
		self.assertEqual(success_num, test_num)
		self.assertEqual(fail_num, 0)
		self.assertEqual((end-start)<60 ,True)

	def test_5_test_text(self):
		start = time.time()
		test_num=1000
		success_num=0
		fail_num=0
		params = {'text': "Hello"}
		req_list = [grequests.post('http://localhost:5000',data=params) for i in range(test_num)]
		res_list = grequests.map(req_list,size=100)
		for res in res_list:
			if res.status_code==200:
				success_num+=1
			else:
				fail_num+=1
		end = time.time()
		print('Post Stress Test:')
		print('Test Number:',test_num)
		print('Success Number:',success_num)
		print('Fail Number:',fail_num)
		print('Time used:',end-start)
		self.assertEqual(success_num, test_num)
		self.assertEqual(fail_num, 0)
		self.assertEqual((end-start)<60 ,True)

if __name__ == '__main__':
	unittest.main()		





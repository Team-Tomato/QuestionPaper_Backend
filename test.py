try:
    from app import app
    import unittest
    import json

except Exception as e:
    print("some modules are missing {} ".format(e))

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "question":
                {
                "subjectName": "tamil",
                "shortForm": "tam",
                "staff": "youtube",
                "year": "2011",
                "url": "https://www.codespeedy.com/"
                }
        }
        self.data1 = {
            "question":
                {
                    "subjectName": "network",
                    "shortForm": "nm",
                    "staff": "youtube",
                    "year": "3000",
                    "url": "http_type"
                }
        }

        self.data2 = {
            "book":
                {
                    "title": "fundamentals",
                    "author": "anitha",
                    "publisher": "somebody",
                    "isbn": "123456789011",
                    "url": "https://book.com"
                }
        }
        self.data3 = {
            "book":
                {
                    "title": "fundamental",
                    "author": "anitha",
                    "publisher": "somebody",
                    "isbn": "12345678901178979879",
                    "url": "https type"
                }
        }

#Question testing
    #check if response is 200
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)

    #check for data return
    def test_index_data(self):
        res = self.client.get('/')
        self.assertTrue(b'Team Tomato' in res.data)
    """
    #positive test for add question
    def test_add_question_positive(self):
        res = self.client.post(path = '/api/v1/question/add',data=json.dumps(self.data),content_type ='application/json')
        self.assertEqual(res.status_code,200)

    # negative test for add question
    def test_add_question_negative(self):
        res = self.client.post(path='/api/v1/question/add', data=json.dumps(self.data1),content_type='application/json')
        self.assertTrue(b'valid' in res.data)

    #check if response is 200 for get all question
    def test_get_all_question(self):
        res = self.client.get('/api/v1/question')
        self.assertEqual(res.status_code,200)

    #positive testing  for get question by id
    def test_get_question_positive(self):
        res = self.client.get('/api/v1/question/20')
        self.assertEqual(res.status_code,200)

    #negative testing  for get question by id
    def test_get_question_negative(self):
        res = self.client.get('/api/v1/question/50')
        self.assertTrue(b'no attribute'in res.data)

    #positive testing for search question
    def test_search_question_positive(self):
        res = self.client.get('/api/v1/question/search?search_str=hari')
        self.assertEqual(res.status_code,200)

    #positive testing for search question
    def test_search_question_negative(self):
        res = self.client.get('/api/v1/question/search?search_str=mfjijdjfjsdfjdjfsdjfsff')
        self.assertEqual(res.data,b'[]\n')
"""

#Book testing
#positive test for add book
    def test_add_book_positive(self):
        res = self.client.post(path = '/api/v1/book/add',data=json.dumps(self.data2),content_type ='application/json')
        self.assertEqual(res.status_code,200)

    # negative test for add book
    def test_add_book_negative(self):
        res = self.client.post(path='/api/v1/book/add', data=json.dumps(self.data3),content_type='application/json')
        self.assertTrue(b'valid' in res.data)

    #check if response is 200 for get all books
    def test_get_all_book(self):
        res = self.client.get('/api/v1/book/all')
        self.assertEqual(res.status_code,200)

    #positive testing for search question
    def test_search_book_positive(self):
        res = self.client.get('/api/v1/book/search?search_str=anitha')
        self.assertEqual(res.status_code,200)

    #positive testing for search question
    def test_search_book_negative(self):
        res = self.client.get('/api/v1/book/search?search_str=mfjijdjfjsdfjdjfsdjfsff')
        self.assertEqual(res.data,b'[]\n')







if __name__ == "__main__":
    unittest.main()
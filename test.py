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
#positive testing
    #check if response is 200
    def test_index(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code,200)

    #check for data return
    def test_index_data(self):
        res = self.client.get('/')
        self.assertTrue(b'Team Tomato' in res.data)

    #positive test for add question
    def test_add_question_positive(self):
        res = self.client.post(path = '/api/v1/question/add',data=json.dumps(self.data),content_type ='application/json')
        self.assertEqual(res.status_code,200)

    # negative test for add question
    def test_add_question_negative(self):
        res = self.client.post(path='/api/v1/question/add', data=json.dumps(self.data1),content_type='application/json')
        self.assertTrue(b'valid' in res.data)



if __name__ == "__main__":
    unittest.main()
import requests,unittest
class test_login(unittest.TestCase):
    def login(self):
        session=requests.Session()
        verify="http://localhost/index.php?m=Home&c=User&a=verify"
        login="http://localhost/index.php?m=Home&c=User&a=do_login"
        response_verify = session.get(verify)
        data={"username": "13761263624", "password": "123456", "verify_code": "8888"}
        response_login = session.post(url=login,data=data)
        print(response_login.json())
        session.close()
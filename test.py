import requests,unittest
from parameterized import parameterized


class test_login(unittest.TestCase):
    p_list=[("13761263624","123456","8888")]
    @parameterized.expand(p_list)
    def test_login(self,username,password,verify_code):
        session=requests.Session()
        verify="http://localhost/index.php?m=Home&c=User&a=verify"
        login="http://localhost/index.php?m=Home&c=User&a=do_login"
        response_verify = session.get(verify)
        data={"username":username, "password": password, "verify_code": verify_code}
        response_login = session.post(url=login,data=data)
        print(response_login.json())
        session.close()

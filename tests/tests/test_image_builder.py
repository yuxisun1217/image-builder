import unittest
import logging
import time
import requests

AuthString0 = "eyJlbnRpdGxlbWVudHMiOnsiaW5zaWdodHMiOnsiaXNfZW50aXRsZWQiOnRydWV9LCJzbWFydF9tYW5hZ2VtZW50Ijp7ImlzX2VudGl0bGVkIjp0cnVlfSwib3BlbnNoaWZ0Ijp7ImlzX2VudGl0bGVkIjp0cnVlfSwiaHlicmlkIjp7ImlzX2VudGl0bGVkIjp0cnVlfSwibWlncmF0aW9ucyI6eyJpc19lbnRpdGxlZCI6dHJ1ZX0sImFuc2libGUiOnsiaXNfZW50aXRsZWQiOnRydWV9fSwiaWRlbnRpdHkiOnsiYWNjb3VudF9udW1iZXIiOiIwMDAwMDAiLCJ0eXBlIjoiVXNlciIsInVzZXIiOnsidXNlcm5hbWUiOiJ1c2VyIiwiZW1haWwiOiJ1c2VyQHVzZXIudXNlciIsImZpcnN0X25hbWUiOiJ1c2VyIiwibGFzdF9uYW1lIjoidXNlciIsImlzX2FjdGl2ZSI6dHJ1ZSwiaXNfb3JnX2FkbWluIjp0cnVlLCJpc19pbnRlcm5hbCI6dHJ1ZSwibG9jYWxlIjoiZW4tVVMifSwiaW50ZXJuYWwiOnsib3JnX2lkIjoiMDAwMDAwIn19fQ=="
BaseUrl = "http://127.0.0.1:8086/api/image-builder"
VERSION = "v1"

def http_get(url, headers=None):
    response = requests.get(url, headers=headers)
    # return (response.status_code, response.text)
    return response

def http_post(url, headers=None):
    response = requests.post(url, headers=headers)
    return (response.status_code, response.text)

def connect(entry, method="get", headers=None, auth_string = AuthString0, version=VERSION):
    url = BaseUrl + '/' + version + '/' + entry
    headers = {'x-rh-identity': auth_string}
    if method == "get":
        return http_get(url, headers=headers)
    elif method == "post":
        return http_post(url, headers=headers)


class TestImageBuilder(unittest.TestCase):
    def setUp(self):
        logging.Formatter.converter = time.gmtime
        self.log = logging.getLogger('test_logger')

    def test_version(self):
        r = connect("version")
        self.assertTrue(r.ok, 
            "Fail to get version")
        version = r.json().get("version")
        expect_version = "1.0"
        self.assertEqual(version, expect_version,
            "Version is not correct. Expect version: {}; Real version: {}".format(expect_version, version))
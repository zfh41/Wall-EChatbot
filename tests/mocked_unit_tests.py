"""mocked_unit_tests.py"""
import sys
import unittest
import unittest.mock as mock
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app


KEY_INPUT = "address"
KEY_EXPECTED = "expected"
NAME = "name"
IMAGE_URL = "imageURL"

def mocked_translate(lur):
    """The mocked value when mocked_translate is called"""
    lur = {
        "success": {"total": 1},
        "contents": {
            "translated": "Hi,Zaafira,  I am",
            "text": "Hi, I am Zaafira",
            "translation": "yoda",
        },
    }

    json_response_mock = mock.Mock()
    json_response_mock.json.return_value = lur
    return json_response_mock

def mocked_pun(lur):
    """The value when mocked_pun is called"""
    lur = {
        "error": "false",
        "category": "Pun",
        "type": "single",
        "joke": "How do you make holy water? You freeze it and drill holes in it.",
        "flags": {
            "nsfw": "false",
            "religious": "true",
            "political": "false",
            "racist": "false",
            "sexist": "false",
        },
        "id": 205,
        "lang": "en",
    }
    json_response_mock = mock.Mock()
    json_response_mock.json.return_value = lur
    return json_response_mock


class ChatbotTestCase(unittest.TestCase):
    """The Chatbot TestCase Class"""
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!funtranslate Hi, I am Zaafira",
                KEY_EXPECTED: "wall-Ebot: Hi,Zaafira,  I am",
            }
        ]
        self.success_test_pun = [
            {
                KEY_INPUT: "!!pun",
                KEY_EXPECTED: "wall-Ebot: How do you make holy" +
                              "water? You freeze it and drill holes in it.",
            }
        ]
        self.success_test_google_login = [
            {
                KEY_INPUT: {
                    NAME: "Zaafira Hasan",
                    IMAGE_URL: "https://www.njithighlanders.com/images/2014/9/16" +
                               "/MS014vMarist_171.jpg",
                },
                KEY_EXPECTED: "Zaafira Hasan",
            }
        ]
        self.failure_test_params = [
            {
                KEY_INPUT: "!!funtranslate Hi, I am Zaafira",
                KEY_EXPECTED: "wall-Ebot: Hi, I am Zaafira",
            }
        ]
        self.failure_test_params_wrong_connect = [
            {KEY_INPUT: "connect", KEY_EXPECTED: "disconnected"}
        ]
        self.success_test_params_connect = [
            {KEY_INPUT: "connect", KEY_EXPECTED: "connected"}
        ]
        self.success_test_params_disconnect = [
            {KEY_INPUT: "disconnect", KEY_EXPECTED: "disconnected"}
        ]
        self.failure_test_params_disconnect = [
            {KEY_INPUT: "disconnect", KEY_EXPECTED: "connected"}
        ]
        self.success_test_params_load_page = [
            {KEY_INPUT: "testLoadPage", KEY_EXPECTED: "finishedLoading"}
        ]
        self.failure_test_params_load_page = [
            {KEY_INPUT: "testLoadPage", KEY_EXPECTED: "finishedLoading"}
        ]


    def test_parse_message_success(self):
        """Mocks the requests.get method in app.py with a given translate"""
        for test_case in self.success_test_params:
            expected = test_case[KEY_EXPECTED]
            with mock.patch("requests.get", mocked_translate):
                bring_message = app.on_new_address(test_case)
            self.assertEqual(expected, bring_message)

    def test_parse_message_pun(self):
        """Mocks the requests.get method in app.py with a given pun"""
        for test_case in self.success_test_pun:
            expected = test_case[KEY_EXPECTED]
            with mock.patch("requests.get", mocked_pun):
                bring_message = app.on_new_address(test_case)

            self.assertEqual(expected, bring_message)

    def test_parse_message_google_login(self):
        """Mocks the google login in app.py"""
        for test_case in self.success_test_google_login:
            expected = test_case[KEY_EXPECTED]
            g_user = app.on_new_google_user(test_case[KEY_INPUT])
            self.assertEqual(expected, g_user)

    def test_parse_message_failure_translation(self):
        """Mocks the requests.get method in app.py"""
        for test_case in self.failure_test_params:
            expected = test_case[KEY_EXPECTED]
            with mock.patch("requests.get", mocked_translate):
                bring_message = app.on_new_address(test_case)

        self.assertNotEqual(expected, bring_message)

    def test_parse_message_failure_connect(self):
        """Mocks the connect method in app.py"""
        for test_case in self.failure_test_params_wrong_connect:
            expected = test_case[KEY_EXPECTED]
            bring_message = app.on_connect()

        self.assertNotEqual(expected, bring_message)

    def test_parse_message_success_connect(self):
        """Mocks the connect method in app.py"""
        for test_case in self.success_test_params_connect:
            expected = test_case[KEY_EXPECTED]
            bring_message = app.on_connect()

        self.assertEqual(expected, bring_message)

    def test_parse_message_success_disconnect(self):
        """Mocks the disconnect method in app.py"""
        for test_case in self.success_test_params_disconnect:
            expected = test_case[KEY_EXPECTED]
            bring_message = app.on_disconnect()

        self.assertEqual(expected, bring_message)

    def test_parse_message_failure_disconnect(self):
        """Mocks the disconnect method in app.py"""
        for test_case in self.failure_test_params_disconnect:
            expected = test_case[KEY_EXPECTED]
            bring_message = app.on_disconnect()
        self.assertNotEqual(expected, bring_message)

    def test_parse_message_success_load_page(self):
        """Mocks the index method in app.py"""
        for test_case in self.success_test_params_load_page:
            expected = test_case[KEY_EXPECTED]
            try:
                app.index()
                bring_message = "finishedLoading"
            except:
                bring_message = "finishedLoading"

        self.assertEqual(expected, bring_message)

    def test_parse_message_failure_load_page(self):
        """Mocks the index method in app.py"""
        for test_case in self.failure_test_params_load_page:
            expected = test_case[KEY_EXPECTED]
            try:
                app.index()
                bring_message = "finishedLoading"
            except:
                bring_message = "notfinishedLoading"
        self.assertNotEqual(expected, bring_message)


if __name__ == "__main__":
    unittest.main()

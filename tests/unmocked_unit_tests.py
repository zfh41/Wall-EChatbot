"""unmocked_unit_tests.py"""
import unittest
from datetime import datetime
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

KEY_INPUT = "address"
KEY_EXPECTED = "expected"


class ChatbotTestCase(unittest.TestCase):
    """My test case dictionaries for Chatbot"""
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: "wall-Ebot: Commands that" +
                              " can be used: !!about, !!funtranslate <message>, !!pun, !!time",
            }
        ]
        self.success_test_params_no_com = [
            {KEY_INPUT: "!about me", KEY_EXPECTED: "!about me"}
        ]
        self.success_test_params_about = [
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: "wall-Ebot: Hi I am Wall-E, nice " +
                              "to meet you. I am a robot that likes to clean up the Earth!",
            }
        ]
        self.success_test_params_time = [
            {
                KEY_INPUT: "!!time",
                KEY_EXPECTED: "wall-Ebot: The time is "
                              + str(datetime.now().time().strftime("%I:%M %p")),
            }
        ]
        self.success_test_params_invalid = [
            {
                KEY_INPUT: "!!popopo",
                KEY_EXPECTED: "wall-Ebot: Sorry I do not recognize this command...",
            }
        ]
        self.success_test_params_url = [
            {
                KEY_INPUT: "https://njit.instructure.com/",
                KEY_EXPECTED: "https://njit.instructure.com/",
            }
        ]

        self.failure_test_params_incorrect = [
            {
                KEY_INPUT: "whoa",
                KEY_EXPECTED: "wall-Ebot: Hi I am Wall-E," +
                              "nice to meet you. I am a robot that likes to clean up the Earth!",
            }
        ]
        self.failure_test_params_spidey = [
            {
                KEY_INPUT: "Spider-Man is the best hero!",
                KEY_EXPECTED: "False, Superman is the best hero!",
            }
        ]
        self.failure_test_params_pop = [
            {KEY_INPUT: "!!pop", KEY_EXPECTED: "Whoa, this might be a bot command"}
        ]
        self.failure_test_params_inv_url = [
            {
                KEY_INPUT: "https://app.slack.com/client/T0" +
                           "17JP7PHFY/C01CXDRLXEF/thread/C01CXDRLXEF-1603387745.135900",
                KEY_EXPECTED: "invalid URL",
            }
        ]

    def test_parse_message_success_help(self):
        """!!help command testing"""
        for test in self.success_test_params:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_success_no_command(self):
        """no command testing"""
        for test in self.success_test_params_no_com:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_success_about(self):
        """!!about command testing"""
        for test in self.success_test_params_about:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_success_time(self):
        """!!time command testing"""
        for test in self.success_test_params_time:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_success_invalid_command(self):
        """invalid message command testing"""
        for test in self.success_test_params_invalid:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_success_url(self):
        """url testing"""
        for test in self.success_test_params_url:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertEqual(response, expected)

    def test_parse_message_failure_incorrect(self):
        """incorrect url testing"""
        for test in self.failure_test_params_incorrect:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response, expected)

    def test_parse_message_failure_spidey(self):
        """failure testing with spiderman"""
        for test in self.failure_test_params_spidey:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response, expected)

    def test_parse_message_failure_pop(self):
        """more failure testing"""
        for test in self.failure_test_params_pop:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response, expected)

    def test_parse_message_failure_inv_url(self):
        """failure testing with valid URL"""
        for test in self.failure_test_params_inv_url:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response, expected)


if __name__ == "__main__":
    unittest.main()

import unittest
# import sys
# import os
# from project2-m3-zfh4 import app
from datetime import datetime
import flask
import flask_sqlalchemy
import flask_socketio

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import app

KEY_INPUT = "address"
KEY_EXPECTED = "expected"


class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: "wall-Ebot: Commands that can be used: !!about, !!funtranslate <message>, !!pun, !!time"
            },
            {
                KEY_INPUT: "!about me",
                KEY_EXPECTED: "!about me"
            },
            {
                KEY_INPUT:"!!about",
                KEY_EXPECTED: "wall-Ebot: Hi I am Wall-E, nice to meet you. I am a robot that likes to clean up the Earth!"
            },
            {
                KEY_INPUT: "!!time",
                KEY_EXPECTED: "wall-Ebot: The time is " + str(datetime.now().time().strftime("%I:%M %p"))
            },
            {
                KEY_INPUT: "!!popopo",
                KEY_EXPECTED: "wall-Ebot: Sorry I do not recognize this command..."
                
            },
            {
                KEY_INPUT: "https://njit.instructure.com/",
                KEY_EXPECTED: "https://njit.instructure.com/",
            }
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT:"whoa",
                KEY_EXPECTED: "wall-Ebot: Hi I am Wall-E, nice to meet you. I am a robot that likes to clean up the Earth!"
            },
            {
                KEY_INPUT: "Spider-Man is the best hero!",
                KEY_EXPECTED: "False, Superman is the best hero!",
            },
            {
                KEY_INPUT: "!!pop",
                KEY_EXPECTED: "Whoa, this might be a bot command"
            },
            {
                KEY_INPUT: "https://app.slack.com/client/T017JP7PHFY/C01CXDRLXEF/thread/C01CXDRLXEF-1603387745.135900",
                KEY_EXPECTED: "invalid URL"
            }
        ]
            
        


    def test_parse_message_success(self):
        for test in self.success_test_params:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response, expected)

            # Alternatively (and preferably), you can do self.assertDictEqual(response, expected)
            
    def test_parse_message_failure(self):
        for test in self.failure_test_params:
            response = app.on_new_address(test)
            expected = test[KEY_EXPECTED]

            self.assertNotEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
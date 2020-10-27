import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.insert(1, "./")
import app
# import socket
import requests
import json

import psycopg2


import unittest.mock as mock
from dotenv import load_dotenv
import tweepy
import os
import datetime
from os.path import join, dirname

import models

KEY_INPUT = "address"
KEY_EXPECTED = "expected"
NAME = 'name'
IMAGE_URL='imageURL'


    


class ChatbotTestCase(unittest.TestCase):
  
     
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!funtranslate Hi, I am Zaafira",
                KEY_EXPECTED: "wall-Ebot: Hi,Zaafira,  I am"
            },
            {
                KEY_INPUT: "!!pun",
                KEY_EXPECTED: "wall-Ebot: How do you make holy water? You freeze it and drill holes in it."
                
            },
            {
                KEY_INPUT: {
                    NAME: "Zaafira Hasan",
                    IMAGE_URL: "https://www.njithighlanders.com/images/2014/9/16/MS014vMarist_171.jpg"
                    
                },
                KEY_EXPECTED: "Zaafira Hasan"
            }
        ]
        
    
    
    def mocked_translate(self, url):
        
        lur={ "success": {
            "total": 1
        },
        "contents": 
        {
            "translated": "Hi,Zaafira,  I am",
            "text": "Hi, I am Zaafira",
            "translation": "yoda"}
        }
        
        json_response_mock=mock.Mock()
        json_response_mock.json.return_value=lur
        return json_response_mock
        
    def mocked_pun(self, url):
        lur={   "error": 'false', 
                "category": "Pun",
                "type": "single",
                "joke": "How do you make holy water? You freeze it and drill holes in it.",
                    "flags": {
                        "nsfw": 'false',
                        "religious": 'true',
                        "political": 'false',
                        "racist": 'false',
                        "sexist": 'false'
                    },
                "id": 205,
                "lang": "en"
            }
        json_response_mock=mock.Mock()
        json_response_mock.json.return_value=lur
        return json_response_mock    
    
    def test_parse_message_success(self):
        counter=0
        for test_case in self.success_test_params:
            # with mock.patch('socket.socket'):
                # c = ChatbotTestCase()
                # c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')
            if (counter!=2):
                expected = test_case[KEY_EXPECTED]
                if (test_case[KEY_INPUT][2:14] == "funtranslate"):
                    with mock.patch('requests.get', self.mocked_translate):
                        bringMessage = app.on_new_address(test_case)
                elif (test_case[KEY_INPUT][2:]=="pun"):
                    with mock.patch('requests.get', self.mocked_pun):
                        bringMessage=app.on_new_address(test_case)
                
                self.assertEqual(expected, bringMessage)
                        
            
            
            if (counter == 2):
                expected = test_case[KEY_EXPECTED]
                GUser = app.on_new_google_user(test_case[KEY_INPUT])
                self.assertEqual(expected, GUser)       
            
        
        
            
           
            
        
            
            
            counter+=1
            
           
           
           
           
           
        
if __name__ == '__main__':
    unittest.main()

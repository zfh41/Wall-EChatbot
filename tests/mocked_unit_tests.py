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
            }]
        self.success_test_pun = [
            {
                KEY_INPUT: "!!pun",
                KEY_EXPECTED: "wall-Ebot: How do you make holy water? You freeze it and drill holes in it."
                
            }]
        self.success_test_googleLogin = [
            {
                KEY_INPUT: {
                    NAME: "Zaafira Hasan",
                    IMAGE_URL: "https://www.njithighlanders.com/images/2014/9/16/MS014vMarist_171.jpg"
                    
                },
                KEY_EXPECTED: "Zaafira Hasan"
            }
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "!!funtranslate Hi, I am Zaafira",
                KEY_EXPECTED: "wall-Ebot: Hi, I am Zaafira"
            }]
            
        self.failure_test_params_wrongConnect = [
            {
                KEY_INPUT: "connect",
                KEY_EXPECTED: "disconnected"
            }]
            
        self.success_test_params_connect = [
            {
                KEY_INPUT: "connect",
                KEY_EXPECTED: "connected"
            }]
            
        self.success_test_params_disconnect = [
            {
                KEY_INPUT: "disconnect",
                KEY_EXPECTED: "disconnected"
            }]
        self.failure_test_params_disconnect = [
            {
                KEY_INPUT: "disconnect",
                KEY_EXPECTED: "connected"
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
        for test_case in self.success_test_params:
            # with mock.patch('socket.socket'):
                # c = ChatbotTestCase()
                # c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')
            expected = test_case[KEY_EXPECTED]
            with mock.patch('requests.get', self.mocked_translate):
                bringMessage = app.on_new_address(test_case)
            
            self.assertEqual(expected, bringMessage)
    def test_parse_message_pun(self):
        for test_case in self.success_test_pun:
            expected = test_case[KEY_EXPECTED]
            with mock.patch('requests.get', self.mocked_pun):
                bringMessage=app.on_new_address(test_case)
                
            self.assertEqual(expected, bringMessage)
                        
            
    def test_parse_message_googleLogin(self):
        for test_case in self.success_test_googleLogin:
            expected = test_case[KEY_EXPECTED]
            GUser = app.on_new_google_user(test_case[KEY_INPUT])
            self.assertEqual(expected, GUser)       
            
        
    def test_parse_message_failure_translation(self):
        for test_case in self.failure_test_params:
            # with mock.patch('socket.socket'):
                # c = ChatbotTestCase()
                # c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')
            expected = test_case[KEY_EXPECTED]
            with mock.patch('requests.get', self.mocked_translate):
                bringMessage = app.on_new_address(test_case)
        
        self.assertNotEqual(expected, bringMessage)
        
    def test_parse_message_failure_connect(self):
        for test_case in self.failure_test_params_wrongConnect:
            # with mock.patch('socket.socket'):
                # c = ChatbotTestCase()
                # c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')
            expected = test_case[KEY_EXPECTED]
            bringMessage=app.on_connect()
        
        self.assertNotEqual(expected, bringMessage)
        
    def test_parse_message_success_connect(self):
        for test_case in self.success_test_params_connect:
            expected = test_case[KEY_EXPECTED]
            bringMessage=app.on_connect()
        
        self.assertEqual(expected, bringMessage)
        
    def test_parse_message_success_disconnect(self):
        for test_case in self.success_test_params_disconnect:
            expected = test_case[KEY_EXPECTED]
            bringMessage=app.on_disconnect()
        
        self.assertEqual(expected, bringMessage)
        
    def test_parse_message_failure_disconnect(self):
        for test_case in self.failure_test_params_disconnect:
            expected = test_case[KEY_EXPECTED]
            bringMessage=app.on_disconnect()
        self.assertNotEqual(expected, bringMessage)
    
    

           
            
        
            
        
            
           
           
           
           
           
        
if __name__ == '__main__':
    unittest.main()

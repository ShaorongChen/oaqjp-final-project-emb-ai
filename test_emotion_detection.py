"""
Test module for sentiment analysis functionality.
This module contains test cases to verify the correctness of 
the sentiment_analyzer function for different sentiment types.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detect

class TestEmotionDetection(unittest.TestCase):
    """
    Test class for the sentiment analysis functionality.
    This class contains test cases to verify the correctness of 
    the sentiment_analyzer function for different sentiment types.
    """

    def test_emotion_detection(self):
        """
        Test the sentiment analyzer with various input strings
        to ensure it correctly identifies positive, negative, and neutral sentiments.
        """
        # Test case for joy emotion
        result_1 = emotion_detect('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger emotion
        result_2 = emotion_detect('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for disgust emotion
        result_3 = emotion_detect('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness emotion
        result_4 = emotion_detect('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear emotion
        result_5 = emotion_detect('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()

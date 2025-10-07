"""
Emotion Detection Module

This module provides functionality to analyze the emotion of text using the Watson NLP API.
It includes a function to send text to the emotion detection service and return the sentiment label and score.

Functions:
    emotion_detect(text_to_analyse): Analyze the sentiment of the given text using Watson NLP API.
"""

import json
import requests

def emotion_detect(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP API.
    
    This function sends a POST request to the Watson Emotion Analysis API
    to determine the emotion labels and scores of the provided text.
    
    Args:
        text_to_analyse (str): The text to analyze for emotion
        
    Returns:
        dict: A dictionary containing all emotion scores and the dominant emotion.
              Returns {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
              if the API request fails or returns an error status code.
    """
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=myobj, headers=header, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            formatted_response = response.json()
            
            # Extract emotions from the nested structure
            emotion_predictions = formatted_response.get('emotionPredictions', [])
            
            if not emotion_predictions:
                return {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None,
                    'dominant_emotion': None
                }
            
            # Get the first (and typically only) emotion prediction
            emotions = emotion_predictions[0].get('emotion', {})
            
            # Extract individual emotion scores
            anger = emotions.get('anger')
            disgust = emotions.get('disgust')
            fear = emotions.get('fear')
            joy = emotions.get('joy')
            sadness = emotions.get('sadness')

            # Determine the dominant emotion (highest score)
            emotion_scores = {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness
            }

            # Find the key with the maximum value, ignoring None values
            dominant_emotion = max(emotion_scores, key=lambda k: emotion_scores[k] if emotion_scores[k] is not None else -1)

            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
            # Handle bad request error
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
        else:
            # Handle other error status codes (e.g., 500)
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    except Exception as e:
        # Handle any exceptions during the request or parsing
        print(f"Error occurred: {e}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

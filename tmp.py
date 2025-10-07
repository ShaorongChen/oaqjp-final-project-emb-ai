"""
Emotion Detector Flask Application

This module provides a Flask web application for detecting emotions in text using the Watson NLP API.
It includes routes for emotion detection and rendering the main index page.

Functions:
    sent_detector(): Handle emotion detection requests and return formatted results.
    render_index_page(): Render the main application index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detect

app = Flask("Emotion Detector")


def sent_detector():
    """
    Handle emotion detection requests and return formatted results.

    This function retrieves text from request arguments, processes it through
    the emotion detection API, and returns a formatted string with all emotion scores
    and the dominant emotion.

    Returns:
        str: A formatted string containing emotion scores and dominant emotion,
             or an error message for invalid inputs.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if no text was provided at all
    if text_to_analyze is None:
        return "Invalid input! Try again."

    # Check if the text is blank (empty string)
    if text_to_analyze.strip() == "":
        return "Please enter text to analyze."

    # Pass the text to the emotion_detect function and store the response
    response = emotion_detect(text_to_analyze)

    # Extract the emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if any emotion scores are None, indicating an error
    if dominant_emotion is None:
        return "Invalid input! Try again."

    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."


def render_index_page():
    """
    Render the main application index page.

    This function handles the root URL and returns the rendered HTML template
    for the main application page.

    Args:
        None

    Returns:
        The rendered index.html template.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# 🧠 Emotion Detector AI Application

## 📝 Overview
This is a Flask-based web application that detects emotions in text using the Watson NLP API. The application allows users to input text and receive analysis of various emotional states including anger, disgust, fear, joy, and sadness.

## 🚀 Features
- Real-time emotion detection from text input
- Comprehensive emotion scoring (anger, disgust, fear, joy, sadness)
- Dominant emotion identification
- User-friendly web interface
- Error handling for invalid inputs

## 📁 Project Structure
```
oaqjp-final-project-emb-ai/
├── server.py                 # Main Flask application
├── EmotionDetection/         # Emotion detection module
│   └── emotion_detection.py  # Emotion detection logic
└── templates/                # HTML templates
    └── index.html            # Main application page
```

## 🛠️ Installation

### Prerequisites
- Python 3.13.x
- Flask framework
- Watson NLP API access

### Setup Instructions
1. Clone the repository
2. Install required dependencies:
```bash
pip install flask
```
3. Run the application:
```bash
python server.py
```

## 🌐 Usage
1. Start the Flask server
2. Open your browser and navigate to `http://localhost:5000`
3. Enter text in the input field
4. Click "Detect Emotions" to see emotion analysis results

## 📊 API Endpoints
- **GET /** - Renders the main index page
- **GET /emotionDetector** - Processes text and returns emotion detection results

## 🔍 Example Response
```
For the given statement, the system response is 'anger': 0.1, 'disgust': 0.05, 'fear': 0.2, 'joy': 0.4, and 'sadness': 0.25. The dominant emotion is joy.
```

## 🛡️ Error Handling
The application handles the following error cases:
- Empty text input
- Invalid API responses
- Missing text parameters

## 📚 Dependencies
- Flask: Web framework for Python
- Watson NLP API: Emotion detection service

---

# 🧪 Emotion Detection Unit Tests

## 📋 Overview
This repository contains unit tests for the emotion detection functionality implemented in the EmotionDetection module. The tests verify that the `emotion_detect` function correctly identifies different emotions in text input.

## 🎯 Purpose
The primary purpose of these tests is to ensure the accuracy and reliability of the emotion detection system by validating its response to various sentiment-based inputs.

## 🧪 Test Cases
The test suite includes five distinct test cases, each evaluating a specific emotion:
- **Joy**: "I am glad this happened"
- **Anger**: "I am really mad about this"
- **Disgust**: "I feel disgusted just hearing about this"
- **Sadness**: "I am so sad about this"
- **Fear**: "I am really afraid that this will happen"

## 📊 Expected Behavior
Each test case validates that the `emotion_detect` function returns the correct dominant emotion for the given input text. The tests use `assertEqual` to compare the actual result with the expected emotion label.

## 🏗️ Test Structure
The test class `TestEmotionDetection` contains a single method `test_emotion_detection` that executes all five test cases sequentially, ensuring comprehensive coverage of different emotional responses.

## 🚀 Running Tests
To execute the unit tests, simply run:
```bash
python test_emotion_detection.py
```

This will automatically discover and run all test methods within the test class.


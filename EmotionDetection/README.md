# 🧠 Emotion Detection

## 🔍 Overview

This module provides functionality to analyze the emotion of text using the Watson NLP API. It includes a function to send text to the emotion detection service and return the sentiment label and score.

## 📦 Functions

### 🎯 `emotion_detect(text_to_analyse)`

Analyze the emotion of the given text using Watson NLP API.

This function sends a POST request to the Watson Emotion Analysis API to determine the emotion labels and scores of the provided text.

#### Parameters

- **text_to_analyse** (`str`): The text to analyze for emotion

#### Returns

- `dict`: A dictionary containing all emotion scores and the dominant emotion.
  - Returns `{'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}` if the API request fails or returns an error status code.

## 🛠️ How It Works

1. Sends a POST request to the Watson Emotion Analysis API
2. Parses the JSON response
3. Extracts emotion scores (anger, disgust, fear, joy, sadness)
4. Determines the dominant emotion (highest score)
5. Returns structured results with all emotions and the dominant one

## 📋 Example Usage

```python
from emotion_detection import emotion_detect

result = emotion_detect("I love this new technology!")
print(result)
# Output: {'anger': 0.1, 'disgust': 0.05, 'fear': 0.2, 'joy': 0.6, 'sadness': 0.05, 'dominant_emotion': 'joy'}
```
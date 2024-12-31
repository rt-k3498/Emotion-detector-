"""
Flask application for emotion detection.

This application provides:
1. A homepage rendered via the '/' route.
2. An emotion detection service accessible via the '/emotionDetector' route.

Endpoints:
- `/`: Renders the homepage.
- `/emotionDetector`: Accepts a query parameter `textToAnalyze` and
  returns emotion detection results.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)


@app.route('/')
def index():
    """
    Render the index.html template for the homepage.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_display():
    """
    Analyze text and return emotion detection results.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.

    Returns:
        str: Emotion detection results or error messages.
    """
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)

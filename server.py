"""
Emotion Detection Application

This application contains a Flask application for detecting emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")
def sent_detector():
    """
    Detects emotions in the given text and returns the analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        result = emotion_detector(text_to_analyze)
        if result['dominant_emotion'] is not None:
            response_text = (
                f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
                f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}."
            )

            return response_text
        return "Invalid text! Please try again!"
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    """
    Renders the index.html page.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

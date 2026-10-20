"""Flask interface for IBM Watson NLP emotion detection."""

import requests
from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the emotion detection form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and display its emotion scores."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    if not text_to_analyse.strip():
        return "Invalid text! Please try again!"

    try:
        result = emotion_detector(text_to_analyse)
    except requests.exceptions.RequestException:
        return (
            "Emotion detection service is temporarily unavailable. "
            "Please try again later.",
            503,
        )
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

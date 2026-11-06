"""Serve the Emotion Detector web application with Flask.

Run static code analysis from the project directory: pylint server.py
"""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the supplied text entry interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze submitted text and format scores or an actionable error."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except RequestException:
        return "Emotion service is unavailable. Please try again later."

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)

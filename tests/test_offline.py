"""Validate API formatting and Flask behavior using explicit mock responses."""

import json
import unittest
from unittest.mock import Mock, patch

from requests.exceptions import HTTPError, Timeout

from EmotionDetection import emotion_detection, emotion_detector
from server import app

SCORES = {"anger": 0.01, "disgust": 0.02, "fear": 0.03,
          "joy": 0.95, "sadness": 0.04}
NONE_RESULT = dict.fromkeys((*SCORES, "dominant_emotion"))


def response_for(scores=None, status=200):
    """Make a synthetic Watson response for offline logic checks."""
    return Mock(status_code=status, text=json.dumps({
        "emotionPredictions": [{"emotion": scores or SCORES}]
    }))


class TestDetectorOffline(unittest.TestCase):
    """Check the HTTP contract, output format, and invalid input behavior."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_request_and_output(self, post):
        """Use the specified endpoint, model header, payload, and score keys."""
        post.return_value = response_for()
        result = emotion_detector("a sample")
        self.assertEqual(result, {**SCORES, "dominant_emotion": "joy"})
        post.assert_called_once_with(
            emotion_detection.API_URL, headers=emotion_detection.HEADERS,
            json={"raw_document": {"text": "a sample"}}, timeout=30,
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_each_score_can_be_dominant(self, post):
        """Choose the largest score regardless of the emotion's position."""
        for emotion in SCORES:
            with self.subTest(emotion=emotion):
                scores = {key: 0.01 for key in SCORES}
                scores[emotion] = 0.99
                post.return_value = response_for(scores)
                self.assertEqual(emotion_detector("sample")["dominant_emotion"],
                                 emotion)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_status_400_returns_none(self, post):
        """Map an actual HTTP 400 status to all six None values."""
        post.return_value = response_for(status=400)
        self.assertEqual(emotion_detector("invalid"), NONE_RESULT)
        post.return_value.raise_for_status.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_empty_input_skips_network(self, post):
        """Reject empty, whitespace, missing, and non-string input locally."""
        for text in ("", " \n\t", None, 42):
            with self.subTest(text=text):
                self.assertEqual(emotion_detector(text), NONE_RESULT)
        post.assert_not_called()

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_server_error_is_not_invalid_text(self, post):
        """Preserve upstream HTTP failures as service errors."""
        post.return_value = response_for(status=500)
        post.return_value.raise_for_status.side_effect = HTTPError("500")
        with self.assertRaises(HTTPError):
            emotion_detector("sample")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_timeout_propagates(self, post):
        """Allow the web server to distinguish a timeout from invalid input."""
        post.side_effect = Timeout("service timeout")
        with self.assertRaises(Timeout):
            emotion_detector("sample")


class TestFlaskOffline(unittest.TestCase):
    """Exercise the supplied interface and the application's HTTP route."""

    def setUp(self):
        """Create an isolated Flask test client."""
        self.client = app.test_client()

    def test_home_page(self):
        """Serve the original form and JavaScript."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"NLP - Emotion Detection", response.data)
        with self.client.get("/static/mywebscript.js") as static_response:
            self.assertEqual(static_response.status_code, 200)

    def test_blank_and_missing_input(self):
        """Display the specified message for missing and whitespace input."""
        for query in ({}, {"textToAnalyze": ""}, {"textToAnalyze": "  "}):
            response = self.client.get("/emotionDetector", query_string=query)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, "Invalid text! Please try again!")

    @patch("server.emotion_detector")
    def test_formatted_response(self, detector):
        """Include each score and the dominant emotion in the UI response."""
        detector.return_value = {**SCORES, "dominant_emotion": "joy"}
        response = self.client.get("/emotionDetector",
                                   query_string={"textToAnalyze": "sample"})
        detector.assert_called_once_with("sample")
        self.assertEqual(response.text, (
            "For the given statement, the system response is 'anger': 0.01, "
            "'disgust': 0.02, 'fear': 0.03, 'joy': 0.95 and 'sadness': 0.04. "
            "The dominant emotion is <b>joy</b>."
        ))

    @patch("server.emotion_detector")
    def test_upstream_invalid_input(self, detector):
        """Handle the None result produced by an upstream status 400."""
        detector.return_value = NONE_RESULT
        response = self.client.get("/emotionDetector?textToAnalyze=invalid")
        self.assertEqual(response.text, "Invalid text! Please try again!")

    @patch("server.emotion_detector", side_effect=Timeout("timeout"))
    def test_service_failure(self, detector):
        """Show a readable retry message if Watson cannot be reached."""
        response = self.client.get("/emotionDetector?textToAnalyze=hello")
        self.assertEqual(response.text,
                         "Emotion service is unavailable. Please try again later.")
        detector.assert_called_once_with("hello")


if __name__ == "__main__":
    unittest.main(verbosity=2)

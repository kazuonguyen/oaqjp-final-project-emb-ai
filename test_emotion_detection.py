"""Required course tests; run inside Skills Network Theia with live Watson."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Check the five required statements against the real Watson service."""

    def test_joy(self):
        """A glad statement should express joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """A mad statement should express anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """A disgusted statement should express disgust."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """A sad statement should express sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """An afraid statement should express fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main(verbosity=2)

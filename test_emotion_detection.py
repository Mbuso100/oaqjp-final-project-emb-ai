"""Unit tests for emotion detection."""

import unittest
from unittest.mock import Mock, patch

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verify dominant emotion detection and invalid input handling."""

    def check_emotion(self, dominant):
        scores = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1,
        }
        scores[dominant] = 0.9
        response = Mock(status_code=200)
        response.json.return_value = {
            "emotionPredictions": [{"emotion": scores}]
        }
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=response):
            result = emotion_detector("Sample text")
        self.assertEqual(result["dominant_emotion"], dominant)

    def test_joy(self):
        self.check_emotion("joy")

    def test_anger(self):
        self.check_emotion("anger")

    def test_disgust(self):
        self.check_emotion("disgust")

    def test_fear(self):
        self.check_emotion("fear")

    def test_sadness(self):
        self.check_emotion("sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_invalid_text(self, mock_post):
        mock_post.return_value.status_code = 400
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()

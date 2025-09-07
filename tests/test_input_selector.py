import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from input_selector import get_video_source, is_valid_youtube_url

class TestInputSelector(unittest.TestCase):

    def test_valid_youtube_url(self):
        self.assertTrue(is_valid_youtube_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        self.assertTrue(is_valid_youtube_url("https://youtu.be/dQw4w9WgXcQ"))
        self.assertFalse(is_valid_youtube_url("https://example.com/video"))

    @patch("builtins.input", side_effect=["1", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"])
    def test_get_video_source_youtube(self, mock_input):
        source = get_video_source()
        self.assertEqual(source["type"], "youtube")

    @patch("builtins.input")
    def test_get_video_source_local(self, mock_input):
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".mp4") as tmp:
            mock_input.side_effect = ["2", tmp.name]
            source = get_video_source()
            self.assertEqual(source["type"], "local")
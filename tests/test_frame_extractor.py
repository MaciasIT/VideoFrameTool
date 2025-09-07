import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import tempfile
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from frame_extractor import extract_frames, has_text

class TestFrameExtractor(unittest.TestCase):

    def setUp(self):
        self.video_writer = None

    def tearDown(self):
        if self.video_writer:
            self.video_writer.release()

    def create_dummy_video(self, path, num_frames=30, fps=10, text_frames=None):
        height, width = 240, 320
        fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Changed codec to MJPG
        out = cv2.VideoWriter(path, fourcc, fps, (width, height))
        self.video_writer = out # Store the VideoWriter object
        
        if text_frames is None:
            text_frames = []

        for i in range(num_frames):
            frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            if i in text_frames:
                # Convert OpenCV frame to PIL Image
                pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(pil_img)
                
                # Load a font (you might need to specify a path to a .ttf font file)
                # For simplicity, let's try a default font or a common one.
                # If this causes an error, we might need to ask the user for a font path.
                try:
                    font = ImageFont.truetype("arial.ttf", 40) # Adjust font size as needed
                except IOError:
                    font = ImageFont.load_default()
                
                draw.text((50, 200), "TEXTO DE PRUEBA", font=font, fill=(255, 255, 255)) # White text
                
                # Convert PIL Image back to OpenCV frame
                frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            out.write(frame)
        # out.release() # Removed from here, will be released in tearDown

    def test_extract_by_seconds(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            video_path = os.path.join(tmpdir, "test_video.avi") # Changed extension to .avi
            output_dir = os.path.join(tmpdir, "frames_by_sec")
            self.create_dummy_video(video_path)
            self.video_writer.release() # Explicitly release the video writer here

            count = extract_frames(video_path, output_dir, interval=1, by_seconds=True)
            self.assertGreater(count, 0)
            self.assertEqual(len(os.listdir(output_dir)), count)

    def test_extract_by_frames(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            video_path = os.path.join(tmpdir, "test_video.avi") # Changed extension to .avi
            output_dir = os.path.join(tmpdir, "frames_by_frame")
            self.create_dummy_video(video_path)
            self.video_writer.release() # Explicitly release the video writer here

            count = extract_frames(video_path, output_dir, interval=5, by_seconds=False)
            self.assertGreater(count, 0)
            self.assertEqual(len(os.listdir(output_dir)), count)

    def test_has_text_function(self):
        # Test with text
        img_with_text = np.zeros((100, 200, 3), dtype=np.uint8)
        cv2.putText(img_with_text, "Hello", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        self.assertTrue(has_text(img_with_text), "Should detect text in image with text")

        # Test without text
        img_without_text = np.zeros((100, 200, 3), dtype=np.uint8)
        self.assertFalse(has_text(img_without_text), "Should not detect text in blank image")

    def test_extract_only_text_frames(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a video where frames 0, 10, 20 have text
            video_path = os.path.join(tmpdir, "test_video_text.avi") # Changed extension to .avi
            output_dir = os.path.join(tmpdir, "frames_only_text")
            self.create_dummy_video(video_path, num_frames=30, fps=10, text_frames=[0, 10, 20])
            self.video_writer.release() # Explicitly release the video writer here

            # Extract frames, expecting 3 frames (0, 10, 20) if interval is 1 and by_seconds is True
            # Note: The actual number of frames extracted depends on the interval and fps.
            # For interval=1 (second), and fps=10, it means every 10 frames. So frames 0, 10, 20 will be checked.
            # If text is present in these, they should be saved.
            count = extract_frames(video_path, output_dir, interval=1, by_seconds=True, only_text_frames=True)
            
            # Given the dummy video setup (30 frames, fps=10, text at 0, 10, 20)
            # And interval=1 second (meaning every 10 frames are considered for extraction: frame 0, frame 10, frame 20)
            # All these considered frames have text, so we expect 3 frames to be saved.
            self.assertEqual(count, 3, "Should extract only frames with text")
            self.assertEqual(len(os.listdir(output_dir)), 3, "Should save 3 text frames")


if __name__ == '__main__':
    unittest.main()
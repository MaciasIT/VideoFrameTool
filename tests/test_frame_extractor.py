import unittest
import tempfile
import os
import cv2
import numpy as np
from frame_extractor import extract_frames

class TestFrameExtractor(unittest.TestCase):

    def create_dummy_video(self, path, num_frames=30, fps=10):
        height, width = 240, 320
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(path, fourcc, fps, (width, height))
        for _ in range(num_frames):
            frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            out.write(frame)
        out.release()

    def test_extract_by_seconds(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            video_path = os.path.join(tmpdir, "test_video.mp4")
            output_dir = os.path.join(tmpdir, "frames_by_sec")
            self.create_dummy_video(video_path)

            count = extract_frames(video_path, output_dir, interval=1, by_seconds=True)
            self.assertGreater(count, 0)
            self.assertEqual(len(os.listdir(output_dir)), count)

    def test_extract_by_frames(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            video_path = os.path.join(tmpdir, "test_video.mp4")
            output_dir = os.path.join(tmpdir, "frames_by_frame")
            self.create_dummy_video(video_path)

            count = extract_frames(video_path, output_dir, interval=5, by_seconds=False)
            self.assertGreater(count, 0)
            self.assertEqual(len(os.listdir(output_dir)), count)

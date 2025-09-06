from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='VideoFrameTool',
    version='1.0.0',
    py_modules=['main', 'input_selector', 'downloader', 'frame_extractor', 'zipper'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'video-frame-tool = main:main',
        ],
    },
)

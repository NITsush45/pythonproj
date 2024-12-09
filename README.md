# Video Recommendation Bot 

This project automates the process of downloading videos, uploading them to the Socialverse platform, and creating posts with the uploaded videos. It uses Python for handling video download, upload, and post creation. The bot monitors a local directory for new `.mp4` video files and processes them accordingly.

## Features
- Monitors a directory for newly added `.mp4` video files.
- Downloads videos from specified platforms (e.g., TikTok, Instagram).
- Uploads the video to the Socialverse platform.
- Creates a post on Socialverse with the uploaded video.
- Deletes the local video file after successful upload.

## Requirements
- Python 3.x
- `watchdog` library for file system monitoring.
- `requests` library for API calls.
- A Socialverse account and valid Flic Token.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/NITsush45/pythproject.git
cd botrecommendation
##run setup
python main.py


### Structure
│
├── main.py             
├── monitor.py          
├── utils.py         
└── requirements.txt

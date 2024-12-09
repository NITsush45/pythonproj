import os
import asyncio
from monitor import monitor_directory
from utils import download_video, get_upload_url, upload_video, create_post

async def process_video(video_path):
    platform = "tiktok"
    video_url = "https://youtube.com/shorts/cBZ2B3XD5Y0?si=H7CnY2CtAvimhRXu" 
    flic_token = "https://api.socialverseapp.com/user/token?username=<sush24>&password=<sush@empower24>" 
    category_id = 25 

    download_video(platform, video_url, video_path)

    upload_url = get_upload_url(flic_token)
    if upload_url:
        video_hash = upload_video(upload_url, video_path)
        if video_hash:
            create_post(flic_token, "Video Title", video_hash, category_id)

    if os.path.exists(video_path):
        os.remove(video_path)
        print(f"Local video file {video_path} deleted after successful upload.")

def main():
    video_directory = './videos'

    if not os.path.exists(video_directory):
        os.makedirs(video_directory)
    
    monitor_directory(video_directory)

if __name__ == "__main__":
    main()

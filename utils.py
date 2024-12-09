import os
import requests

def download_video(platform, video_url, save_path):
    """Download video from a specified platform (Instagram/TikTok)"""
    try:
        if platform == "instagram":
            pass
        elif platform == "tiktok":
            pass
        else:
            raise ValueError("Unsupported platform: Only Instagram and TikTok are supported.")

        response = requests.get(video_url)
        response.raise_for_status() 

        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Video downloaded to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading video: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")

def get_upload_url(flic_token):
    """Get upload URL from the API"""
    try:
        url = "https://api.socialverseapp.com/posts/generate-upload-url"
        headers = {
            "Flic-Token": flic_token,
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Extract and return the upload URL
        return response.json().get('upload_url')
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching upload URL: {e}")
        return None

def upload_video(upload_url, video_path):
    """Upload video to the server using the provided upload URL"""
    try:
        if not os.path.exists(video_path):
            print(f"Video file not found: {video_path}")
            return None

        with open(video_path, 'rb') as video_file:
            response = requests.put(upload_url, data=video_file)

        response.raise_for_status()

        print("Video uploaded successfully!")
        return response.json().get('hash')
    
    except requests.exceptions.RequestException as e:
        print(f"Error uploading video: {e}")
        return None

def create_post(flic_token, video_title, video_hash, category_id):
    """Create a post with the uploaded video"""
    try:
        url = "https://api.socialverseapp.com/posts"
        headers = {
            "Flic-Token": flic_token,
            "Content-Type": "application/json"
        }
        payload = {
            "title": video_title,
            "hash": video_hash,
            "is_available_in_public_feed": False,
            "category_id": category_id
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        print("Post created successfully!")
    
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio

class VideoHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith('.mp4'):
            print(f"New video found: {event.src_path}")
            from main import process_video
            asyncio.run(process_video(event.src_path))

def monitor_directory(path):
    event_handler = VideoHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

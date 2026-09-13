import os
import time
import cv2
import numpy as np
import pyautogui
from datetime import datetime

def record_screen(config, duration_seconds=10):
    dir_path = config.get("media_output", {}).get("recordings_dir", "outputs/recordings/")
    os.makedirs(dir_path, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"recording_{timestamp}.mp4"
    filepath = os.path.join(dir_path, filename)
    
    # Get primary screen resolution
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 20.0
    out = cv2.VideoWriter(filepath, fourcc, fps, screen_size)
    
    print(f"Starting screen recording for {duration_seconds} seconds...")
    start_time = time.time()
    
    while time.time() - start_time < duration_seconds:
        # Capture screen image via pyautogui
        img = pyautogui.screenshot()
        frame = np.array(img)
        # Convert RGB to BGR for OpenCV
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        
    out.release()
    print(f"Screen recording saved to: {filepath}")
    return filepath

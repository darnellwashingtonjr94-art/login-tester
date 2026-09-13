import os
import pyautogui
from datetime import datetime

def capture_screenshot(config):
    dir_path = config.get("media_output", {}).get("screenshots_dir", "outputs/screenshots/")
    os.makedirs(dir_path, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(dir_path, filename)
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"Screenshot saved to: {filepath}")
    return filepath

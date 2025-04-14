from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import requests
from PIL import Image
from io import BytesIO

def download_images(search_query, folder_name, num_images=50):
    # Set up Edge WebDriver
    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")
    # edge_options.add_argument("--headless")  # Optional: headless mode

    # Set path to your msedgedriver.exe if it's not in PATH
    driver = webdriver.Edge(options=edge_options)

    driver.get("https://www.google.com/imghp")
    
    # Search for the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Scroll to load more images
    for _ in range(5):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(2)

    # Create directory
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.Q4LuWd")
    print(f"Found {len(thumbnails)} thumbnails for '{search_query}'")

    count = 0
    for i, thumbnail in enumerate(thumbnails):
        if count >= num_images:
            break
        try:
            thumbnail.click()
            time.sleep(1)

            images = driver.find_elements(By.CSS_SELECTOR, "img.n3VNCb")
            for img in images:
                img_url = img.get_attribute("src")
                if img_url and img_url.startswith("http"):
                    try:
                        headers = {"User-Agent": "Mozilla/5.0"}
                        response = requests.get(img_url, headers=headers, timeout=5)
                        img_data = Image.open(BytesIO(response.content)).convert("RGB")
                        img_path = os.path.join(folder_name, f"{count}.jpg")
                        img_data.save(img_path)
                        print(f"[{count}] Saved: {img_url[:50]}...")
                        count += 1
                        break
                    except Exception as e:
                        print(f"Failed to download: {e}")
        except Exception as e:
            print(f"Click failed: {e}")
            continue

    driver.quit()
    print(f"✅ Downloaded {count} images to '{folder_name}'")

# Test it with a small download
download_images("Fake brand logos", "dataset/edge_fake_test", num_images=10)

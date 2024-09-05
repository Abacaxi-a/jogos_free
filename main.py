from playwright.sync_api import sync_playwright
import requests as r
import time
from platforms.epicgames import epicgames_colect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    epicgames_colect(page)
    

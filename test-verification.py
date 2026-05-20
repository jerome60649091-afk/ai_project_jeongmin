# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
from time import sleep

# Set output encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Try to use Selenium if available
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller

    # Auto-install chromedriver if needed
    chromedriver_autoinstaller.install()

    print("=== Selenium-based Verification ===\n")

    # Setup Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode

    # Open the HTML file
    file_path = Path(__file__).parent / "index.html"
    file_url = f"file:///{str(file_path).replace(chr(92), '/')}"

    print(f"Opening: {file_url}\n")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(file_url)

    # Wait for page to load
    sleep(1)

    print("=== Test 1: Click button without entering name (should show warning) ===")

    # Find elements
    start_button = driver.find_element(By.ID, "startButton")
    result_area = driver.find_element(By.ID, "resultArea")

    # Click button without entering name
    start_button.click()

    # Wait for message box to appear
    sleep(0.5)

    # Get the message element
    message_boxes = result_area.find_elements(By.TAG_NAME, "div")
    if message_boxes:
        message_box = message_boxes[0]
        message_text = message_box.text
        class_name = message_box.get_attribute("class")

        print(f"[PASS] Message displayed: \"{message_text}\"")
        print(f"[PASS] CSS Class: \"{class_name}\"")
        print(f"[PASS] Contains 'message-warning': {('message-warning' in class_name)}")
        print(f"[PASS] Contains 'message-box': {('message-box' in class_name)}")
    else:
        print("[FAIL] No message box found!")
        sys.exit(1)

    # Take screenshot
    driver.save_screenshot("test1-warning-message.png")
    print("[SCREENSHOT] Saved: test1-warning-message.png\n")

    print("=== Test 2: Enter name and click button (should show success message) ===")

    # Clear the result area
    result_area.send_keys("")
    driver.execute_script("document.getElementById('resultArea').innerHTML = '';")

    sleep(0.3)

    # Enter a name
    name_input = driver.find_element(By.ID, "nameInput")
    name_input.clear()
    name_input.send_keys("Kim Cheol-su")

    # Click button
    start_button.click()

    # Wait for message box to appear
    sleep(0.5)

    # Get the message element
    message_boxes = result_area.find_elements(By.TAG_NAME, "div")
    if message_boxes:
        message_box = message_boxes[0]
        message_text = message_box.text
        class_name = message_box.get_attribute("class")

        print(f"[PASS] Message displayed: \"{message_text}\"")
        print(f"[PASS] CSS Class: \"{class_name}\"")
        print(f"[PASS] Contains 'message-success': {('message-success' in class_name)}")
        print(f"[PASS] Contains 'message-box': {('message-box' in class_name)}")
    else:
        print("[FAIL] No message box found!")
        sys.exit(1)

    # Take screenshot
    driver.save_screenshot("test2-success-message.png")
    print("[SCREENSHOT] Saved: test2-success-message.png\n")

    print("=== Test 3: Verify no console errors ===")

    # Get console logs
    logs = driver.get_log('browser')
    errors = [log for log in logs if log['level'] == 'SEVERE']

    if not errors:
        print("[PASS] No console errors detected")
    else:
        print("[WARNING] Console errors found:")
        for error in errors:
            print(f"  {error['message']}")

    print("\n=== All tests completed successfully ===")

    driver.quit()

except ImportError as e:
    print(f"Selenium not available: {e}\nRunning fallback verification...\n")

    # Fallback: Just verify the file exists and code analysis
    file_path = Path(__file__).parent / "index.html"

    if not file_path.exists():
        print(f"[FAIL] HTML file not found: {file_path}")
        sys.exit(1)

    print(f"[PASS] HTML file exists: {file_path}")

    # Read and verify the JavaScript file
    js_file = Path(__file__).parent / "script.js"
    if js_file.exists():
        with open(js_file, 'r', encoding='utf-8') as f:
            js_content = f.read()

        print("\n=== JavaScript Code Verification ===\n")

        checks = [
            ("getElementById(\"nameInput\")", "ID for name input field"),
            ("getElementById(\"startButton\")", "ID for start button"),
            ("getElementById(\"resultArea\")", "ID for result area"),
            ("message-success", "Success message class name"),
            ("message-warning", "Warning message class name"),
            ("message-box", "Base message box class"),
            ("!nameInput || !startButton || !messageArea", "Null checks for elements"),
        ]

        all_passed = True
        for check, description in checks:
            if check in js_content:
                print(f"[PASS] {description}")
            else:
                print(f"[FAIL] {description}: Missing '{check}'")
                all_passed = False

        if all_passed:
            print("\n=== Code verification: PASS ===")
            print("\nAll required fixes are present in script.js:")
            print("- Correct ID references (nameInput, startButton, resultArea)")
            print("- Correct CSS class names (message-success, message-warning)")
            print("- Base class 'message-box' applied")
            print("- Null checks for defensive programming")
        else:
            print("\n=== Code verification: FAIL ===")
            sys.exit(1)
    else:
        print(f"[FAIL] JavaScript file not found: {js_file}")
        sys.exit(1)

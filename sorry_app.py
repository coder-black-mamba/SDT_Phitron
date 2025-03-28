import time
import pyautogui 
print("Running the script in 5 seconds...")
time.sleep(5)
print("Action started...")

for i in range(100):
    print(f"Saying Sorry {i+1}")
    pyautogui.write(f"Sorry {i+1}")
    pyautogui.press('enter')
    pyautogui.press('enter')
    time.sleep(1)

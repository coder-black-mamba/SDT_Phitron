import pyautogui
import time 

n = int(input("Enter the number of rows: "))  # Prompting input

time.sleep(5)  # Wait before execution (to switch to another window)
for i in range(n):
    str_to_print = ""  # Reset for each row
    for j in range(i+1):  # Use a different variable (j)
        str_to_print += "#"
    str_to_print += "\n"
    
    pyautogui.write(str_to_print)  # Simulate typing

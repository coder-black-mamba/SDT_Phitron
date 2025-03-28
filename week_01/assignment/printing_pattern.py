# Take a number from the user and draw a pyramid using PyAutoGUI	
import pyautogui
import time 


n = int(input())
 

# time.sleep(5)


for i in range(n):
    str_to_print=""
    for j in range(i+1):
        str_to_print+="#"
    str_to_print+="\n"
    # print(str_to_print)
    pyautogui.write(str_to_print)
    # print("\n")




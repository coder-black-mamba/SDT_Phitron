# Take a number from the user and draw a pyramid using PyAutoGUI	
import pyautogui
import time 


n = int(input())
# print("\n")

time.sleep(2)
main_str=""

for i in range(n):
    str_to_print=""
    for j in range(i+1):
        str_to_print+="#"
    str_to_print+="\n"
    main_str+=str_to_print
    # print(str_to_print)
    pyautogui.write(str_to_print)
    # print("\n")




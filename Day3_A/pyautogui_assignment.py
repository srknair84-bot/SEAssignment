import pyautogui
import pyscreeze
import time
from datetime import date
import os
# Get the current date
today = date.today()    
#print("Today's date:", today)

#pyautogui.alert("Today's date is: " + str(today))   

pyautogui.FAILSAFE=True  # Enable fail-safe feature
pyautogui.PAUSE=1  # Set a pause duration between actions

print ("opening chrome and navigating to the URL....")
pyautogui.hotkey('win', 'r')  # Open the Run dialog
pyautogui.typewrite('chrome\n')  # Type 'chrome' in the Run dialog
pyautogui.press('enter')  # Press Enter to open Chrome
#time.sleep(2)  # Wait for 2 seconds
pyautogui.typewrite('https://www.bseindia.com/sensex/code/16')  # Type the URL
time.sleep(3)  # Wait for 2 seconds
pyautogui.press('enter')  # Press Enter to open Excel   
time.sleep(7)  # Wait for 2 seconds

print("selecting the text and copying it...")
#pyautogui.moveTo(1000, 800)  # Move the mouse to the specified coordinates
pyautogui.dragTo(1500, 1000, duration=3)  # Drag the mouse to the specified coordinates over 1 second
pyautogui.rightClick()  # Right-click at the current mouse position
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
time.sleep(5)  # Wait for 1 second


print("Opening and pasting the copied text into Excel...")
pyautogui.hotkey('win', 'r')  # Open the Run dialog againD
pyautogui.typewrite('excel')  # Type 'excel' in the Run dialog
pyautogui.press('enter')  # Press Enter to open Excel   
time.sleep(5)

pyautogui.hotkey('ctrl', 'n')  # Create a new Excel workbook
time.sleep(2)
pyautogui.press('enter')  # Press Enter to open Excel   
time.sleep(2)
pyautogui.press('enter')  # Press Enter to open Excel   

pyautogui.hotkey('ctrl', 'v')  # Paste the copied text into Excel
time.sleep(3)
print("Taking a screenshot of the Excel window...")
pyautogui.screenshot('screenshot.png')  # Take a screenshot and save it as 'screenshot.png'
time.sleep(5)

pyautogui.hotkey('ctrl','s')  # Save the file
time.sleep(1)   
pyautogui.press('tab',interval=0.5)  # Press Tab to navigate to the filename field
pyautogui.press('tab',interval=0.5)  # Press Tab to navigate to the filename field
pyautogui.press('tab',interval=0.5)  # Press Tab to navigate to the filename field

pyautogui.press('space',interval=0.5)  # Press Space to select the filename field

pyautogui.press('tab',interval=0.5)  # Press Tab to navigate to the filename field

pyautogui.press('down',interval=0.5)  # Press Down to navigate to the filename field
pyautogui.press('down',interval=0.5)  # Press Down to navigate to the filename field
pyautogui.press('down',interval=0.5)  # Press Down to navigate to the filename field
pyautogui.press('down',interval=0.5)  # Press Down to navigate to the filename field
pyautogui.press('down',interval=0.5)  # Press Down to navigate to the filename field

pyautogui.press('space',interval=0.5)  # Press Space to select the filename field

# Get the current date to use in the filename
current_date = date.today()

print("Todays Date is: ", current_date)

time.sleep(5)

filename = f"Todays_Sensex_{current_date}.xlsx"

# Define the folder cleanly using a raw string
folder_path = r"D:\Ramesh\PROGRAM\2026\SocialEagle\Assignment\Day3_A"

# Let Python perfectly glue the folder path and filename together
full_path = os.path.join(folder_path, filename)


pyautogui.typewrite(full_path,interval=0.5)  # Type the filename
time.sleep(0.5)

pyautogui.press('enter')  # Press Enter to confirm the filename

time.sleep(1)

pyautogui.hotkey('alt','f4')

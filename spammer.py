import pyautogui, time
time.sleep(5)
with open("spammerScript.txt", "r") as script:
	for word in script.readlines():
		pyautogui.typewrite(word)
		pyautogui.press("enter")
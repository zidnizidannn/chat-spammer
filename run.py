import pyautogui
import time

position= pyautogui.position()
pesan= "min gas e entek"

for a in range(30):
    pyautogui.click(position.x, position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.01)
    pyautogui.typewrite(["enter"])

# for a in range(1, 11):
#     pesan = "test " + str(a) + " dicoba"
#     pyautogui.click(position.x, position.y)
#     pyautogui.typewrite(pesan)
#     print(pesan)
#     time.sleep(0.01)
#     pyautogui.typewrite(["enter"])
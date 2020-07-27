import cv2
import glob

import pyautogui
import win32gui

import time

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
large_image = cv2.imread('gui-test/screenshot.png')[745:1150, 75:1850]

champions = glob.glob('test/*.png')
champs = []

for champion in champions:
	small_image = cv2.imread(champion)

	result = cv2.matchTemplate(small_image, large_image, method)

	# We want the minimum squared difference
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	MPx,_ = mnLoc
	slice_champ = champion[5:]
	name_champ = slice_champ.split("-")[0]
	champs.append((name_champ, mn, mnLoc))

team = sorted(champs, key = lambda x: x[1])[:10]
picks = sorted(team, key = lambda x: x[2])
#print(picks)
print([x[0] for x in picks])

# Display the original image
cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(0)
# Draw the rectangle:
# Extract the coordinates of our best match
#MPx,MPy = scoreLoc

# ytp-pause-overlay ytp-scroll-min
# ytp-chrome-bottom

# def screenshot(window_title=None):
#     if window_title:
#         hwnd = win32gui.FindWindow(None, window_title)
#         if hwnd:
#             win32gui.SetForegroundWindow(hwnd)
#             x, y, x1, y1 = win32gui.GetClientRect(hwnd)
#             x, y = win32gui.ClientToScreen(hwnd, (x, y))
#             x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
#             im = pyautogui.screenshot(region=(x, y, x1, y1))
#             return im
#         else:
#             print('Window not found!')
#     else:
#         im = pyautogui.screenshot()
#         return im


# # im = screenshot('LoL Esports - Google Chrome')
# # if im:
# #     im.show()
# #     im.save(r"gui_test\screenshot.png")
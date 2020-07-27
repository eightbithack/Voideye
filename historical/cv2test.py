import cv2
import glob

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
large_image = cv2.imread('red-team.png')
champions = glob.glob('test/*.png')
print(champions)
score = 100
scoreLoc = None

for champion in champions:
	small_image = cv2.imread(champion)

	result = cv2.matchTemplate(small_image, large_image, method)

	# We want the minimum squared difference
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	if mn < score:
		score = mn
		scoreLoc = mnLoc
# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = scoreLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)

# The image is only displayed if we call this
cv2.waitKey(0)
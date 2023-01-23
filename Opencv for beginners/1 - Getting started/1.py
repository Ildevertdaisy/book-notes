# Read the image "Apollo-8-Launch.jpg" and store it in a variable called "image".
image = cv2.imread('Apollo-8-Launch.jpg')

# Display the image using the imshow() function from matplotlib.
plt. figure(figsize = [10, 10])
plt.imshow(image)
plt. title('Apollo-8-Launch.jpg', fontsize=16)

# Save the image to the file system as a PNG file.
cv2.imwrite('Apollo-8-Launch.png', image)

# Read the saved image from the file system and store it in a variable called "image_png".
image_png = cv2.imread('Apollo-8-Launch.png')

# Display the saved image using the imshow() function from matplotlib.
plt. figure(figsize = [10, 10])
plt.imshow(image_png)
plt. title('Apollo-8-Launch.png', fontsize=16)

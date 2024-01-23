from PIL import Image

image = Image.open('download.jpg')

image.show()

width,height=image.size
print(width,height)

new_width =width*3
new_height = height*3

new_image = image.resize((new_width,new_height))
new_image.show()
print(new_width,new_height)
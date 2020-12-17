from PIL import Image

im1 = Image.open('word_matrix.png')
im2 = Image.open('mask.png').resize(im1.size)

mask = Image.new('L',im1.size, 128)
final_img = Image.composite(im1,im2,mask)

print(final_img) # Blended Image of im1 & im2 

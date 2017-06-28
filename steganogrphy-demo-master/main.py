# Demo of Steganography

from steganography.steganography import Steganography

fo = open("messages.txt", "r")
lines = fo.readlines()

counter = 1
for line in lines:
    original_image = "original_images\\%d.jpg"%(counter)
    output_image = "encrypted_images\\secret%d.jpg"%(counter)
    message = line
    Steganography.encode(original_image, output_image, message)
    print("%d Successful"%(counter))
    counter += 1
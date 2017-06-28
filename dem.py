from steganography.steganography import  *
original_image=raw_input("enter image\n")
output="output.jpg"
text=raw_input("enter")
Steganography.encode(original_image,output,text)
secret=Steganography.decode("output.jpg")
print (secret)

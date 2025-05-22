import string
import random
text=" "+ string.punctuation + string.digits + string.ascii_letters
text = list(text)
key = text.copy()

print(f"text:{text}")
print(f"key:{key}")
random.shuffle(key)

plant_text=input("enter a text to encrypt:")
cipher_text=""
for letter in plant_text:
    index=text.index(letter)
    cipher_text +=key[index]
print(f"original message:{plant_text}")
print(f"encrypted message:{cipher_text}")
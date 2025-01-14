from PIL import Image
img = Image.open("face.png")
img2 = Image.open("котенок.png")

img2.show()
img.show()
#Открываем изображения




# Можем получить некоторую информацию об изображениях:
print("'face'")
print(f"Width: {img.width}")
print(f"Height: {img.height}")
print(f"Filename: {img.filename}")
print(f"Format: {img.format}")
print(f"Mode: {img.mode}")
print("\n'cat'")
print(f"Width: {img2.width}")
print(f"Height: {img2.height}")
print(f"Filename: {img2.filename}")
print(f"Format: {img2.format}")
print(f"Mode: {img2.mode}")

# зеркальное отображение








#зеркальное отображение

img = Image.open("face.png")
img.show()
img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img.save("face_new.png")
img = Image.open("face_new.png")
img3 = Image.open("face_new.png")

img3.show()




with open("Trainging/image.jpg", "rb") as f:
    data = f.read()
    print("Bytes read :", len(data))

with open("image_copy.jpg", "wb") as f:
    f.write(data)
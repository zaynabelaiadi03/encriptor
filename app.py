content= open("msg.txt", "r+")

print(content.read())

content.write("This is a new line added to the file.\n")

content.close()
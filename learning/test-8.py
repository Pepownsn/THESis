## writing to the file

text = 'sample Text to Save \nNewline!'
saveFile = open('exampleFile.txt','w')
## W =write // R=read
saveFile.write(text)
saveFile.close()

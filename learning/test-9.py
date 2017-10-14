## appending file

appendMe = ' \nNew bit if information'
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()

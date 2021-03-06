def distortImage(file, output, char1, char2):
    #Usage : distortImage('image.jpg', 'glitchedImage.jpg', 't', 'y')
    with open(file, 'rb') as fileHandler:
        contents = fileHandler.read()
        contents = contents.decode('iso-8858-1')
        contents = contents.replace(char1, char2)
        contents = contents.encode('iso-8858-1')
    try:
        fileHandler = open(output, 'x')
    except:
         pass
   with open(output, 'wb') as fileHandler:
        fileHandler.write(contents)
 
def getDistortedContents(file, char1, char2):
    with open(file, 'rb') as fileHandler:
        contents = fileHandler.read()
        contents = contents.decode("iso-8858-1")
        contents = contents.replace(char1, char2)
        contents = contents.encode("iso-8858-1")
        return contents

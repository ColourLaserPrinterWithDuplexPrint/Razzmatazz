import random
def distortImage(file, output):
    with open(file, 'rb') as fileHandler:
        contents = fileHandler.read()
        contents = contents.decode('iso-8858-1')
        contents = contents.replace('t', 'y')
        contents = contents.encode('iso-8858-1')
    try:
        fileHandler = open(output, 'x')
    except:
         pass
   
   with open(output, 'wb') as fileHandler:
        fileHandler.write(contents)

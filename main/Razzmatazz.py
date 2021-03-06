if __name__ == '__main__':
    try:
        file = input("Image To Distort : ")
        file2 = input("Output File (Creates A New File) : ")
        repl1 = input("Character To Replace : ")
        repl2 = input("Character To Replace With : ")
        with open(file, 'rb') as fileHandler:
            contents = fileHandler.read()
            contents = contents.decode('iso-8859-1')
            contents = contents.replace(repl1, repl2)
        with open(file2, 'x') as fileHandler:
            print("Created New File")
            contents = contents.encode('iso-8859-1')
        with open(file2, 'wb') as fileHandler:
            fileHandler.write(contents)
        input("Done ! : ")
    except Exception as e:
        print(e)
        input("Press Any Key To Exit : ")

def distortImage(file, output):
    with open(file, 'rb') as fileHandler:
        contents = fileHandler.read()
        contents = contents.decode('iso-8858-1')
        contents = contents.replace('t', 'y')
        contents = contents.encode('iso-8858-1')
    with open(file, 'wb') as fileHandler:
        fileHandler.write(contents)

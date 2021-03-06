if __name__ == '__main__':
    try:
        file = input("Image To Distort : ")
        file2 = input("Output File (Creates A New File) : ")
        #Taking Input
        
        repl1 = input("Character To Replace : ")
        repl2 = input("Character To Replace With : ")
        #Gives the user an option of how to distort the image
        
        with open(file, 'rb') as fileHandler:
            #Opens the file in read bytes mode
            
            contents = fileHandler.read()
            #Gets the contents of the file
            
            contents = contents.decode('iso-8859-1')
            #Decodes the contents of the file with the 'iso-8859-1' format
            
            contents = contents.replace(repl1, repl2)
            #Replaces the first input character with the second input character
            
        with open(file2, 'x') as fileHandler:
            #Creates a new file
            
            print("Created New File")
            
            contents = contents.encode('iso-8859-1')
            #Re-Encodes the file contents
            
        with open(file2, 'wb') as fileHandler:
            #Opens the created output file
            
            fileHandler.write(contents)
            #Writes the contents to the output file
            
        input("Done ! : ")
    except Exception as e:
        #Checks if there's an error
        
        print(e)
        input("Press Any Key To Exit : ")

# imports the library (https://pypi.org/project/ExifRead/)
# License    OSI Approved :: BSD License
# pip install ExifRead
import exifread
# imports the library (https://docs.python.org/3/library/os.html)
import os
import csv

# Asks for filename MUST BE JPG
imageName = input("Name of image = ")

# Checks if filename exists
if (os.path.isfile(imageName)):

    # Opens image file for reading (must be in binary mode)

    with open (imageName, 'rb') as imageFile:

        # creates a dictionary with EXIF info
        exifInfo = exifread.process_file(imageFile)
        # Deletes de info from JPEGThumbnail
        del exifInfo['JPEGThumbnail']
        

        # Prints the tags and their values
        for key in exifInfo.keys():
            print(key," = ", exifInfo[key])

# EXPERIMENTAL PHASE
    writeFile = input("Would you like to save the data as .json file? [Y/n]")
    if (writeFile == "Y" or writeFile == "y"):
        with open('csv_file.csv', 'w') as exifFile:
            for key in exifInfo.keys():
                exifFile.write("%s,%s"%(key,exifInfo[key]))
        

       
    else:
        print("Bye!")


else:
    print("Sorry, no such file!")



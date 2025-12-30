with open("../../../../../Desktop/my_file.txt", mode="a") as file:
    file.write("\nI came to Kansas City, Missouri, US - 64111")
# /Users/roshini/Desktop/my_file.txt - If the file is in desktop
# /Users/roshini/Desktop
with open("new_file.txt", mode= "w") as file:
    file.write("This is my new file.")

# /Users/roshini/Documents/PracticeExamples/100DaysofPython/Day24/test

# To find the relative path, you have to write '../' with the no. of levels you have to go from the current directory
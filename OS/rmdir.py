import os

#os.mkdir("./my_first_directory")
os.mkdir("./my_first_directory/my_second_directory")
print(os.listdir("./my_first_directory"))
os.rmdir("./my_first_directory/my_second_directory")
print(os.listdir("./my_first_directory"))
    
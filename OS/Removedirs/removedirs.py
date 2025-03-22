import os
print(os.getcwd())
os.makedirs("my_first_directory/my_second_directory")
print(os.listdir())
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
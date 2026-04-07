
# File Handling
"""# File Handling using with statement - This is a comment too"""

# Reading from a file
my_file = open('./files/my_file.txt', 'r') # Opening the file in read mode, the file can be accessed through relative path
# print(my_file.read()) # Output: the entire content of the file
# print(my_file.readline()) # Output: Hello world from my text file - this will read the first line of the file
print(my_file.readline(3)) # Output: Hel - this will read the first 3 characters of the first line

# if you read a file or a line, the file pointer will be at the end of the file or at the end of the line, so if you try to read it again, it will return an empty string or will read from the current position.
# You can use the seek() method to move the file pointer back to the beginning of the file.
my_file.seek(0) # Moving the file pointer back to the beginning of the file

my_file.close() # Closing the file, you can't read or write to file that is closed, you need to open it again to read or write to it.


# writing to a file
write_file = open('./files/write_file.txt', "w") # Opening the file in write mode
write_file.write("This is a new file created using python. \n") # Writing a line to the file
write_file.close() # Closing the file
write_file = open('./files/write_file.txt', "a") # Opening the file in append mode
write_file.write("This line is added to the file using append mode. \n") # Writing a line to the file
write_file.close()

# Copying a file
write_file = open('./files/copied_file.txt', "w")
my_file = open('./files/my_file.txt', 'r') # Opening the file in read mode
for line in my_file:
   write_file.write(line) # Writing each line of the original file to the new file
my_file.close()
write_file.close()

# when writing or reading an Image, we use binary mode, which is donated by 'rb' for reading and 'wb' for writing in open() function.
# This is because images are not text files, they are binary files, and we need to read and write them in binary mode to preserve their integrity.
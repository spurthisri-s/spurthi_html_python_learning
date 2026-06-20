# Writing to a file

file = open("notes.txt", "w")

file.write("Hello, this is my first file handling program.")

file.close()

print("Data written successfully!")


file = open("notes.txt", "r")

data = file.read()

print(data)

file.close()




file = open("notes.txt", "a")

file.write("\nLearning Python File Handling")

file.close()

print("Data Added Successfully!")
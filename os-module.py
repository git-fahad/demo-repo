import os

cwd = os.getcwd()
print("\nThe current working directory is: ", cwd, "--Do not change!!\n")
files = os.listdir(cwd)
print(files,"\n")
# os.chdir("/Users/fahad/Scripting/PythonTutorials")
cwd = os.getcwd()
print("The new working directory is: ", cwd, "--Do not change!!")

print("\n\n")

# Creating a new directory

# os.mkdir("NewDirectory")
# os.makedirs("test/randomcode", exists_ok = True)

file1 = "testfile.txt"
combined = os.path.join(cwd, "testfile.txt")
print(combined)
print(os.path.exists(combined))
print("\n")
print(os.stat(cwd))

print("\n")

v = os.environ.get("PATH")
print(os.getlogin())
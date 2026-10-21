with open("file1.txt", "r") as f1:
    content1 = f1.read()
with open("file2.txt", "r") as f2:
    content2 = f2.read()
with open("merged.txt", "w") as f3:
    f3.write(content1 + "\n" + content2)
print("Files merged successfully.")

with open("file1.txt", "r") as f1:
    lines1 = f1.readlines()
with open("file2.txt", "r") as f2:
    lines2 = f2.readlines()

for i in range(max(len(lines1), len(lines2))):
    line1 = lines1[i].strip() if i < len(lines1) else ""
    line2 = lines2[i].strip() if i < len(lines2) else ""
    if line1 != line2:
        print("Files are different.")
        print("First difference at line:", i + 1)
        print("File 1:", line1)
        print("File 2:", line2)
        break
else:
    print("Files are identical.")

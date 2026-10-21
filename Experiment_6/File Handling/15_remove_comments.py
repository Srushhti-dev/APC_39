with open("program.py", "r") as file:
    lines = file.readlines()

with open("without_comments.py", "w") as file:
    for line in lines:
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            if "#" in line:
                line = line.split("#")[0] + "\n"
            file.write(line)

print("Comments removed successfully.")

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")
        
        # Track the current file path
        self.file_path = None

        # Create Text Area
        self.text_area = tk.Text(self.root, font=("Arial", 12), undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Create Main Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Add File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Untitled - Notepad")
        self.file_path = None

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".txt", 
                                      filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            self.file_path = file.name
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, file.read())
            file.close()
            self.root.title(f"{self.file_path} - Notepad")

    def save_file(self):
        if self.file_path is None:
            self.save_as_file()
        else:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def save_as_file(self):
        file = filedialog.asksaveasfile(initialfile="Untitled.txt", 
                                        defaultextension=".txt", 
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            self.file_path = file.name
            with open(self.file_path, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{self.file_path} - Notepad")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
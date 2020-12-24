import shutil
import os
import time
import subprocess


class FileMan:
    MENU = [
        "1. Read a file",
        "2. Write to a file",
        "3. Append text to a file",
        "4. Delete a file",
        "5. List files in a directory",
        "6. Check file existence",
        "7. Move a file",
        "8. Copy a file",
        "9. Create a directory",
        "10. Delete a directory",
        "11. Open a program",
        "12. Exit",
    ]

    STEP_MENU = [
        "1. Return to menu",
        "2. Exit",
    ]

    def read(self):
        path = input("Enter the file path ro read:\n")
        try:
            with open(path, "r") as r_file:
                print(r_file.read())
                input("Press Enter")
        except FileNotFoundError as err:
            print("No such file or directory:", err.filename)

    def write(self):
        path = input("Enter the path of file to write or create")
        if os.path.isfile(path):
            print("Rebuilding the executing file")
        else:
            print("Creating the file")

        text = input("Enter text:")
        with open(path, "w") as w_file:
            w_file.write(text)

    def __init__(self):
        self._run = True

    def __call__(self, *args, **kwargs):
        while self._run:
            try:
                os.system("clear")
            except OSError:
                os.system("cls")

            try:
                dec = int(input("\n".join(self.MENU)))
            except ValueError:
                print("Please input integer only...")
                continue

            if dec == 1:
                self.read()
            elif dec == 2:
                self.write()

            try:
                self._run = int(input("\n".join(self.STEP_MENU)))
            except ValueError:
                print("Please input integer only...")
                continue

            if self._run == 2:
                exit()


file_man = FileMan()
file_man()

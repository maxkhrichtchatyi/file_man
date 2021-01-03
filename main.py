import shutil
import os
import time
import subprocess

from rich import print
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table


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

    def _make_msg(self, title, text, msg_type="warning"):
        _msg_type = "bold red"
        if msg_type == "attention":
            _msg_type = "bold yellow"
        table = Table(show_header=True, header_style=_msg_type)
        table.add_column(title)
        table.add_row(text)
        self._console.print(table)

    def _make_menu(self, options, first_run=False):
        if not first_run:
            input("Press Enter")
        self._console.clear()
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("Number", style="dim", width=12)
        table.add_column("Description")

        for item in options:
            table.add_row(*item.split("."))
        self._console.print(table)

    def read(self):
        path = input("Enter the file path ro read: ")
        try:
            with open(path, "r") as r_file:
                syntax = Syntax(r_file.read(), "python", theme="monokai", line_numbers=True)
                self._console.print(syntax)
                input("Press Enter")
        except FileNotFoundError as err:
            self._make_msg(title="Warning!", text="No such file or directory: " + err.filename)

    def write(self):
        path = input("Enter the path of file to write or create:\n")
        if os.path.isfile(path):
            self._make_msg(title="Attention!", text="Rebuilding the executing file", msg_type="attention")
        else:
            self._make_msg(title="Attention!", text="Creating the file", msg_type="attention")

        text = input("Enter text:")
        with open(path, "w") as w_file:
            w_file.write(text)

    def delete(self):
        path = input("Enter the path of file for deletion:\n")
        if os.path.exists(path):
            self._console.print("File Found")
            os.remove(path)
            self._console.print("File has been deleted")
        else:
            self._console.print("File not found")

    def dirlist(self):
        path = input("Enter the Directory path to display:\n")
        if os.path.exists(path):
            for item in sorted(os.listdir(path)):
                self._console.print(item)
        else:
            self._console.print("Directory not found")

    def __init__(self):
        self._run = True
        self._console = Console()

    def __call__(self, *args, **kwargs):
        while self._run:
            self._make_menu(self.MENU, first_run=True)

            try:
                dec = int(input("Enter a number: "))
            except ValueError:
                print("Please input integer only...")
                continue

            if dec == 1:
                self.read()
            elif dec == 2:
                self.write()
            elif dec == 3:
                self.delete()
            elif dec == 5:
                self.dirlist()

            self._make_menu(self.STEP_MENU)

            try:
                self._run = int(input("Enter a number: "))
            except ValueError:
                print("Please input integer only...")
                continue

            if self._run == 2:
                exit()


file_man = FileMan()

try:
    file_man()
except KeyboardInterrupt:
    exit()

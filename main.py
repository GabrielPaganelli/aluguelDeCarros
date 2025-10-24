from tkinter import *

import ttkbootstrap as tb
from ttkbootstrap.constants import *

from views.mainWindow import MainWindow
from database.db import create_table

if __name__ == "__main__":
    root = tb.Window(themename="united")
    root.title("RentCar")
    root.resizable(False, False)

    create_table()
    
    app = MainWindow(root)

    root.mainloop()
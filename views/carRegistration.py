import tkinter as tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

from utils.treatment import str_to_int, validate_empty_fields
from utils.interface import FORM_CHOICES
from database.db import insert_car

class CarRegistration(tk.Toplevel):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.parent = self.mainWindow.root

        super().__init__(self.parent)
        self.title("Registro de Carro")
        self.resizable(False,False)

        self.vcmd_int = (self.register(lambda P: P.isdigit() or P == ""), "%P")
        self.vcmd_float = (self.register(lambda P: P.replace('.', '', 1).isdigit() or P == ""), "%P")

        self.grab_set()

        self._createFrames()
        self._createWidgets()

    def _createFrames(self):
        self.frame_main = tb.Frame(self, padding="10 10 10 10", relief="raised")
        self.frame_main.grid(column=0, row=0, sticky=(N, W, E, S))

    def createLabelledComboboxes(self, parent, labelText, comboValues, labelRow, pady=5):
        tb.Label(parent, text=labelText).grid(column=0, row=labelRow, sticky=W, padx=(0, 10))
        var = tk.StringVar()
        combobox = tb.Combobox(parent, textvariable=var, values=comboValues, state='readonly')
        combobox.current(0)
        combobox.grid(column=1, row=labelRow, columnspan=2, sticky=(W, E), pady=pady)

        return var
    
    def _createWidgets(self):
        tb.Label(self.frame_main, text="Registrar carro", style="primary", font=("Arial", 18, "bold")).grid(column=0, row=0, sticky=W, pady=(0, 10))

#________
        tb.Label(self.frame_main, text="Modelo:").grid(column=0, row=1, sticky=W, padx=(0, 10))
        self.modelEntry = tb.Entry(self.frame_main, width=30, style="primary")
        self.modelEntry.grid(column=1, row=1, sticky=(W, E), columnspan=4, pady=5)

        self.brandVar = self.createLabelledComboboxes(self.frame_main, "Marca", FORM_CHOICES['BRANDS'], 2)
#________

        self.fuelVar = self.createLabelledComboboxes(self.frame_main, "Combustível", FORM_CHOICES["FUEL"], 3)

        tb.Label(self.frame_main, text="Ano:").grid(column=3, row=5, sticky=W, padx=(0, 10))
        self.yearEntryRaw = tb.Entry(self.frame_main, width=30, validate="key", validatecommand=self.vcmd_int, style="primary")
        self.yearEntryRaw.grid(column=4, row=5, sticky=(W, E), pady=5)
#________

        self.categoryVar = self.createLabelledComboboxes(self.frame_main, "Categoria", FORM_CHOICES["CATEGORIES"], 4)
#________

        tb.Label(self.frame_main, text="Placa:").grid(column=0, row=5, sticky=W, padx=(0, 10))
        self.plateEntry = tb.Entry(self.frame_main, width=30, style="primary")
        self.plateEntry.grid(column=1, row=5, sticky=(W, E), pady=5)
#________

        self.transmissionVar = self.createLabelledComboboxes(self.frame_main, "Transmissão", FORM_CHOICES["TRANSMISSION"], 6)
#_______

        tb.Button(self.frame_main, text="Adiconar carro", command= lambda: self.loadEntry()).grid(column=1, row=7, sticky=(W, E, N, S), pady=5)
        tb.Button(self.frame_main, text="Cancelar", style="outline", command=self.destroy).grid(column=4, row=7, sticky=(E), pady=5)


    def loadEntry(self):
        self.yearEntry = str_to_int(self.yearEntryRaw.get())

        forms = {
            "model" : self.modelEntry.get(),
            "year" : self.yearEntry,
            "plate" : self.plateEntry.get(),
            "fuelType" : self.fuelVar.get(),
            "category" : self.categoryVar.get(),
            "brand" : self.brandVar.get(),
            "transmission" : self.transmissionVar.get()
        }

        validate = validate_empty_fields(forms)

        if validate:
            carData = [
                forms["model"],
                forms["year"],
                forms["plate"],
                forms["fuelType"],
                forms["category"],
                forms["brand"],
                forms["transmission"]
            ]

            insert = insert_car(carData)
            if insert:
                self.mainWindow.defaultFilters()
                self.mainWindow.loadData()

            self.destroy()
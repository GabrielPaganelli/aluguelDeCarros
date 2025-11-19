import tkinter as tk

import ttkbootstrap as tb
from ttkbootstrap.constants import *

from utils.interface import *
from database.db import search_cars, delete_car

from views.carRegistration import CarRegistration


class MainWindow:
    def __init__(self, root: tk.Tk):
        self.root = root
        self._createFrames()
        self._createWidgets()
        self._createTreeView()
        self.loadData()

    def loadData(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        filters = {
            "category": self.categoryVar.get() if self.categoryVar.get() != "Todas as categorias" else None,
            "brand": self.brandVar.get() if self.brandVar.get() != "Todas as marcas" else None,
            "max_price": self.priceVar.get() if self.priceVar.get() != "Sem limite" else None,
            "year": self.yearVar.get() if self.yearVar.get() != "Todos os anos" else None
        }

        data = search_cars(filters)

        for item in data:
            self.tree.insert('', 'end', values=item)

    def defaultFilters(self):
        self.categoryVar.set("Todas as categorias")
        self.brandVar.set("Todas as marcas")
        self.priceVar.set("Sem limite")
        self.yearVar.set("Todos os anos")

    def confirmDelete(self, dbId):
        deleteMessage = tk.messagebox.askyesno(
            title="Excluir carro", message="Você irá excluir este carro. Tem Certeza?")

        if deleteMessage:
            delete_car(dbId)

    def createContextMenu(self, dbId=None):
        contextMenu = tk.Menu(self.root, tearoff=0)
        contextMenu.add_command(label="Excluir", command=lambda: [self.confirmDelete(
            dbId), self.defaultFilters(), self.loadData()] if dbId else None)
        contextMenu.add_command(
            label="Editar", command=lambda: CarRegistration(self, car_data=dbId))

        return contextMenu

    def openContextMenu(self, event, tree):
        itemId = self.tree.identify_row(event.y)

        if itemId:
            tree.selection_set(itemId)
            values = self.tree.item(itemId, 'values')

            dbId = values[0]

        contextMenu = self.createContextMenu(dbId)
        contextMenu.post(event.x_root, event.y_root)

    def _createFrames(self):
        self.frame_top = tb.Frame(
            self.root, padding="10 10 10 10", relief="raised")
        self.frame_top.grid(column=0, row=1, sticky=(N, W, E, S))

        self.frame_bottom = tb.Frame(self.root, padding="10 10 10 10")
        self.frame_bottom.grid(column=0, row=2, sticky=(N, W, E, S))

    def createLabelledComboboxes(self, parent, labelText, comboValues, comboColumn, labelColumn, pady=(5, 15), width=30):
        tb.Label(parent, text=labelText).grid(
            column=labelColumn, row=1, sticky=(W, E), pady=(0, 0))
        var = tk.StringVar()
        combobox = tb.Combobox(parent, textvariable=var,
                               values=comboValues, state='readonly', width=width)
        combobox.current(0)
        combobox.grid(column=comboColumn, row=2, pady=pady,
                      padx=(0, 10), columnspan=2, sticky=(W, E, N, S))

        return var

    def _createWidgets(self):
        tb.Label(self.frame_top, text="Buscar carros", style="primary", font=(
            "Arial", 18, "bold")).grid(column=0, row=0,  columnspan=2, sticky=W, pady=(0, 10))

        self.categoryVar = self.createLabelledComboboxes(
            self.frame_top, "Categoria:", FILTER_CHOICES["CATEGORIES"], comboColumn=0, labelColumn=0)
        self.brandVar = self.createLabelledComboboxes(
            self.frame_top, "Marca:", FILTER_CHOICES["BRANDS"], comboColumn=2, labelColumn=2)
        self.priceVar = self.createLabelledComboboxes(
            self.frame_top, "Preço máximo p/dia:", FILTER_CHOICES["PRICES_PER_DAY"], comboColumn=4, labelColumn=4)
        self.yearVar = self.createLabelledComboboxes(
            self.frame_top, "Ano:", FILTER_CHOICES["YEAR"], comboColumn=6, labelColumn=6)

        tb.Button(self.frame_top, text="Buscar", command=self.loadData).grid(
            column=2, row=4, sticky=S, columnspan=2, padx=(0, 10))
        tb.Button(self.frame_top, text="Adicionar carro", style="outline", command=lambda: CarRegistration(
            self)).grid(column=4, row=4, sticky=S, columnspan=2, padx=(0, 10))
        tb.Button(self.frame_top, text="Filtros padrão", command=lambda: self.defaultFilters(
        )).grid(column=6, row=4, sticky=S, columnspan=2, padx=(0, 10))

    def _createTreeView(self):
        self.tree = tb.Treeview(
            self.frame_bottom, columns=TREEVIEW_COLUMNS, show='headings')

        for col in TREEVIEW_COLUMNS:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=95, anchor=CENTER)

        self.tree.grid(column=0, row=0, sticky=(N, S, W, E))

        scrollbar = tb.Scrollbar(
            self.frame_bottom, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(column=1, row=0, sticky=(N, S))
        self.tree.bind(
            "<Button-3>", lambda event: self.openContextMenu(event, self.tree))

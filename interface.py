from tkinter import *
from tkinter import ttk

class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title('Extração de Contorno')
        #Inserção de componentes
        self.popula_interface()
        self.root.mainloop()

    def popula_interface(self):

        tabs_notebook = ttk.Notebook(self.root)
        tabs_notebook.pack()

        frame_raw_image = Frame(tabs_notebook, width=500, height=500, bg="blue")
        frame_mask_image = Frame(tabs_notebook, width=500, height=500, bg="red")

        frame_raw_image.pack(fill="both", expand=1)
        frame_mask_image.pack(fill="both", expand=1)

        tabs_notebook.add(frame_raw_image, text='Tab 1')
        tabs_notebook.add(frame_mask_image, text='lalla')
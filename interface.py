from tkinter import *
from tkinter import ttk, filedialog

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

        frame_mask_image = Frame(tabs_notebook, width=500, height=500)
        frame_contour_image = Frame(tabs_notebook, width=500, height=500)
        frame_sections_image = Frame(tabs_notebook, width=500, height=500)

        frame_mask_image.pack(fill="both", expand=1)
        frame_contour_image.pack(fill="both", expand=1)
        frame_sections_image.pack(fill="both", expand=1)

        abre_arquivo_fotografia_botao = Button(frame_mask_image, text='Inserir', command=self.abre_arquivo_fotografia) 
        abre_arquivo_fotografia_botao.grid(row=0, column=0, padx=10, pady=10)

        tabs_notebook.add(frame_mask_image, text='Máscara')
        tabs_notebook.add(frame_contour_image, text='Contorno')
        tabs_notebook.add(frame_sections_image, text='Seções')

    def abre_arquivo_fotografia(self):
        self.root.filename = filedialog.askopenfilename(initialdir='./', title='Escolha um arquivo de imagem', filetype=(('Png Files', '*.png'),("All Files", "*.*")))
        print(self.root.filename)
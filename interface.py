from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.title('Extração de Contorno')
        #Inserção de componentes
        self.popula_interface()
        self.root.mainloop()

    def popula_interface(self):

        #Responsável pelo Notebook
        tabs_notebook = ttk.Notebook(self.root)
        tabs_notebook.pack()

        #Responsável pelos frames das abas
        frame_mask_image = Frame(tabs_notebook)
        frame_contour_image = Frame(tabs_notebook, width=500, height=500)
        frame_sections_image = Frame(tabs_notebook, width=500, height=500)

        frame_mask_image.pack(fill="both", expand=1)
        frame_contour_image.pack(fill="both", expand=1)
        frame_sections_image.pack(fill="both", expand=1)

        #Responsável pelo botão de inserir imagem
        abre_arquivo_fotografia_botao = Button(frame_mask_image, text='Inserir', command=lambda: self.abre_arquivo_fotografia(frame_mask_image)) 
        abre_arquivo_fotografia_botao.grid(row=0, column=0, padx=10, pady=10)

        #Sliders de Treshold para RGB para criar a máscara
        red_slider = Scale(frame_mask_image, from_=0, to=255, orient=HORIZONTAL)
        red_slider.grid(row=2, column=0, sticky='we')

        green_slider = Scale(frame_mask_image, from_=0, to=255, orient=HORIZONTAL)
        green_slider.grid(row=2, column=0, sticky='we')

        blue_slider = Scale(frame_mask_image, from_=0, to=255, orient=HORIZONTAL)
        blue_slider.grid(row=2, column=0, sticky='we')

        #Responsável pelas abas
        tabs_notebook.add(frame_mask_image, text='Máscara')
        tabs_notebook.add(frame_contour_image, text='Contorno')
        tabs_notebook.add(frame_sections_image, text='Seções')


    def abre_arquivo_fotografia(self, context):
        self.root.filename = filedialog.askopenfilename(initialdir='./', title='Escolha um arquivo de imagem', filetype=(('Png Files', '*.png'),("All Files", "*.*")))
        global canvas_arquivo_fotografia
        global imagem_arquivo_fotografia
        global label_fotografia
        canvas_arquivo_fotografia = Canvas(context, bg='black', width=500, height=500)
        imagem_arquivo_fotografia = ImageTk.PhotoImage(Image.open(self.root.filename))
        label_fotografia = Label(context, image=imagem_arquivo_fotografia)
        label_fotografia.grid(row=1, column=0, sticky='NW')
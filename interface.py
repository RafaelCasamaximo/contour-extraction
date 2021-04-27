from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from scrollableImage import ScrollableImage   
from analisaImagem import AnalisaImagem
import gc

class Interface:
    def __init__(self):
        #Dicionário com os widgets que existem na GUI da aplicação em cada aba e na raiz
        self.root_widgets = {}
        self.mask_widgets = {}
        self.contour_widgets = {}
        self.section_widgets = {}

        #Inicia biblioteca e define o nome da janela
        self.root = Tk()
        self.root.title('Extração de Contorno')
        #Define o tamanho mínimo da janela
        self.root.minsize(500, 500)

        #Popula abas
        self.popula_root()
        self.popula_mask_frame()
        #Inserção de componentes
        self.root.mainloop()

    def popula_root(self):
        #Responsável pelo Notebook
        tabs_notebook = ttk.Notebook(self.root)
        tabs_notebook.pack(fill=BOTH, expand=True)

        #Responsável pelos frames das abas
        frame_mask_image = Frame(tabs_notebook)
        frame_contour_image = Frame(tabs_notebook)
        frame_section_image = Frame(tabs_notebook, width=500, height=500)

        frame_mask_image.pack(fill=BOTH, expand=True)
        frame_contour_image.pack(fill=BOTH, expand=True)
        frame_section_image.pack(fill=BOTH, expand=True)

        #Responsável pelas abas
        tabs_notebook.add(frame_mask_image, text='Máscara')
        tabs_notebook.add(frame_contour_image, text='Contorno')
        tabs_notebook.add(frame_section_image, text='Seções')

        self.root_widgets = {
            "tabs_notebook": tabs_notebook,
            "frame_mask_image": frame_mask_image,
            "frame_contour_image": frame_contour_image,
            "frame_section_image": frame_section_image,
        }

        return

    def popula_mask_frame(self):
         #Responsável pelo botão de inserir imagem
        botao_insere_imagem = Button(self.root_widgets['frame_mask_image'], text='Inserir', command=self.on_botao_insere_imagem) 
        botao_insere_imagem.grid(row=0, column=0, padx=10, pady=10)
        return

    def popula_contour_frame(self):
        return

    def popula_section_frame(self):
        return

    #Métodos de Botões e Utilitários
    def on_botao_insere_imagem(self):
        self.root.filename = filedialog.askopenfilename(initialdir='./', title='Escolha um arquivo de imagem', filetype=(('.png Files', '*.png'),("All Files", "*.*")))
        if not self.root.filename:
            return
        
        imagem_arquivo_fotografia = ImageTk.PhotoImage(Image.open(self.root.filename))
        label_fotografia = ScrollableImage(self.root_widgets['frame_mask_image'], image=imagem_arquivo_fotografia, scrollbarwidth=6, width=500, height=500)
        #label_fotografia = Label(self.root_widgets['frame_mask_image'], image=imagem_arquivo_fotografia)
        label_fotografia.grid(row=1, column=0, sticky='NW', padx=10, pady=10)

        #Sliders de Treshold para RGB para criar a máscara
        min_hue = Scale(self.root_widgets['frame_mask_image'], from_=0, to=180, orient=HORIZONTAL, command=self.on_scale_change, label='Min Hue')
        min_hue.grid(row=2, column=0, sticky='we')

        max_hue = Scale(self.root_widgets['frame_mask_image'], from_=0, to=180, orient=HORIZONTAL, command=self.on_scale_change, label='Max Hue')
        max_hue.grid(row=3, column=0, sticky='we')

        min_satur = Scale(self.root_widgets['frame_mask_image'], from_=0, to=255, orient=HORIZONTAL, command=self.on_scale_change, label='Min Satur.')
        min_satur.grid(row=4, column=0, sticky='we')

        max_satur = Scale(self.root_widgets['frame_mask_image'], from_=0, to=255, orient=HORIZONTAL, command=self.on_scale_change, label='Max Satur.')
        max_satur.grid(row=5, column=0, sticky='we')

        min_value = Scale(self.root_widgets['frame_mask_image'], from_=0, to=255, orient=HORIZONTAL, command=self.on_scale_change, label='Min Value')
        min_value.grid(row=6, column=0, sticky='we')

        max_value = Scale(self.root_widgets['frame_mask_image'], from_=0, to=255, orient=HORIZONTAL, command=self.on_scale_change, label='Max Value')
        max_value.grid(row=7, column=0, sticky='we')

        opacity = Scale(self.root_widgets['frame_mask_image'], from_=0, to=100, orient=HORIZONTAL, command=self.on_scale_change, label='Opacity')
        opacity.grid(row=8, column=0, sticky='we')


        self.mask_widgets = {
            'imagem_arquivo_fotografia': imagem_arquivo_fotografia,
            'label_fotografia': label_fotografia,
            'min_hue': min_hue,
            'max_hue': max_hue,
            'min_satur': min_satur,
            'max_satur': max_satur,
            'min_value': min_value,
            'max_value': max_value,
            'opacity': opacity,
        }

    def on_scale_change(self, arg):
        hsva_threshold = {
            'min_hue': self.mask_widgets['min_hue'].get(),
            'max_hue': self.mask_widgets['max_hue'].get(),
            'min_satur': self.mask_widgets['min_satur'].get(),
            'max_satur': self.mask_widgets['max_satur'].get(),
            'min_value': self.mask_widgets['min_value'].get(),
            'max_value': self.mask_widgets['max_value'].get(),
            'opacity': self.mask_widgets['opacity'].get(),
        }

        imagem_arquivo_fotografia = AnalisaImagem.cria_mascara(hsva_threshold, self.root.filename)

        #label_fotografia = ScrollableImage(self.root_widgets['frame_mask_image'], image=imagem_arquivo_fotografia, scrollbarwidth=6, width=500, height=500)
        label_fotografia = Label(self.root_widgets['frame_mask_image'], image=imagem_arquivo_fotografia)
        label_fotografia.grid(row=1, column=0, sticky='NW', padx=10, pady=10)

        self.mask_widgets.update({
            'imagem_arquivo_fotografia': imagem_arquivo_fotografia,
            'label_fotografia': label_fotografia,
        })

        gc.collect()








    

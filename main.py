#Arquivo de manipulação de texto
import tkinter as tk
from tkinter import ttk, filedialog

'''Função retirada do chat GPT, pois eu não sabia como manipular arquivos. Ela
basicamente abre um arquivo de texto .txt e joga no widget Text.'''
def abrir_arquivo():
    """Abre um arquivo .txt e carrega no Text"""

    """Aqui é aberta a caixa de diálogos para procurar o arquivo a ser aberto, 
    utiliza-se o 'filedialog' do tkinter para esse propósito"""
    caminho = filedialog.askopenfilename(
        title='Abrir arquivo',
        filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')]
    )

    """Aqui é testado se foi selecionado algum arquivo"""
    if caminho:
        
        #Aqui se abre o arquivo e se atribui o conteúdo à variável 'conteudo'
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        #Aqui é deletado qualquer texto que ainda esteja no editor
        texto.delete('1.0', tk.END)

        #Aqui é inserido o conteúdo do arquivo selecionado
        texto.insert(tk.END, conteudo)

        #Aqui é atualizada a barra de status
        status_var.set(f'Arquivo aberto: {caminho}')

"""Função retirada do chat GPT pois eu não sabia como manipular arquivos"""
def salvar_arquivo():
    """Salva o conteúdo do Text em um arquivo .txt"""

    """Aqui é aberta a caixa de diálogo para salvar o arquivo .txt. Utiliza-se 
    o 'filedialog' para tanto."""
    caminho = filedialog.asksaveasfilename(

        #Aqui é definido o padrão de extensão de arquivo .txt
        defaultextension='.txt',
        filetypes=[('Arquivos de texto', '.txt'), ('Todos os arquivos', '*.*')],
        title='Salvar arquivo'
    )

    #Aqui é testado se foi selecionado um caminho para salvar o arquivo
    if caminho:

        #Aqui é pego o conteúdo do Text
        conteudo = texto.get('1.0', tk.END).strip()

        #Aqui é criado o arquivo .txt
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        #Aqui é atualizada a barra de status
        status_var.set(f'Arquivo salvo: {caminho}')


"""Aqui é criada a janela principal, ajustado o tamanho e definido que ela pode
ser redimensionada. É definido o título e ajustado o 'rowconfigure' e o 
'columnconfigure'."""
root = tk.Tk()
root.geometry('600x600+200+200')
root.resizable(True, True)
root.title('Bloco de notas')
root.rowconfigure(4, weight=1)
root.columnconfigure(0, weight=1)

"""Aqui é criada a barra de status que vai mostrar o nome do arquivo aberto e o 
nome do arquivo salvo"""
status = ttk.LabelFrame(root, text="Barra de status")
status.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

#Aqui é criada a variável de controle para a barra de status
status_var = tk.StringVar()

#Aqui é criado o Label para mostrar o status na barra de status
mostrador = tk.Label(status, textvariable=status_var)
mostrador.grid(row=0, column=0, columnspan=10, sticky='nsew', padx=10, pady=10)

#Aqui é criado um painel para mostrar as opções de salvamento e abertura
painel = ttk.LabelFrame(root, text="Opções")
painel.grid(row=1, column=0, rowspan=2, columnspan=5, sticky='nsew', padx=10, 
            pady=10)

#Aqui é criado o botão para abrir um arquivo
abrir = ttk.Button(painel, text='Abrir', width=10, command=abrir_arquivo)
abrir.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

#Aqui é criado um botão para salvar um arquivo
salvar = ttk.Button(painel, text='Salvar', width=10, command=salvar_arquivo)
salvar.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

#Aqui é criado o widget para manipular o texto
texto = tk.Text(root, height=20, wrap='word')
texto.grid(row=4, column=0, rowspan=25, columnspan=10, sticky='nsew', padx=10,
           pady=10)

#Aqui é para rodar o aplicativo
root.mainloop()
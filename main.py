from tkinter import*    
import tkinter.messagebox

#cores
cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"

#criando a janela

janela =Tk()
janela.geometry("530x205")#tamanho da janela
janela.configure(bg=cor1)#cor da janela

#configurando a janela

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

#funçao escale

def escale(valor):
    r= S_red.get()
    g= S_green.get()
    b= S_Blue.get()

 
    rgb = f'{r}, {g}, {b}'
    
    hexadecimal = "#%02x%02x%02x" % (r,g,b)    
    #alterando a cor do fundo da tela
    tela['bg'] = hexadecimal

    #alterando a entry

    E_cor.delete(0,END)
    E_cor.insert(0,hexadecimal)
#funçao cliclar

def onClick():
    #informar cor copiada

    tkinter.messagebox.showinfo( 'Cor', "a cor foi copiada")
        
    #serve para criar botao copiar

    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(E_cor.get())
    clip.destroy()



#configurando frame direito
l_red = Label(frame_direita,text="red", width=7, bg=cor1, fg="red", anchor='nw', font=("Time New Roman", 12, "bold"))
l_red.grid(row=0, column=0)
S_red= Scale(frame_direita,command= escale, from_=0, to=255, length=150,bg=cor1, fg='red', orient=HORIZONTAL)
S_red.grid(row=0, column=1)

l_green = Label(frame_direita,text="Green", width=7, bg=cor1, fg="green", anchor='nw', font=("Time New Roman", 12, "bold"))
l_green.grid(row=1, column=0)
S_green= Scale(frame_direita, command= escale,from_=0, to=255, length=150,bg=cor1, fg='green', orient=HORIZONTAL)
S_green.grid(row=1, column=1)

l_Blue = Label(frame_direita,text="Blue", width=7, bg=cor1, fg="Blue", anchor='nw', font=("Time New Roman", 12, "bold"))
l_Blue.grid(row=2, column=0)
S_Blue= Scale(frame_direita,command= escale, from_=0, to=255, length=150,bg=cor1, fg='Blue', orient=HORIZONTAL)
S_Blue.grid(row=2, column=1)

#Configurando o frame baixo

l_RGB = Label(frame_baixo,text="CÓDIGO HEX: ", bg=cor1, font=("Ivy", 10, "bold"))
l_RGB.grid(row=0, column=0,padx=5)

#entry

E_cor = Entry(frame_baixo, width=12, font=("Ivy", 10, "bold"), justify=CENTER)
E_cor.grid(row=0, column=1,padx=5)

#Botao copiar

b_copiar = Button(frame_baixo, command=onClick, text="Copiar a cor", bg=cor1, font=("Ivy", 8, "bold"), relief=RAISED, overrelief=RIDGE)
b_copiar.grid(row=0, column=2,padx=5)

#app nome

l_app_nome = Label(frame_baixo,text="Seletor de Cores", bg=cor1, font=("Ivy", 15, "bold"))
l_app_nome.grid(row=0, column=3,padx=40)


janela.mainloop()
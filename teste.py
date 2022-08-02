import tkinter as tk

nome = 'Juan Campos' #str
anos = 19  #int 
altura = 1.73  #float
e_maior = anos >= 18  #bool
peso = 66
imc= peso / (altura**2)






root = tk.Tk()

teste1 = tk.Label(root, text=f"Nome: {nome}")
teste1.pack()

teste2 = tk.Label(root, text=anos)
teste2.pack()

teste3 = tk.Label(root, text=altura)
teste3.pack()


root.mainloop()
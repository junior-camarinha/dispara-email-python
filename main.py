import tkinter as tk
import os
# Função para lidar com o clique no botão
def on_button_click():
    print("Botão clicado!")

# janelas
janela = tk.Tk()
janela.title("DISPARAR EMAIL LEMBRETE")

# janela.geometry("1024x800")
janela.geometry("600x300")
janela.resizable(False, False)

# frames
caminho = os.path.dirname(os.path.abspath(__file__))
caminho_img = os.path.join(caminho, "app", "background_image.png")
print(caminho_img)
print("app/background_image.png")
# Carregando a imagem de fundo
background_image = tk.PhotoImage(file=caminho_img)

# Criando um frame principal para cobrir toda a janela
main_frame = tk.Frame(janela)
main_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Exibindo a imagem de fundo no frame principal
background_label = tk.Label(main_frame, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# labels
label_email = tk.Label(main_frame, text="Digite seu email", font=2)
label_email.grid(row=0, column=0, pady=(50, 0), padx=(30,10), sticky=tk.W)
label_senha = tk.Label(main_frame, text="Digite sua senha", font=2)
label_senha.grid(row=1, column=0, pady=(30, 0), padx=(30,10), sticky=tk.W)

input_email = tk.Entry(main_frame, width=44, font=2)
input_email.grid(row=0, column=1, padx=(10, 30), pady=(50, 0))
input_senha = tk.Entry(main_frame,width=44, font=2)
input_senha.grid(row=1, column=1, padx=(10, 30), pady=(30, 0))

# botões 
botao_login_email = tk.Button(main_frame, text="Login",command=on_button_click,  font=("Helvetica", 12, "bold"))
botao_login_email.place(relx=0.05, rely=0.65, anchor="sw")
botao_sair_email = tk.Button(main_frame, text="Sair",command=on_button_click,  font=("Helvetica", 12, "bold"))
botao_sair_email.place(relx=0.22, rely=0.65, anchor="s")
botao_enviar_email = tk.Button(main_frame, text="Enviar email",command=on_button_click,  font=("Helvetica", 12, "bold"))
botao_enviar_email.place(relx=0.38, rely=0.65, anchor="s")
botao_relatorio_envio = tk.Button(main_frame, text="Relatório de envio",command=on_button_click,  font=("Helvetica", 12, "bold"))
botao_relatorio_envio.place(relx=0.76, rely=0.65, anchor="se")
botao_minimizar = tk.Button(main_frame, text="Minimizar",command=on_button_click,  font=("Helvetica", 12, "bold"))
botao_minimizar.place(relx=0.88, rely=0.65, anchor="s")

janela.mainloop()

# if __name__ == "__main__":





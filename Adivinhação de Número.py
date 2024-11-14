import tkinter as tk
import random

# Função que verifica a tentativa do usuário
def verificar_adivinhacao():
    global tentativas
    tentativa = int(entry.get())
    tentativas += 1

    if tentativa < numero_secreto:
        resultado_label.config(text="Número muito abaixo" , font=("Times new Roman", 12), bg="white", fg="darkblue")
    elif tentativa > numero_secreto:
        resultado_label.config(text="Número muito acima" , font=("Times new Roman", 12), bg="white", fg="darkblue")
    else:
        resultado_label.config(text=f"Você acertou! O número era {numero_secreto}." , font=("Times new Roman", 15), bg="darkgreen", fg="yellow")
        tentativas_label.config(text=f"Tentativas: {tentativas}" , font=("Times new Roman", 18, "bold"), bg="gray", fg="white")

    entry.delete(0, tk.END)  # Limpa o campo de entrada

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("400x400")
janela.configure(bg="#ADD8E6")  # Cor de fundo azul-claro

# Número secreto aleatório
numero_secreto = random.randint(1, 100)
tentativas = 0

# Caixa de entrada
entry = tk.Entry(janela)
entry.pack(pady=20)

# Botão para verificar o número
botao = tk.Button(janela, bg="darkgreen", fg="white", font=("Times new Roman", 14), text="Verificar", command=verificar_adivinhacao)
botao.pack(pady=10)

# Labels para mostrar o resultado e tentativas
resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=10)

tentativas_label = tk.Label(janela, text="Tentativas: 0", font=("Arial", 18, "bold"))
tentativas_label.pack()

# Inicia o loop da interface gráfica
janela.mainloop()

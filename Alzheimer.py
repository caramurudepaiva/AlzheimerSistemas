import tkinter as tk
from tkinter import messagebox

class AlzheimerChanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avaliação de Chance de Alzheimer")
        self.root.geometry("750x300")
        
        self.root.configure(bg="#f0f8ff")
        self.chance = 0
        
        self.perguntas = [
            ("A pessoa apresenta perda de memória?", 1),
            ("A pessoa apresenta mudanças de humor ou personalidade?", 1),
            ("A pessoa tem dificuldade em realizar tarefas básicas?", 1),
            ("A pessoa já teve caso de AVC/Derrame?", 2),
            ("A pessoa possui algum tipo de doença crônica (diabetes, hipertensão, colesterol elevado)?", 1),
            ("Há histórico de Alzheimer em parentes próximos da pessoa?", 2),
            ("A pessoa mantém hábitos saudáveis? (responda 'não' se os hábitos forem ruins)", 1),
            ("Informe a idade da pessoa:", "idade")
        ]
        
        self.indice_pergunta = 0
        self.resultado_label = None

        self.exibir_pergunta()

    def exibir_pergunta(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        progresso_label = tk.Label(self.root, text=f"Pergunta {self.indice_pergunta + 1} de {len(self.perguntas)}", bg="#f0f8ff", font=("Helvetica", 10))
        progresso_label.pack(pady=(10, 5))

        pergunta, valor = self.perguntas[self.indice_pergunta]
        pergunta_label = tk.Label(self.root, text=pergunta, wraplength=500, bg="#f0f8ff", font=("Helvetica", 12))
        pergunta_label.pack(pady=10)

        if valor == "idade":
            self.entrada_idade = tk.Entry(self.root)
            self.entrada_idade.pack(pady=5)
            proximo_button = tk.Button(self.root, text="Próximo", command=self.validar_idade, bg="#4CAF50", fg="white", font=("Helvetica", 10))
            proximo_button.pack(pady=(10, 20))
        else:
            button_frame = tk.Frame(self.root, bg="#f0f8ff")
            button_frame.pack(side=tk.BOTTOM, anchor=tk.SE, padx=20, pady=(10, 20))

            sim_button = tk.Button(button_frame, text="Sim", command=lambda: self.incrementar_chance(valor), bg="#4CAF50", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
            sim_button.pack(side=tk.LEFT, padx=10)

            nao_button = tk.Button(button_frame, text="Não", command=self.proxima_pergunta, bg="#f44336", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
            nao_button.pack(side=tk.LEFT, padx=10)

    def validar_idade(self):
        try:
            idade = int(self.entrada_idade.get())
            if idade >= 65:
                self.chance += 1
            self.proxima_pergunta()
        except ValueError:
            messagebox.showerror("Erro de entrada", "Por favor, insira uma idade válida.")

    def incrementar_chance(self, valor):
        self.chance += valor
        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.indice_pergunta += 1
        if self.indice_pergunta < len(self.perguntas):
            self.exibir_pergunta()
        else:
            self.exibir_resultado()

    def exibir_resultado(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        resultado_texto = self.sint_chance(self.chance)
        resultado_label = tk.Label(self.root, text=resultado_texto, wraplength=500, bg="#f0f8ff", font=("Helvetica", 14, "bold"))
        resultado_label.pack(pady=(30, 10))

        reiniciar_button = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, bg="#008CBA", fg="white", font=("Helvetica", 10), relief="raised", bd=2)
        reiniciar_button.pack(pady=(10, 20))

    def reiniciar(self):
        self.chance = 0
        self.indice_pergunta = 0
        self.exibir_pergunta()

    def sint_chance(self, chance):
        if chance <= 3:
            return "Baixa chance de Alzheimer. Monitoramento é recomendado."
        elif 4 <= chance <= 5:
            return "Moderada chance de Alzheimer. Consulta com especialista é recomendada."
        else:
            return "Alta chance de Alzheimer. Consulta com especialista é altamente recomendada."

root = tk.Tk()
app = AlzheimerChanceApp(root)
root.mainloop()
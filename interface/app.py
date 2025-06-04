import customtkinter as ctk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import paciente_controller, consultas_controller, lembrete_controller
from tkinter import messagebox

# Configura o tema global
ctk.set_appearance_mode("light")  # "dark" também disponível
ctk.set_default_color_theme("blue")  # tema azul

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Clínica Odonto - Sistema de Lembretes")
        self.geometry("700x550")
        self.resizable(False, False)
        self.minsize(700, 550)

        # Frame menu lateral
        self.menu_frame = ctk.CTkFrame(self, width=200)
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.criar_menu()
        self.menu_principal()

    def criar_menu(self):
        ctk.CTkLabel(self.menu_frame, text="Menu", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        btn_params = dict(width=140, height=40, corner_radius=8, fg_color="#0078D7", hover_color="#005A9E",)

        ctk.CTkButton(self.menu_frame, text="Início", command=self.menu_principal, **btn_params).pack(pady=10)
        ctk.CTkButton(self.menu_frame, text="Cadastrar Paciente", command=self.tela_cadastro_paciente, **btn_params).pack(pady=10)
        ctk.CTkButton(self.menu_frame, text="Agendar Consulta", command=self.tela_agendar_consulta, **btn_params).pack(pady=10)
        ctk.CTkButton(self.menu_frame, text="Listar Consultas", command=self.listar_consultas, **btn_params).pack(pady=10)
        ctk.CTkButton(self.menu_frame, text="Enviar Lembretes", command=self.enviar_lembretes, **btn_params).pack(pady=10)
        ctk.CTkButton(self.menu_frame, text="Sair", command=self.quit, fg_color="#d9534f", hover_color="#c9302c", width=140, height=40, corner_radius=8).pack(pady=20)

    def limpar_conteudo(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.content_frame, text="Bem-vindo ao seu \n Sistema de Lembretes", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=40)
        ctk.CTkLabel(self.content_frame, text="Use o menu lateral para navegar pelas opções.", font=ctk.CTkFont(size=14)).pack()
        ctk.CTkLabel(self.content_frame, text="World Code Sistemas.", font=ctk.CTkFont(size=8)).pack(pady=110)

    def tela_cadastro_paciente(self):
        self.limpar_conteudo()

        ctk.CTkLabel(self.content_frame, text="Cadastro de Paciente", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        nome_var = ctk.StringVar()
        tel_var = ctk.StringVar()
        email_var = ctk.StringVar()
        nasc_var = ctk.StringVar()

        def criar_campo(label):
            ctk.CTkLabel(self.content_frame, text=label).pack(anchor="w", pady=(10,2))
            entry = ctk.CTkEntry(self.content_frame, width=300)
            entry.pack()
            return entry

        nome_entry = criar_campo("Nome")
        tel_entry = criar_campo("Telefone")
        email_entry = criar_campo("E-mail")
        nasc_entry = criar_campo("Nascimento (YYYY-MM-DD)")

        def salvar():
            paciente_controller.cadastrar_paciente(
                nome_entry.get(),
                tel_entry.get(),
                email_entry.get(),
                nasc_entry.get()
            )
            messagebox.showinfo("Sucesso", "Paciente cadastrado.")
            self.menu_principal()

        ctk.CTkButton(self.content_frame, text="Salvar", command=salvar, width=150, height=40, corner_radius=12, fg_color="#0078D7", hover_color="#005A9E").pack(pady=20)

    def tela_agendar_consulta(self):
        self.limpar_conteudo()

        ctk.CTkLabel(self.content_frame, text="Agendar Consulta", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        pacientes = paciente_controller.listar_pacientes()
        if not pacientes:
            ctk.CTkLabel(self.content_frame, text="Nenhum paciente cadastrado.", font=ctk.CTkFont(size=14)).pack(pady=20)
            return

        paciente_var = ctk.StringVar(value=f"{pacientes[0].id} - {pacientes[0].nome}")
        data_var = ctk.StringVar()
        obs_var = ctk.StringVar()

        ctk.CTkLabel(self.content_frame, text="Selecione o Paciente:").pack(anchor="w", pady=(10,5))
        options = [f"{p.id} - {p.nome}" for p in pacientes]
        dropdown = ctk.CTkOptionMenu(self.content_frame, values=options, variable=paciente_var, width=300)
        dropdown.pack()

        def criar_campo(label):
            ctk.CTkLabel(self.content_frame, text=label).pack(anchor="w", pady=(15,2))
            entry = ctk.CTkEntry(self.content_frame, width=300)
            entry.pack()
            return entry

        data_entry = criar_campo("Data (YYYY-MM-DD HH:MM)")
        obs_entry = criar_campo("Observações")

        def agendar():
            pid = int(paciente_var.get().split(" - ")[0])
            consultas_controller.agendar_consulta(pid, data_entry.get(), obs_entry.get())
            messagebox.showinfo("Sucesso", "Consulta agendada.")
            self.menu_principal()

        ctk.CTkButton(self.content_frame, text="Agendar", command=agendar, width=150, height=40, corner_radius=12, fg_color="#0078D7", hover_color="#005A9E").pack(pady=30)

    def listar_consultas(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.content_frame, text="Consultas Agendadas", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)

        consultas = consultas_controller.listar_consultas()
        if not consultas:
            ctk.CTkLabel(self.content_frame, text="Nenhuma consulta agendada.", font=ctk.CTkFont(size=14)).pack()
            return

        for c in consultas:
            ctk.CTkLabel(self.content_frame, text=f"ID: {c[0]} - {c[1]} - {c[2]} - {c[3]}", font=ctk.CTkFont(size=12)).pack(anchor="w", pady=3)

    def enviar_lembretes(self):
        lembrete_controller.enviar_lembretes()
        messagebox.showinfo("Lembretes", "Lembretes enviados com sucesso.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
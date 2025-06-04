from utils.db import create_tables
from controllers import paciente_controller, consultas_controller, lembrete_controller
from models import paciente, lembrete, consultas

def main():
    create_tables()
    # print("Lembretes Clinica: Sistema Iniciado... Tabelas foram criadas com sucesso!")

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Buscar paciente por nome")
        print("4. Agendar consulta")
        print("5. Listar consultas")
        print("6. Enviar Lembrete")
        print("7. Cancelar consulta")
        print("8. Editar consulta")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            nascimento = input("Data de nascimento (YYYY-MM-DD): ")
            paciente_controller.cadastrar_paciente(nome, telefone, email, nascimento)

        elif opcao == "2":
            pacientes = paciente_controller.listar_pacientes()
            for p in pacientes:
                print(f"[{p.id}] {p.nome} - {p.telefone} - {p.email} - {p.data_nascimento}")

        elif opcao == "3":
            termo = input("Digite parte do nome: ")
            
            pacientes = paciente_controller.buscar_paciente_por_nome(termo)
            for p in pacientes:
                print(f"[{p.id}] {p.nome} - {p.telefone}")

        elif opcao == "4":
            pacientes = paciente_controller.listar_pacientes()
            print("\nSelecione um paciente pelo ID:")
            for p in pacientes:
                print(f"[{p.id}] {p.nome}")

            paciente_id = int(input("ID do paciente: "))
            data = input("Data da consulta (YYYY-MM-DD HH:MM): ")
            obs = input("Observações (opcional): ")
            consultas_controller.agendar_consulta(paciente_id, data, obs)

        elif opcao == "5":
            consultas = consultas_controller.listar_consultas()
            for c in consultas:
                print(f"[{c[0]}] Paciente: {c[1]} - Data: {c[2]} - Obs: {c[3]}")

        elif opcao == "6":
            lembrete_controller.enviar_lembretes()

        elif opcao == "7":
            consultas = consultas_controller.listar_consultas()
            for c in consultas:
                print(f"[{c[0]}] Paciente: {c[1]} - Data: {c[2]}")

            consulta_id = int(input("Digite o ID da consulta a cancelar: "))
            consultas_controller.cancelar_consulta(consulta_id)

        elif opcao == "8":
            consultas = consultas_controller.editar_consulta()
            for c in consultas:
                print(f"[{c[0]}] Paciente: {c[1]} - Data: {c[2]} - Obs: {c[3]}")

            consulta_id = int(input("Digite o ID da consulta a editar: "))
            nova_data = input("Nova data (YYYY-MM-DD HH:MM): ")
            novas_obs = input("Novas observações: ")
            consultas_controller.editar_consulta(consulta_id, nova_data, novas_obs)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("❌ Opção inválida.")
if __name__ == "__main__":
    main()
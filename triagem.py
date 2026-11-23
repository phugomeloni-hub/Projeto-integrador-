def ler_inteiro(mensagem, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(mensagem))
            if min_val is not None and valor < min_val:
                print(f"Erro: O valor deve ser no mínimo {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"Erro: O valor deve ser no máximo {max_val}.")
                continue
            return valor
        except ValueError:
            print("Erro: Por favor, digite apenas um número inteiro válido.")

def classificar_prioridade(nivel_dor, febre):
    if nivel_dor >= 8 or febre >= 39.0:
        return "Vermelho - Emergência"
    elif nivel_dor >= 5 or febre >= 37.5:
        return "Amarelo - Urgente"
    else:
        return "Verde - Pouco Urgente"

fila_atendimento = []
historico_pacientes = []

def adicionar_com_prioridade(paciente):
    prioridade = paciente["prioridade"]
    if "Vermelho" in prioridade:
        index = 0
        while index < len(fila_atendimento) and "Vermelho" in fila_atendimento[index]["prioridade"]:
            index += 1
        fila_atendimento.insert(index, paciente)
    elif "Amarelo" in prioridade:
        index = 0
        while index < len(fila_atendimento) and "Verde" not in fila_atendimento[index]["prioridade"]:
            index += 1
        fila_atendimento.insert(index, paciente)
    else:
        fila_atendimento.append(paciente)

def registar_paciente():
    print("\n--- NOVO REGISTO DE TRIAGEM ---")
    nome = input("Nome do paciente: ").strip()
    idade = ler_inteiro("Idade: ", 0, 120)
    print("\nNível de Dor (0 a 10):")
    dor = ler_inteiro("Digite o nível de dor: ", 0, 10)
    while True:
        try:
            febre = float(input("Temperatura corporal (°C) [ex: 37.5]: ").replace(',', '.'))
            break
        except ValueError:
            print("Erro: Digite um valor numérico válido para a temperatura.")
    prioridade = classificar_prioridade(dor, febre)
    paciente = {"nome": nome, "idade": idade, "dor": dor, "febre": febre, "prioridade": prioridade}
    adicionar_com_prioridade(paciente)
    historico_pacientes.append(paciente)
    print(f"\n[Sucesso] Paciente {nome} registado com classificação: {prioridade}")

def chamar_proximo():
    if len(fila_atendimento) == 0:
        print("\n[Aviso] A fila de atendimento está vazia!")
    else:
        paciente_chamado = fila_atendimento.pop(0)
        print(f"\n--> A CHAMAR PARA O CONSULTÓRIO: {paciente_chamado['nome']} ({paciente_chamado['prioridade']})")

def mostrar_fila():
    if len(fila_atendimento) == 0:
        print("\n[Aviso] Não há pacientes em espera.")
        return
    print("\n--- FILA DE ESPERA ATUAL (ORDENADA POR GRAVIDADE) ---")
    for i, p in enumerate(fila_atendimento, 1):
        print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Prioridade: {p['prioridade']}")

def main():
    while True:
        print("\n===============================")
        print("    SISTEMA DE TRIAGEM - HOSPITAL")
        print("===============================")
        print("1. Registar e Triar Paciente")
        print("2. Chamar Próximo Paciente (Fila)")
        print("3. Ver Fila de Espera")
        print("4. Sair")
        opcao = ler_inteiro("Escolha uma opção (1-4): ", 1, 4)
        if opcao == 1:
            registar_paciente()
        elif opcao == 2:
            chamar_proximo()
        elif opcao == 3:
            mostrar_fila()
        elif opcao == 4:
            print("\nA encerar o sistema. Até breve!")
            break

if __name__ == "__main__":
    main()


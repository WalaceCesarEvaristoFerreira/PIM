import json
import os

ARQUIVO_RESULTADOS = 'resultados.json'

perguntas = [
    {
        "pergunta": "O que significa 'int' em Python?",
        "opcoes": ["1. Número decimal", "2. Número inteiro", "3. Texto", "4. Lista"],
        "resposta": 2
    },
    {
        "pergunta": "Qual a função para imprimir algo na tela?",
        "opcoes": ["1. input()", "2. print()", "3. output()", "4. echo()"],
        "resposta": 2
    },
    {
        "pergunta": "Como se inicia um loop 'for' em Python?",
        "opcoes": ["1. for i até 10", "2. loop(i)", "3. for i in range(10):", "4. repetir 10 vezes"],
        "resposta": 3
    }
]

def carregar_resultados():
    if os.path.exists(ARQUIVO_RESULTADOS):
        with open(ARQUIVO_RESULTADOS, 'r') as f:
            return json.load(f)
    return []

def salvar_resultados(dados):
    with open(ARQUIVO_RESULTADOS, 'w') as f:
        json.dump(dados, f, indent=4)

def aplicar_quiz():
    nome = input("Digite seu nome: ")
    pontuacao = 0

    print("\nInício do Quiz!\n")
    for i, p in enumerate(perguntas, 1):
        print(f"{i}) {p['pergunta']}")
        for opcao in p['opcoes']:
            print(opcao)
        try:
            resposta = int(input("Sua resposta (1-4): "))
            if resposta == p['resposta']:
                pontuacao += 1
                print("✅ Correto!\n")
            else:
                print("❌ Errado.\n")
        except ValueError:
            print("Resposta inválida. Contando como errada.\n")

    print(f"Quiz concluído! {nome}, sua pontuação foi: {pontuacao}/{len(perguntas)}")

    # Salvar resultado
    resultados = carregar_resultados()
    resultados.append({"nome": nome, "pontuacao": pontuacao})
    salvar_resultados(resultados)

def mostrar_ranking():
    resultados = carregar_resultados()
    if not resultados:
        print("Nenhum resultado ainda.")
        return

    print("\n--- Ranking ---")
    ordenado = sorted(resultados, key=lambda x: x['pontuacao'], reverse=True)
    for i, r in enumerate(ordenado, 1):
        print(f"{i}. {r['nome']} - {r['pontuacao']} pontos")

def main():
    while True:
        print("\nMenu:")
        print("1. Fazer quiz")
        print("2. Ver ranking")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            aplicar_quiz()
        elif escolha == '2':
            mostrar_ranking()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

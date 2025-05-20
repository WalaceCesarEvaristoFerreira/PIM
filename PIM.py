import json
import os
import time
import statistics
import matplotlib.pyplot as plt

ARQUIVO_DADOS = "dados_usuarios.json"

# Carrega os dados do JSON
def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)

# Salva os dados no JSON
def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# Ensina lógica de programação com perguntas simples
def ensinar_programacao():
    print("\n📘 Vamos praticar lógica de programação!")
    perguntas = [
        {
            "pergunta": "1. O que a instrução 'if' faz em Python?",
            "resposta": "verifica uma condição"
        },
        {
            "pergunta": "2. Qual o comando mais comum para repetir algo várias vezes? (for ou while?)",
            "resposta": "for"
        },
        {
            "pergunta": "3. Como chamamos uma coleção de itens em Python?",
            "resposta": "lista"
        }
    ]

    acertos = 0
    for p in perguntas:
        resp = input(p["pergunta"] + "\n> ").strip().lower()
        if resp in p["resposta"]:
            print("✅ Resposta correta!")
            acertos += 1
        else:
            print(f"❌ Resposta incorreta. A resposta certa era: {p['resposta']}")

    print(f"\nVocê acertou {acertos} de {len(perguntas)} perguntas.")
    return acertos

# Registra o usuário e salva o tempo de uso
def registrar_usuario():
    nome = input("Digite seu nome: ").strip()
    inicio = time.time()

    pontuacao = ensinar_programacao()

    fim = time.time()
    tempo_uso = round(fim - inicio, 2)

    usuario = {
        "nome": nome,
        "tempo_uso": tempo_uso,
        "pontuacao": pontuacao
    }

    dados = carregar_dados()
    dados.append(usuario)
    salvar_dados(dados)

    print(f"\nObrigado por participar, {nome}!")
    print(f"⏱ Tempo de uso: {tempo_uso} segundos | 🎯 Pontuação: {pontuacao}\n")

# Exibe estatísticas básicas e gráfico
def exibir_estatisticas():
    dados = carregar_dados()
    if not dados:
        print("⚠️ Nenhum dado disponível ainda.")
        return

    tempos = [u["tempo_uso"] for u in dados]

    media = round(statistics.mean(tempos), 2)
    mediana = round(statistics.median(tempos), 2)
    try:
        moda = round(statistics.mode(tempos), 2)
    except statistics.StatisticsError:
        moda = "Sem moda (valores únicos)"

    print("\n📊 Estatísticas de uso dos usuários:")
    print(f"🔹 Tempo médio: {media} segundos")
    print(f"🔹 Tempo mediano: {mediana} segundos")
    print(f"🔹 Tempo mais comum (moda): {moda}")

    nomes = [u["nome"] for u in dados]

    # Exibe gráfico
    plt.bar(nomes, tempos, color='skyblue')
    plt.title("Tempo de Uso por Usuário")
    plt.xlabel("Usuários")
    plt.ylabel("Tempo (segundos)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Menu principal em português
def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Fazer perguntas de programação")
        print("2. Ver estatísticas dos usuários")
        print("3. Sair do programa")

        escolha = input("Escolha uma opção (1, 2 ou 3): ")
        if escolha == "1":
            registrar_usuario()
        elif escolha == "2":
            exibir_estatisticas()
        elif escolha == "3":
            print("👋 Encerrando o programa. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()

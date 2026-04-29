from funcoes import (rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela)

cartela = {
    'regra_simples': {
        1: -1,
        2: -1,
        3: -1,
        4: -1,
        5: -1,
        6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

rodada = 0

while rodada < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    terminou_rodada = False

    while terminou_rodada == False:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        opcao = input()

        while opcao not in ["0", "1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == "3":
            if rerrolagens < 2:
                quantidade = len(dados_rolados)
                dados_rolados = rolar_dados(quantidade)
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            categoria = input()

            marcou = False

            while marcou == False:
                if categoria in cartela['regra_avancada']:
                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                        categoria = input()
                    else:
                        todos_os_dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(todos_os_dados, categoria, cartela)
                        marcou = True
                        terminou_rodada = True

                elif categoria in ["1", "2", "3", "4", "5", "6"]:
                    categoria_int = int(categoria)

                    if cartela['regra_simples'][categoria_int] != -1:
                        print("Essa combinação já foi utilizada.")
                        categoria = input()
                    else:
                        todos_os_dados = dados_rolados + dados_guardados
                        cartela = faz_jogada(todos_os_dados, categoria, cartela)
                        marcou = True
                        terminou_rodada = True

                else:
                    print("Combinação inválida. Tente novamente.")
                    categoria = input()

    rodada += 1

pontuacao = 0

for chave in cartela['regra_simples']:
    pontuacao += cartela['regra_simples'][chave]

for chave in cartela['regra_avancada']:
    pontuacao += cartela['regra_avancada'][chave]

soma_simples = 0

for chave in cartela['regra_simples']:
    soma_simples += cartela['regra_simples'][chave]

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")


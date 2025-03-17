import os
import time
pontuacao=0
medalhas=0
erros=0

nome = (input("Digite seu nome:"))
print(f"Ok {nome}, Vamos começar")

print("\033[35mPergunta 1\033[m")
print("\033[35mComo são causados os terremotos?\033[m")
A = print("Opção A: O leviatãn decide se mexer\033")
B = print("Opção B: A cratera causada pelos meteoros que cairam na terra afunda um pouco\033")
C = print("Opção C: O manto terrestre se movimenta\033")
D = print("Opção D: As placas tectônicas se movimentam lenta e sucessivamente sobre uma camada de rocha.\033")

while True:
    print("Lembre-se se enviar sua resposta em letra MAIUSCULA")
    pergunta1 = str(input("Qual das alternativas acima está correta?"))
    rpcerta1 = D
    if pergunta1 == "D":
        pontuacao+=1
    resposta = (f"\033[36;32mA resposta está certa, você ganhou 1 ponto, você possui {pontuacao} Ponto\033[m")
    if pergunta1 == "D":
        print(resposta)
        break
    else:
        os.system("cls")
        print("\033[35m A resposta está errada, tente novamente\033[m")
        erros+=1
        print("\033[92mComo são causados os terremotos?\033[m")
        A = print("Opção A: O leviatãn decide se mexer\033")
        B = print("Opção B: A cratera causada pelos meteoros que cairam na terra afunda um pouco\033")
        C = print("Opção C: O manto terrestre se movimenta\033")
        D = print("Opção D: As placas tectônicas se movimentam lenta e sucessivamente sobre uma camada de rocha.\033")


if pergunta1 == "D":
    print("\033[35mPergunta 2\033[m")
    print("Próxima pergunta em 1")
    time.sleep(1)
    print("Próxima pergunta em 2")
    time.sleep(1)
    print("Próxima pergunta em 3")
    time.sleep(1)
    os.system("cls")

continuacao0 = (input("\033[31mDeseja continuar? Sim ou Não:\033[m"))
if continuacao0 == "Sim":
    print("\033[35mPergunta 2\033[m")
    print("Próxima pergunta em 1")
    time.sleep(1)
    print("Próxima pergunta em 2")
    time.sleep(1)
    print("Próxima pergunta em 3")
    time.sleep(1)
    os.system("cls")
    print("\033[35mPergunta 2\033[m")
    print("\033[35mA escola de Paraqui organizou uma Olimpíada de Matemática para seus 250 alunos e premiou com medalhas os 8% que obtiveram as notas mais altas. Quantas medalhas foram distribuídas?\033[m")
    A = print("Opção A: 8\033")
    B = print("Opção B: 11\033")
    C = print("Opção C: 14\033")
    D = print("Opção D: 20\033")

    while True:
        print("Lembre-se de enviar sua resposta em letra MAIUSCULA")
        pergunta2 = str(input("Qual das alternativas acima está correta?"))
        rpcerta2 = C
        if pergunta2 == "C":
            pontuacao+=1
            resposta2 = (f"\033[36;32mA resposta está certa, você ganhou 1 ponto, você possui {pontuacao} Pontos\033[m")
            print(resposta2)
            break
        else:
            os.system("cls")
            print("Repetindo pergunta...")
            time.sleep(2)
            print("\033[35mQual foi a motivação ta 1° guerra mundial?\033[m")
            A = print("Opção A: O assassinato do arquiduque Francisco Ferdinando, herdeiro do trono austríaco, e sua esposa no dia 28 de junho de 1914.\033")
            B = print("Opção B: Foi uma consequência da grande expansão de crédito por meio de oferta monetária.\033")
            C = print("Opção C: A divisão do país em duas zonas com governos ideologicamente distintos em 1945 e a invasão do sul promovida pelas tropas do norte em junho de 1950.\033")
            D = print("Opção D: A primeira grande guerra, a economia, o descontentamento e a desorganização do aparato estatal russo.\033")
            print("\033[0;31m A resposta está errada, tente novamente!\033[m")
            erros+=1

time.sleep(3)
os.system("cls")
continuacao1 = (input("\033[31mDeseja continuar? Sim ou Não:\033[m"))
if continuacao1 == "Sim":
    print("\033[35mPergunta 3\033[m")
    print("Próxima pergunta em 1")
    time.sleep(1)
    print("Próxima pergunta em 2")
    time.sleep(1)
    print("Próxima pergunta em 3")
    time.sleep(1)
    os.system("cls")
    print("\033[35mPergunta 3\033[m")
    print("\033[35mAs redes de alta tensão para transmissão de energia elétrica geram campo magnético variável o suficiente para induzir corrente elétrica no arame das cercas. Tanto os animais quanto os funcionários das propriedades rurais ou das concessionárias de energia devem ter muito cuidado ao se aproximarem de uma cerca quando esta estiver próxima a uma rede de alta tensão, pois, se tocarem no arame da cerca, poderão sofrer choque elétrico.\033[m")
    A = print("Opção A:  Fazer o aterramento dos arames da cerca.\033")
    B = print("Opção B: Acrescentar fusível de segurança na cerca.\033")
    C = print("Opção C: Realizar o aterramento da rede de alta tensão.\033")
    D = print("Opção D: Instalar fusível de segurança na rede de alta tensão.\033")
    while True:
        print("Lembre-se de enviar sua resposta em letra MAIUSCULA")
        pergunta3 = str(input("Qual das alternativas acima está correta?"))
        rpcerta3 = D
        if pergunta3 == "D":
            pontuacao+=1
            resposta3 = (f"\033[36;32mA resposta está certa, você ganhou 1 ponto, você possui {pontuacao} Pontos\033[m")
            print(resposta3)
            time.sleep(2)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Repetindo a pergunta...")
            time.sleep(2)
            os.system("cls")
            print("\033[mQual foi a motivação ta 1° guerra mundial?\033[m")
            A = print("Opção A: O assassinato do arquiduque Francisco Ferdinando, herdeiro do trono austríaco, e sua esposa no dia 28 de junho de 1914.\033")
            B = print("Opção B: Foi uma consequência da grande expansão de crédito por meio de oferta monetária.\033")
            C = print("Opção C: A divisão do país em duas zonas com governos ideologicamente distintos em 1945 e a invasão do sul promovida pelas tropas do norte em junho de 1950.\033")
            D = print("Opção D: A primeira grande guerra, a economia, o descontentamento e a desorganização do aparato estatal russo.\033")
            print("\033[0;31m A resposta está errada, tente novamente!\033[m")
            erros+=1
            os.system("cls")


else:
    print("Até a próxima")
    time.sleep(2)
    os.system("cls")

continuacao2 = (input("\033[31mDeseja continuar? Sim ou Não:\033[m"))
if continuacao2 == "Sim":
    print("\033[35mPergunta 4\033[m")
    print("Próxima pergunta em 1")
    time.sleep(1)
    print("Próxima pergunta em 2")
    time.sleep(1)
    print("Próxima pergunta em 3")
    time.sleep(1)
    os.system("cls")
    print("\033[35mPergunta 4\033[m")
    print("\033[35mQual foi a motivação ta 1° guerra mundial?\033[m")
    A = print("Opção A: O assassinato do arquiduque Francisco Ferdinando, herdeiro do trono austríaco, e sua esposa no dia 28 de junho de 1914.\033")
    B = print("Opção B: Foi uma consequência da grande expansão de crédito por meio de oferta monetária.\033")
    C = print("Opção C: A divisão do país em duas zonas com governos ideologicamente distintos em 1945 e a invasão do sul promovida pelas tropas do norte em junho de 1950.\033")
    D = print("Opção D: A primeira grande guerra, a economia, o descontentamento e a desorganização do aparato estatal russo.\033")
    while True:
        print("Lembre-se de enviar sua resposta em letra MAIUSCULA")
        pergunta3 = str(input("Qual das alternativas acima está correta?"))
        rpcerta3 = D
        if pergunta3 == "D":
            pontuacao+=1
            resposta3 = (f"\033[36;32mA resposta está certa, você ganhou 1 ponto, você possui {pontuacao} Pontos\033[m")
            print(resposta3)
            time.sleep(2)
            os.system("cls")
            break
        else:
            os.system("cls")
            print("Repetindo a pergunta...")
            time.sleep(2)
            os.system("cls")
            print("\033[mQual foi a motivação ta 1° guerra mundial?\033[m")
            A = print("Opção A: O assassinato do arquiduque Francisco Ferdinando, herdeiro do trono austríaco, e sua esposa no dia 28 de junho de 1914.\033")
            B = print("Opção B: Foi uma consequência da grande expansão de crédito por meio de oferta monetária.\033")
            C = print("Opção C: A divisão do país em duas zonas com governos ideologicamente distintos em 1945 e a invasão do sul promovida pelas tropas do norte em junho de 1950.\033")
            D = print("Opção D: A primeira grande guerra, a economia, o descontentamento e a desorganização do aparato estatal russo.\033")
            print("\033[0;31m A resposta está errada, tente novamente!\033[m")
            erros+=1
            os.system("cls")


else:
    print("Até a próxima")
    time.sleep(2)
    os.system("cls")




class acertos:
    def __init__(self, acertos, erros):
        self.acertos = acertos
        self.erros = erros
        pass

usuario = acertos(f"{pontuacao}", f"{erros}")
print(f"O usuario {nome} teve {usuario.acertos} acertos e {usuario.erros} erros")

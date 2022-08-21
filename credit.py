def somarNumerosCartao(digitosDoCartaoInvertidos):
    numerosSomados = 0

    listaNumerosDeIndiceImparParMultiplicados = []
    listaNumerosDeIndiceImparMultiplicadosString = ""

    listanumerosDeIndicePar = []
    listanumerosDeIndiceParString = ""

    for digitoCartao in range(1, len(digitosDoCartaoInvertidos), 2):
        numeroMultiplicado = digitosDoCartaoInvertidos[digitoCartao]*2
        listaNumerosDeIndiceImparParMultiplicados.append(numeroMultiplicado)

    for digitoCartao in range(0, len(digitosDoCartaoInvertidos), 2):
        listanumerosDeIndicePar.append(digitosDoCartaoInvertidos[digitoCartao])

    for digitoCartao in listaNumerosDeIndiceImparParMultiplicados:
        listaNumerosDeIndiceImparMultiplicadosString += str(digitoCartao)

    for digitoCartao in listanumerosDeIndicePar:
        listanumerosDeIndiceParString += str(digitoCartao)

    digitosNumerosIndiceImparAposMultiplicacao = list(map(int, listaNumerosDeIndiceImparMultiplicadosString))

    digitosNumerosIndicePar = list(map(int, listanumerosDeIndiceParString))

    for x in digitosNumerosIndiceImparAposMultiplicacao:
        numerosSomados += x

    for x in digitosNumerosIndicePar:
        numerosSomados += x

    return numerosSomados

def verificarExistenciaCartao(resultadoSomaDigitosCartao):
    if resultadoSomaDigitosCartao % 10 == 0:
        return True
    else:
        return False

def verificarBandeiraCartao(numeroDoCartao):
    numeroDoCartaoString = str(numeroDoCartao)

    if numeroDoCartaoString.startswith("4"):
        return "VISA"
    if numeroDoCartaoString.startswith("51") or numeroDoCartaoString.startswith("52") or numeroDoCartaoString.startswith("53") or numeroDoCartaoString.startswith("54") or numeroDoCartaoString.startswith("55"):
        return "MASTERCARD"
    if numeroDoCartaoString.startswith("34") or str(cartao).startswith("37"):
        return "AMEX"


if __name__ == '__main__':
    cartao = int(input("Digite um número de cartão de crédito: "))

    digitosCartao = [int(digito) for digito in str(cartao)]
    digitosCartao.reverse()

    resultadoSomaDigitosCartao = somarNumerosCartao(digitosCartao)

    cartaoValido = verificarExistenciaCartao(resultadoSomaDigitosCartao)

    if not cartaoValido:
        print("INVÁLIDO")
    else:
        print(verificarBandeiraCartao(cartao))













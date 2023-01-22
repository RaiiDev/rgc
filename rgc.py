import random
import pyluhn

print('''
//....................................................................
//.RRRRRRRRRRRRRRRRR..........GGGGGGGGGGG............CCCCCCCCCCC......
//.RRRRRRRRRRRRRRRRRR........GGGGGGGGGGGGGG........CCCCCCCCCCCCCC.....
//.RRRRRRRRRRRRRRRRRRR.....GGGGGGGGGGGGGGGGG......CCCCCCCCCCCCCCCC....
//.RRRRRRRRRRRRRRRRRRR.....GGGGGGGGGGGGGGGGGG.....CCCCCCCCCCCCCCCCC...
//.RRRRRR.....RRRRRRRR....GGGGGGGGG.GGGGGGGGG....CCCCCCCCC.CCCCCCCC...
//.RRRRRR.......RRRRRR...GGGGGGGG.....GGGGGGG...CCCCCCCC.....CCCCCCC..
//.RRRRRR.......RRRRRR...GGGGGGG.......GGGGGGG..CCCCCCC.......CCCCC...
//.RRRRRR.......RRRRRR...GGGGGG.........GGGGG...CCCCCC................
//.RRRRRR.....RRRRRRRR...GGGGGG.................CCCCCC................
//.RRRRRRRRRRRRRRRRRRR..RGGGGGG.................CCCCCC................
//.RRRRRRRRRRRRRRRRRR...RGGGGG.....GGGGGGGGGGG..CCCCCC................
//.RRRRRRRRRRRRRRRRR....RGGGGG.....GGGGGGGGGGG..CCCCCC................
//.RRRRRRRRRRRRRRR......RGGGGGG....GGGGGGGGGGG..CCCCCC................
//.RRRRRR.RRRRRRRRR......GGGGGG....GGGGGGGGGGG..CCCCCC........CCCCCC..
//.RRRRRR...RRRRRRRR.....GGGGGG.........GGGGGG..CCCCCC........CCCCCC..
//.RRRRRR....RRRRRRR.....GGGGGGG........GGGGGG..CCCCCCC......CCCCCCC..
//.RRRRRR.....RRRRRRR....GGGGGGGG......GGGGGGG..CCCCCCCC....CCCCCCC...
//.RRRRRR.....RRRRRRRR....GGGGGGGGG.GGGGGGGGGG...CCCCCCCCCCCCCCCCCC...
//.RRRRRR......RRRRRRR.....GGGGGGGGGGGGGGGGGGG....CCCCCCCCCCCCCCCC....
//.RRRRRR.......RRRRRRR....GGGGGGGGGGGGGGGGGG.....CCCCCCCCCCCCCCCC....
//.RRRRRR.......RRRRRRRR.....GGGGGGGGGGGGGGG.......CCCCCCCCCCCCCC.....
//.RRRRRR........RRRRRRR......GGGGGGGGGGGG...........CCCCCCCCCC.......
//....................................................................
//========================BY:Rai  VER:0.1===========================..
    ''')

bin_code = input("Insira o código BIN: ")
if len(bin_code) != 6:
    print("O código BIN deve ter 6 dígitos.")
    exit()

numero_cartoes = int(input("Insira o número de cartões a serem gerados: "))

card_numbers = []

def calculate_luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def gera_numero_cartao(bin_code):
    numero_cartao = bin_code
    for i in range(9):
        numero_cartao += str(random.randint(0, 9))
    check_digit = calculate_luhn(numero_cartao)
    numero_cartao += str(check_digit)
    data_validade_ano = str(random.randint(2023, 2025))
    data_validade_mes = str(random.randint(1, 12)).zfill(2)
    cvv = str(random.randint(100, 999))
    if numero_cartao in card_numbers:
        return "Número já existente"
    card_numbers.append(numero_cartao)
    return numero_cartao + "|" + data_validade_mes + "|" + data_validade_ano + "|" + cvv

for i in range(numero_cartoes):
    print(gera_numero_cartao(bin_code))
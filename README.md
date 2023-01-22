# RGC 🔐

Este código é uma implementação simples em Python para gerar números de cartão de crédito válidos. Ele pede ao usuário para inserir um código BIN (os primeiros 6 dígitos de um número de cartão de crédito), e o número de cartões a serem gerados. Em seguida, ele usa a biblioteca random para gerar os números restantes do cartão, data de validade e CVV aleatoriamente. Ele usa também uma função 'calculate_luhn' para calcular o dígito verificador de acordo com o algoritmo de Luhn. Todos os dados gerados são concatenados e separados por '|' e imprimidos na tela.
Lembre-se de que esses números gerados nunca devem ser usados para transações reais.

![Screenshot_20230122-205152_Termux](https://user-images.githubusercontent.com/123031683/213947301-871d1b1f-3550-436b-93f7-49a8541430b3.jpg)

<h1>Comandos TERMUX 📚</h1>

$ pkg update

$ pkg install python3

$ pkg install git

$ pip install pyluhn

$ git clone https://github.com/RaiiDev/rgc

$ python3 rgc.py

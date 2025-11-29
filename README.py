def cardapio():
    print('='*60)
    print('-'*13 + 'Bem vindo a Pizzaria do Igor Pires'+'-'*13)
    print('='*60)
    print('-'*16 + 'Igor Aparecido Marque Pires '+'-'*16)
    print('-'*8 +'|' 'Tamanho'+'|'+'Pizza Salgada (PS)'+'|'+'Pizza Doce (PD)'+'|'+'-'*8)
    print('-'*8 +'|' '   P   '+'|'+'   R$ 30,00       '+'|'+'   R$ 34,00    '+'|'+'-'*8)
    print('-'*8 +'|' '   M   '+'|'+'   R$ 45,00       '+'|'+'   R$ 48,00    '+'|'+'-'*8)
    print('-'*8 +'|' '   G   '+'|'+'   R$ 60,00       '+'|'+'   R$ 66,00    '+'|'+'-'*8)
    print('='*60)

cardapio()
pedidos= []
#Essa lista armazena os pedidos ja feitos

#total é o acumulador, ele retem todos os valores somados
total = 0
pedido_extra = 'S'
#a variavel pedido extra faz o loop abaixo resetar, então quando a pessoa diz 'S' no final do loop ela volta pro while que esta abaixo
while pedido_extra.upper() == 'S':
#2 loops, while true esta dentro do loop do pedido extra
    while True:
        
        sabor = input('Entre com o sabor desejado: (PS/PD) ').upper ()
        #variavel do sabor, que retem o PS e PD

        if sabor == 'PS':
            #criei um if para o PS ou PD e um if dentro do if para definir o tamanho, os tamanhos ficam por conta da resposta a variavel 'tamanho'
            print('Você escolheu Pizza Salgada')
            tamanho = input('Escolha um tamanho: (P/M/G)').upper ()
            if tamanho == 'P':
                print('Você escolheu uma Pizza Salgada Pequena')
                total += 30.00
                pedidos.append("Pizza Salgada - Tamanho P")
                break
            elif tamanho == 'M':
                print('Você escolheu uma Pizza Salgada Média')
                total += 45.00
                pedidos.append("Pizza Salgada - Tamanho M")
                break

            elif tamanho == 'G':
                print('Você escolheu uma Pizza Salgada Grande')
                total += 60.00
                pedidos.append("Pizza Salgada - Tamanho G")
                break
            else:
                print('Tamanho invalido, digite um tamanho valido')
                continue
            #o continue aqui reseta o loop
        
        elif sabor == 'PD':
            #PD age da mesma forma que PS
            print('Você escolheu Pizza Doce')
            tamanho = input('Escolha um tamanho: (P/M/G)').upper ()
            if tamanho == 'P':
                print('Você escolheu uma Pizza Doce Pequena')
                total += 34.00
                pedidos.append("Pizza Doce - Tamanho P")
                break
            elif tamanho == 'M':
                print('Você escolheu uma Pizza Doce Média')
                total += 48.00
                pedidos.append("Pizza Doce - Tamanho M")
                break

            elif tamanho == 'G':
                print('Você escolheu uma Pizza Doce Grande')
                total += 66.00
                pedidos.append("Pizza Doce - Tamanho G")
                break
            else:
                print('Tamanho invalido, digite um tamanho valido')
                continue
        else:
            print('Sabor invalido, digite um sabor valido')
    #Esse print mostra um subtotal a cada compra pro cliente saber quanto esta gastando, como se fosse um 'carrinho'
    print('-'*20,'Itens no Carrinho:','-'*20)
    #aqui ele printa a lista de pedidos e na sequencia o subtotal
    for item in pedidos:
        print('-', item)
        
    print('-'*60)
    print(f'Seu subtotal até o momento é de R${total:.2f}')
    print('-'*60)
    #Aqui ele pergunta se quer continuar
    pedido_extra = input('Deseja mais alguma coisa? (S/N)').upper ()
#Aqui encerra o loop e mostra quanto o cliente deve pagar
print(f'O valor total a ser pago é de R${total:.2f}')

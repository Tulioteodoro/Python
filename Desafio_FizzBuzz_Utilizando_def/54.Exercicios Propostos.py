""
"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
# def funcao(saudacao,nome):
#     print(f'{saudacao} {nome}')
#
# funcao ('Olá', 'Túlio')
"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
#
# def soma(n1,n2,n3):
#     print(n1 + n2 +n3)
#
# soma(2,1,3)
# soma(1,5,4)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (Ex: 10%). 
Retorne (return) o valor do primeiro número somando do aumento do percentual do mesmo.
"""
# def aumento_percentual (valor,percentual):
#     return valor + (valor * percentual/100)
#
# ap = aumento_percentual(100,20)
# print(ap)
# ap = aumento_percentual(50,10)
# print(ap)
# ap = aumento_percentual(200,50)
# print(ap)


"""
4 - Fizz Buzz - Se o parâmetro da função por dividível por 2, retorne fizz, se o parâmetro da função for
dividível por 5, retorne buzz. Se o parâmetro da função for dividível por 5 e por 3, retorne FizzBuzz, caso
contrário, retorne o número enviado.
"""

# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'fizzbuzz'
#     elif n % 3 == 0:
#         return 'fizz'
#     elif n % 5 == 0:
#         return 'buzz'
#     else:
#         return n
# print(fb(5))
# print(fb(3))
# print(fb(15))
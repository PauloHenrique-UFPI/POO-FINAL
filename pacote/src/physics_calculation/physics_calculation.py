import math

class physics_calculation():
    """ Conjunto de funções para calculos de equações do ramo de Fisica

    Paramentros
    --------------
    Não possui, os parametros são exclusivos de cada função onde cada
    função tem seus parametros.

    """

    def velocidade_media(s : float, t : float) -> float:
        """
        s : float, obrigatória
            's' representa a variação de espaço 
        t : flota, obrigatória
            't' representa a variação de tempo.

        retorno : float
            retorna a velocidade media do objeto observado
        """
        print('\nA velocidade do corpo é definida pela relação do seu deslocamento em')
        print('determinado período de tempo, onde a formula da velocidade média é: Vm = S/T')
        resultado = s/t
        print('\tVm = {} / {} -->  {} = {} / {}'.format(s,t,resultado,s,t))
        return resultado


    def segunda_lei_newton(m : float, a : float) -> float:
        """
        m : float, obrigatória
            representa a massa do objeto
        a : 
            representa a aceleração 

        retorno : float
            retorna o resultado do calculo da segunda lei de newton
        """
        print('\nA segunda Lei de newton, trata de que para que um objeto mude seu estado de movimento')
        print('será nescessario uma força resultante da massa do objeto e da aceleração por ele')
        print('adquirida, essa relação pode ser definida pela formula Fr = m * a, onde (M) é a massa ')
        print('e (A) seria a aceleração')
        resultado = m*a
        print('\n\t Fr = {} * {}     -->    {} = {} * {}\n'.format(m,a,resultado,m,a))
        return resultado

    def equacao_1_grau_1(a : float, b : float, c : float, operacao : str) -> float:
        print('\n1º passo definir qual operação esta sendo realizada')
        if operacao == '-':
            print('operação de subtração, logo a estrutura da formula seria: Ax - B = C, substituindo')
            print('\t {}x - {} = {}  -->  {}x = {} + {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c+b
            print('\t-> x = {}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(parte1, a))
            resultado = parte1/a
        elif operacao == '+':
            print('operação de soma, logo a estrutura da formula seria: Ax + B = C, substituindo')
            print('\t {}x + {} = {}  -->  {}x = {} - {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c-b
            print('\t-> x = {}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(parte1, a))
            resultado = parte1/a
        elif operacao == '*':
            print('operação de multiplicacao, logo a estrutura da formula seria: Ax * B = C, substituindo')
            print('\t {}x * {} = {}  -->  {}x = {} / {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c/b
            print('\t-> x = {}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(int(parte1), a))
            resultado = parte1/a
        
        return resultado

    def equacao_2_grau(a : float , b : float, c : float):
        """
        a : float, obrigatória
            representa o ponto 'a' da equação
        b : 
            representa o ponto 'b' da equação
        c: float, obrigatória
            representa o ponto 'c' da equação

        retorno : lista de float
            retorna os valores de x1 e x2 onde x1 esta na primeira posição da lista e x2 na segunda posição
        """
        print('\nPrimeiro passo monte a equacao: {}x² + {}x + {} = 0'.format(a,b,c))
        print('\nSegundo passo calcule o valor de DELTA: DELTA = b²-4.a.c \n\t DELTA = {}²-4.{}.{}'.format(b,a,c))
        D = (b*b) - 4*a*c
        if D < 0:
            print('DELTA e um numero negativo logo o resultado nao pertence ao conjunto de numeros reais!')
        else:
            print("\nTerceiro passo calcule os valores ''x'' da equacao:")
            print('temos a formula de bhaskara: -b +- RAIZ(DELTA)')
            print('                              ----------------')
            print('                                      2.a')
            print('\nsubstituindo por numeros temos: -{} +- RAIZ({})'.format(b,D))
            print('                                 ---------------')
            print('                                       2.{}'.format(a))
            print('\n\npara DELTA negativo temos:    -{} - RAIZ({})'.format(b,D))
            print('                                -----------------')
            print('                                       2.{}'.format(a))
            x1 = (-b - (D**0.5))/(2*a)
            print("resultado 'x1' linha = {}".format(x1))
            print('\n\npara DELTA positivo temos:    -{} + RAIZ({})'.format(b,D))
            print('                                 ----------------')
            print('                                       2.{}'.format(a))
            x2 = (-b + (D**0.5))/(2*a)
            print("resultado 'x2' linha = {}".format(x2))

            x = [x1, x2]

            return x

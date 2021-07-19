class IPcalculation():
    """ Conjunto de funções para calculos de equações do ramo de Fisica

    Paramentros
    --------------
    Não possui, os parametros são exclusivos de cada função onde cada
    função tem seus parametros.

    """
    def juros_composto(C: float, I: float, T: int):
        """
        C : float, obrigatória
            'C' representa o capital inicial
        I : float, obrigatória
            'I' representa a taxa de juros acrecentada
        T : int, obrigatória
            'T' representa a quantidade de vezes que esse juros ocorreu (parcelas)

        retorno : float
            retorna o montante final, valor total a ser pago
        """
        print("\n O juros composto é calculado de forma que cada parcela contem o valor do capital")
        print(' mais um taxa, onde essa taxa é calculada 1 mais a poncentagem do juros, onde o resultado é')
        print(' elevado ao número da parcela atual\n')
        print('\n O montante será a soma de todas as parcelas')
        m=0
        aux=0
        I = I/100
        for x in range(T):
            m = m + (C*(1+I)**(x+1))
            aux = (C*(1+I)**(x+1))
            print('M = C + (1+I)^t ---- {:.2f} = {} * (1+{})^{}'.format(aux,C,I,x+1))
        m = '{:.2f}'.format(m)
        print('Montante final: {}'.format(m))
        return m
    
    def pressao(v : float, n : float, r : float, t : float):
        """
        v : float, obrigatória
            volume
        n : float, obrigatória
            numero de mols
        r : float, obrigatória
            constante dos gases perfeitos
        t : float, obrigatória
            temperatura

        retorno:
            retorna o Pressão do calculo de pressão

        """
        print('Para o cálculo da pressão de líquidos e gases, usamos a seguinte fórmula:')
        print('formula: P * v = n * R * T')
        resultado = n * r * t
        print('\n\t P*{} = {} ---> P = {}/{}'.format(v,resultado,resultado,v))
        return resultado/v

    def progrecao_arit(primeiro : int , razao : int , n : int):
        """
        primeiro : inteiro, obrigatória
            primeiro termo da P.A
        razao : inteiro, obrigatória
            razao dos numeros
        n : inteiro, obrigatória
            posição do termo que queremos descobrir

        retorno: 
            retorna uma lista com a sequencia gerada
        """
        print('A Progressão Aritmética (P.A.) é uma sequência de números onde')
        print('a diferença entre dois termos consecutivos é sempre a mesma.')
        print('formula:  an = a1+(n-1)*r')
        ultimo = primeiro + (n-1)*razao
        ultimo = ultimo + 1
        vet = []
        print('\nsequencia gerada pela formula:')
        for var in range(primeiro, ultimo, razao):
            vet.append(var)
            print(var)
        
        return vet



    def calorimetria(m : float, c : float, D0 : float):
        """
        m : float, obrigatória
            massa do corpo
        c : float, obrigatória
            calor específico da substância
        D0 : float, obrigatória
            variação de temperatura

        retorno:
            retorna a quantidade de calor sensível
        """
        print('A calorimetria é a parte da física que estuda')
        print('os fenômenos recorrentes da transferência da energia')
        print('que chamamos de “calor”. A fórmula principal da')
        print('calorimetria é a que calcula a quantidade total de')
        print('calor em um corpo.')
        print('formula: Q = m * c * D0')
        resultado = m*c*D0
        print('\n\t Q = {} * {} * {} --> Q = {}'.format(m,v,D0,resultado))
        return resultado
    
    def teorema_pitagoras(b : float, c : float):
        """
        b : float, obrigatória
            representa o valor do cateto oposto

        c : float, obrigatória
            representa o valor do cateto adjacente

        retorno
            retorna o valor da hipotenusa
        """
        print('O teorema de Pitágoras diz que o quadrado da hipotenusa')
        print('é igual à soma dos quadrados dos catetos.')
        print('formula: a² = b² + c²')
        print('\n\t a² = {}²+{}², primeiro e definida os valores em suas posicoes')
        resultado = (b*b) + (c*c)
        print('\t a = RAIZ({})'.format(resultado))
        resultado = resultado*0.5
        print('\t a = {}'.format(resultado))

        return resultado

    def movimento_r_uniforme(so : float, v : float, t : float):
        """
        so : float, obrigatória
            representa o espaço inicial
        v : float, obrigatória
            representa a velocidade
        t : float, obrigatória
            representa o tempo

        retorno:
            retorna o resultado do espaco final do objeto do MRU

        """
        print('Movimento Retilíneo Uniforme (MRU) como o movimento de um corpo móvel')
        print('em relação ao seu referencial que está em velocidade constante. Para calcular ')
        print('o espaço, o tempo ou a velocidade no MRU, utiliza-se a famosa equação sorvete.')
        print('formula:\t S = So + V * t')
        resultado = so + v*t
        print('\n\t S = {} + {} * {} ---->  S = {}'.format(so,v,t,resultado))

        return resultado

    def torricelli(v_inicial : float, a : float, s: float):
        """
        v_inicial : float, obrigatória
            representa a velocidade inicial
        a : float, obrigatória
            representa a aceleração
        s : float, obrigatória
            espaco percorrido pelo corpo

        retorno:
            retorna o resultado da velocidade final (da equação de torricelli)
        """
        print('equação de torriceli tem a função de encontrar a velocidade de um móvel')
        print('em movimento retilíneo uniforme (MRU) sem que o tempo seja conhecido')
        print('formula:\t v² = vo²+2*a*s')
        print('[vo] e a velocidade inicial (m/s)\n[a] aceleracao (m/s)\n[s]espaco percorrido pelo corpo (m)')
        resultado = (v_inicial*v_inicial) + 2*a*s
        resultado = resultado**0.5
        print('\n v² = {:.2f} + 2*{:.2f}*{:.2f} --> v² = {:.2}\n'.format(v_inicial,a,s,resultado))
        return resultado

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
    
    def equacao_1_grau_1(a : float, b : float, c : float, operacao : str) -> float:
        """
        a : float, obrigatória
            representa a icognita (numero)X,isto é, 'a'x
        b : float, obrigatória
            representa o termo numerico 'b' da expressão
        c : float, obrigatória
            rerpesenta o termo de resposta da expressão

        retorno : float
            retorna o termo 'x' de ax
        """
        print('\n1º passo definir qual operação esta sendo realizada')
        if operacao == '-':
            print('operação de subtração, logo a estrutura da formula seria: Ax - B = C, substituindo')
            print('\t {}x - {} = {}  -->  {}x = {} + {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c+b
            print('\t-> x = {:.2f}//{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(parte1, a))
            resultado = parte1/a
        elif operacao == '+':
            print('operação de soma, logo a estrutura da formula seria: Ax + B = C, substituindo')
            print('\t {}x + {} = {}  -->  {}x = {} - {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c-b
            print('\t-> x = {:.2f}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(parte1, a))
            resultado = parte1/a
        elif operacao == '*':
            print('operação de multiplicacao, logo a estrutura da formula seria: Ax * B = C, substituindo')
            print('\t {}x * {} = {}  -->  {}x = {} / {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c/b
            print('\t-> x = {:.2f}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(int(parte1), a))
            resultado = parte1/a
        elif operacao =='/':
            print('operação de divisão, logo a estrutura da formula seria: Ax / B = C, substituindo')
            print('\t {}x / {} = {}  -->  {}x = {} * {}, logo quem e incognitas ficam de um lado e os numeros do outro'.format(a,b,c,a,c,b))
            parte1 = c*b
            print('\t-> x = {:.2f}/{}, e feita a operação e o X e isolado, por fim e feito o calculo'.format(int(parte1), a))
            resultado = parte1/a
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

    def juros_simples(C: float, J: float, T: int):
        """
        C : float, obrigatória
            'C' representa o capital inicial
        J : float, obrigatória
            'J' representa a taxa de juros acrecentada
        T : int, obrigatória
            'T' representa a quantidade de vezes que esse juros ocorreu (parcelas)

        retorno : float
            retorna o montante final, valor total a ser pago
        """
        m=0
        aux=0
        print('\n O juros simples é calculador a partir do capital inicial, a taxa a ser acrecentada e quantidade de parcelas')
        print('\n O montante final sera o valor  total a ser pago, somando o valor de todas as parcelas: ')
        for x in range(T):
            aux = C + J
            m += aux
            print('M = C + J ----- {} = {} + {}  parcela {}'.format(aux,C,J,x+1))
        print('Montante final; {:.2f}'.format(m))
        return m
    
    def area_triangulo(H: float, B: float):
        """
        H : float, obrigatória
            'H' representa a altura do triângulo
        B : float, obrigatória
            'B' representa a base do triângulo

        retorno : float
            retorna a área total do triângulo
        """
        print('Para calcular a área do triângulo basta multiplicas a base vezes a altura e dividir o resultado por dois,')
        print(' e a medida final é a medida inicial ao quadrado. Ex: cm---cm^2')
        print('\nPara entender o porquê da divisão bas pensar que um quadrado, com a mesma base e altura, pode conter dois triãngulos igual')
        print('caso seja um triângulo retângulo, caso não, iremos obter três. Neste caso bataria colocar os dois menores lado a lado')
        print('assim obteriamos dois triângulos identicos dentro de um quadrado.')
        print('\nOu seja, a área do triângulo é a área de um quadrado com mesma base e altura, divido por dois.')
        area = (H*B)/2
        return area

    def area_retangulo(L: float, B: float):
        """
        H : float, obrigatória
            'H' representa a altura do retangulo
        B : float, obrigatória
            'B' representa a base do retangulo

        retorno : float
            retorna a área total do retangulo
        """
        print('\nPara calcular a área de um retangulo bas multiplicar a altura com o lado')
        print('\n, assim teremos sua área total.')
        print('\nA media final é a medida inicial ao quadrado. Ex: cm---cm^2.')
        area = L*B
        return area

    def area_circulo(R: float):
        """
        R : float, obrigatória
            'R' representa o raio do círculo

        retorno : float
            retorna a área total do círculo
        """
        print('\n Para calcular a área do círculo basta multiplicar Pi pelo quadrado do raio (A = 2*Pi*r^2).')
        print('\nA medida é dade de acordo com a medida do raio ao quadrado. Ex: cm-----cm^2')
        print('\n Na matemática, o número Pi é uma proporção numérica definida pela relação entre o perímetro de uma circunferência e seu diâmetro; por outras palavras, ')
        print(' se uma circunferência tem perímetro p e diâmetro d, então aquele número é igual a p/d. Dessa forma, ')
        print('\numa circunferência de diametro 1, o seu período é Pi. ')
        area = 2*3.14*R*R
        return area

    def velocidade_angular(T: float):
        """
        T : float, obrigatória
            'T' representa o tempo, em segundos, que o objeto demorou para percorer todo o círculo.

        retorno : float
            velocidade angular do objeto
        """
        print('\n A velocidade angular de um objeto ou partícula representa a velocidade com que um objeto faz um círculo')
        print(' perfeito envolta de um determinado ponto. ')
        print('\nA velocidade angular é dada a partir de duas vezes Pi dividido pelo tempo (Wm = 2*Pi/T).')
        print('A sua medida é dada em rad/s (radianos por segundo).')
        velocidade = 2*3,14/T
        return T
    
    def velocidade_tangencial(R: float, T: float):
        """
        R : float, obrigatória
            'R' representa o raio da circunferência
        T : float, obrigatória
            'T' representa o tempo, em segundos, que o objeto demorou para percorer todo o círculo.

        retorno : float
            velocidade tangencial do objeto
        """
        print('\n A velocidade angular de um objeto é a velocidade com que ele se movimenta ao redor de um ponto formando um círculo.')
        print(' Dessa forma, dois objetos que se movimentão, com raios diferentes, ao redor de um círculo teram velocidades diferentes.')
        print('\nIsso ocorre porque diferente da velocidade angular, a velocidade tangencial leva em consideração a distância do raio (V = Wm * r')
        print('\nSua medida é dada, geralmente, em metros por segundo (m/s).')
        velociade = 2*3.14*R/T
        return velociade

    def aceleração_centripeta(R: float, T: float):
        """
        R : float, obrigatória
            'R' representa o raio da circunferência
        T : float, obrigatória
            'T' representa o tempo, em segundos, que o objeto demorou para percorer todo o círculo.

        retorno : float
            aceleração centrípeta do objeto
        """
        print("\nA aceleração centrípeta de um objeto é a aceleração que ele teve se moveu ao redor de umponto formando um círculo.")
        print('\nA aceleração centrípeta é dada a partir da velocidade angular multiplicado pelo raio ao quadrado (a = Wm * r^2)')
        print('\nA sua medida é, geralmente, em metros por segundo (m/s).')
        a = 2*3,14/T
        a = a * R*R
        return a

    def aceleração(v_inicial: float, v_final: float, T):
        """
        v_inicial : float, obrigatória
            'v_inicial' representa a velocidade inicial do objeto
        v_final : float, obrigatória
            'v_final' representa a velocidade final do objeto
        T : float, obrigatória
            'T' representa o tempo, em segundos, que o objeto demorou para percorer todo o círculo.

        retorno : float
            aceleração do objeto
        """
        print('\nO calculo da aceleração serve para saber qual foi a aceleração de um determinado objeto.')
        print(' Ou até mesmo sua velocidade final, ou o tempo. Para isso basta inverter os membros da equação (a = (V-V0)/T).')
        print('\nSua medida irá considerar a marcação do tempo e do espaço do mebros já apresentados.')
        print('\nEx: V= m, T=s... a=m/s.')
        a = (v_final - v_inicial)/T
        return a

    def forca(v_inicial: float, v_final: float, T, M: float):
        """
        v_inicial : float, obrigatória
            'v_inicial' representa a velocidade inicial do objeto
        v_final : float, obrigatória
            'v_final' representa a velocidade final do objeto
        T : float, obrigatória
            'T' representa o tempo, em segundos, que o objeto demorou para percorer todo o círculo.

        retorno : float
            aceleração do objeto
        """
        print('\nO calculo da força serve para saber qual é a força que é imposta sobre um objeto.')
        print('\nEx: um carro atinge uma parede de concreto qual a força do carro sobre o muro?')
        print('\nA foça é a aceleração de um objeto mais a sua massa (F = m * A).')
        a = (v_final - v_inicial)/T
        F = M * a
        return F

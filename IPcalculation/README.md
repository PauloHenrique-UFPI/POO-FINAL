IPcalculation
==============

## Esse é um pacote que faz calculos matemáticos, desmostra a fórmula passo a passo até o resultado.

## Veja o exemplo de resultado do pacote:

##IPcalculation.juros_composto(1000.00, 10, 3)

## saida:
##
## O juros composto é calculado de forma que cada parcela contem o valor do capital
## mais um taxa, onde essa taxa é calculada 1 mais a poncentagem do juros, onde o resultado é
## elevado ao número da parcela atual
##
##
## O montante será a soma de todas as parcelas
## M = C + (1+I)^t ---- 1100.00 = 1000.0 * (1+0.1)^1
## M = C + (1+I)^t ---- 1210.00 = 1000.0 * (1+0.1)^2
## M = C + (1+I)^t ---- 1331.00 = 1000.0 * (1+0.1)^3
## Montante final: 3641.00


## Instalação:

    pip install IPcalculation

## Uso:
 ...

    from IPcalculation import IPcalculation 

    OP = IPcalculation.IPcalculation

    OP.juros_composto(1000.00, 10, 3)
    OP.pressao(v,n,r,t)
    OP.calorimetria(m,c,D0)


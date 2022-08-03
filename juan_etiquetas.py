import random

def etiqueta(altura_etq, largura_etq):
    altura_papel = 220
    largura_papel = 250
    distância = 4
    
    img_horizontal1 = altura_papel//(altura_etq + distância)
    img_vertical1 = largura_papel//(largura_etq + distância)
    
    img_horizontal2= largura_papel//(altura_etq + distância)
    img_vertical2 = altura_papel//(largura_etq + distância)

    resultado_final1 = img_horizontal1 * img_vertical1
    resultado_final2 = img_vertical2 * img_horizontal2
   
    if resultado_final1 > resultado_final2:
        print(f' Valor cabível de etiquetas no papel é {resultado_final1}')
        return resultado_final1
    else:
         print(f' Valor cabível de etiquetas no papel é {resultado_final2}')
         return resultado_final2

def calculo(pp,p,m,g,gg, altura, largura):
    img_total = etiqueta(altura, largura)
    qtd_etq= pp + p + m + g + gg

                #cálculo dos decimais:


    pp_decimal= pp / qtd_etq  #0.09
    p_decimal= p / qtd_etq  
    m_decimal= m / qtd_etq    # decimal de m é 0.7
    g_decimal= g / qtd_etq    # decimal de m é 0.3
    gg_decimal= gg / qtd_etq



    pp_etq_total = int(pp_decimal * img_total)
    p_etq_total = int(p_decimal * img_total) 
    m_etq_total = int(m_decimal * img_total)  # Esse é o 11
    g_etq_total = int(g_decimal * img_total)  # Esse é o 5
    gg_etq_total = int(gg_decimal * img_total)

    #region
                # cálculo de folhas
    if pp_etq_total > 0:
        print(f'Cálculo de folhas até agora do PP é  {(pp / pp_etq_total):.0f}')     # valor de pp

    if p_etq_total > 0: 
        print(f'Cálculo de folhas até agora do P é  {(p / p_etq_total):.0f}')        # valor de p
    
    if m_etq_total > 0:
        print(f'Cálculo de folhas até agora do M é  {(m / m_etq_total):.0f}')        # valor de m

    if g_etq_total > 0: 
        print(f'Cálculo de folhas até agora do G é  {(g / g_etq_total):.0f}')        # valor de g
    
    if gg_etq_total > 0:
        print(f'Cálculo de folhas até agora do GG é {(gg / gg_etq_total):.0f}')     # valor de gg

                #Quantidade de etiqueta na folha 

    if pp_etq_total > 0:
        print(f'Quantidade de etiqueta em cada folha do tamanho  PP é {pp_etq_total:.0f}')
    
    if p_etq_total > 0:
        print(f'Quantidade de etiqueta em cada folha do tamanho  P é {p_etq_total:.0f}')
    
    if m_etq_total > 0:
        print(f'Quantidade de etiqueta em cada folha do tamanho  M é {m_etq_total:.0f}')

    if g_etq_total > 0:    
        print(f'Quantidade de etiqueta em cada folha do tamanho G é {g_etq_total:.0f}')

    if gg_etq_total > 0:
        print(f'Quantidade de etiqueta em cada folha do tamanho GG é {gg_etq_total:.0f}')
    
    #endregion
    print(f' Quantidade total de etiqueta é {pp + p + m + g + gg}')

#region                             # VARIÁVEIS
x1 = random.randint(100,1000)
x2 = random.randint(100,1000)
x3 = random.randint(100,1000)
x4 = random.randint(100,1000)
x5 = random.randint(100,1000)
alt_x = random.randint(10,90)
larg_x = random.randint(10,90)
#endregion




calculo(x1,x2,x3,x4,x5, altura=alt_x, largura=larg_x)
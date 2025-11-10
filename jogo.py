print ('bom dia,boa tarde e boa noite')
acertou = 0
errou = 0

#descrução
print("jogo das palavras")
#perguntas
print('como eu me chamo?')
chama = input('escreva meu nome')

if(chama == "yuri"):
       print('senha correta mas ainda não tenho certesa vou ter que fazer outras perguntas')
       acertou +=1
else:
       print('errou')
       errou +=1

if (errou or acertou==1):

       print('mikel jackson está vivo e mora em chique chique bahia')
       
       mikel=input('isso é verdade ou mentira:')
       
       if(mikel=='mentira'):
          print('acertou mais ainda tenho que perguntar outra coisa')
          acertou +=1
          
       else:
           print('como vc errou isso')
           errou +=1
           
if (errou or acertou == 1):

        print('0000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('0000000000000080000000000000000000000000000000000000000000000000000000000000')
        print('0000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('0000000000000000000000000000000000000000000000000000000000000000000000000000')
        
        numero=input('qual o numero escondido')
        
        if(numero=='8'):
            print('acertou. você  tem uma visão boa')
            acertou+=1
            
        else:
            print('numero errado')
            errou+=1
            
if (errou or acertou == 1):

    import random

    print('adivinhe o numero')
    numero_secreto = random.randint(1,10)
    tentativas=0

    while True:
        palpite=int(input("Digite um numero entre 1 a 10"))
        tentativas += 1
    
        if palpite == numero_secreto:
            print("parábens vc acertou em",tentativas,"tentativas" )
            break
    
        elif palpite < numero_secreto:
            print("tente um numero maior")
        
        else:
            print("tente um numero menor")
            
if (errou or acertou ==1):
    print('não falta muitas perguntas')
    lula=input('quantos dedos o presidente lula tem?')
    if(lula=='9'):
        print('acertou')
        acertou+=1
    else:
        print('errou')
        errou+=1

if(errou or acertou==1):
    print('agora vai ser a pergunta mais dificil')
    print('não sei se vc vai estar preparado para essa pergunta')
    cor=input('qual a cor de uma maçã')
    if(cor=='vermelho'):
        print('parábens você acertou')
        acertou+=1
    else:
        print('errouuuuuu')
        errou+=1
        
    if(errou or acertou==1):
        print('você acertou'acertou)
        print('você errou'errou)

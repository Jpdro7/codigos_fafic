nome = input("Digite seu nome: ")
print(f"Ola {nome}")

print("01. O modelo OSI e o TPC/IP incluem uma camada de rede que fornece diversos serviços, EXCETO:")
print("A. Empacotamento das mensagens: encapsulando na origem e desencapsulando no destino.")
print("B. Garantia de entrega confiável dos pacotes.")
print("C. Roteamento e encaminhamento dos pacotes de dados.")
print("D. Controle de congestionamento. Responsabilidade esta compartilhada com a camada de transporte.")
print("E. Lidar com a fragmentação de pacotes.")

questao1 = input("Digite sua resposta: ")

if(questao1 == 'b'):
    print("Voce acertou")
else:
    print("Voce errou")

print("02. Acerca de conceitos e ferramentas de informática, arquitetura cliente-servidor, Internet e intranet, julgue o item. Uma VPN, rede formada por circuitos virtuais, pode utilizar-se corretamente de infraestruturas de redes públicas com protocolos de segurança implementados como IPCES e L2PT, por exemplo, com o uso de protocolos de segurança, criptografia e firewall.")
print("A. Certo")
print("B. Errado")

questao1 = input("Digite sua resposta: ")

if(questao1 == 'b'):
    print("Voce acertou")
else:
    print("Voce errou")

print("03. Nos dias atuais, consome-se conteúdo multimídia via Internet de modo sem precedentes. Serviços de streaming de vídeo e áudio são usados amplamente por pessoas de todo o mundo. No entanto, alguns aspectos envolvidos na transmissão desses tipos de dados devem ser observados a fim de que haja uma qualidade de serviço aceitável. Sobre as Redes Multimídia, marque a única alternativa FALSA: ")
print("A. O RTP (Real-time Transport Protocol) é um protocolo que pode ser usado para transportar tanto áudio como vídeo numa rede de dados.")
print("B. A transmissão de vídeo em alta resolução em tempo real exige tecnologias de banda larga, como ADSL e VDSL.")
print("C. O AAC e AVC são, respectivamente, formatos de áudio e vídeo comprimido bastante usados em streaming.")
print("D. O protocolo UDP é mais adequado que o TCP para streaming de áudio/vídeo.")
print("E. O HTTP não é um protocolo usado quando se quer fazer streaming de vídeo via Internet.")

questao1 = input("Digite sua resposta: ")

if(questao1 == 'e'):
    print("Voce acertou")
else:
    print("Voce errou")

print("04.Marque a alternativa que apresenta somente campos presentes no cabeçalho do protocolo IPv4: ")
print("A. Versão; tamanho total; TTL; Endereço de Origem; Endereço de Destino.")
print("B. Versão; tamanho total; TTL; Porta de Origem; Porta de Destino.")
print("C. Versão; Número de Sequência; TTL; Endereço de Origem; Endereço de Destino.")
print("D. Versão; tamanho da janela; Número de Sequência; Endereço de Origem; Endereço de Destino.")
print("E. Tamanho total; Número de Sequência; Número de Confirmação; Endereço de Origem; Endereço de Destino.")

questao1 = input("Digite sua resposta: ")

if(questao1 == 'a'):
    print("Voce acertou")
else:
    print("Voce errou")

print("05.Endereçamento físico numa rede padrão Ethernet fica por conta do MAC (Media Access Control). Assinale a alternativa que contém apenas campos presentes num quadro MAC: ")
print("A. Sincronismo, IP origem, IP destino, tamanho, CRC32.")
print("B. Sincronismo, IP origem, IP destino, preenchimento, CRC32.")
print("C. Preâmbulo, IP origem, Endereço de origem, tamanho, checksum.")
print("D. Preâmbulo, Endereço de destino, Endereço de origem, tamanho, paridade.")
print("E. Preâmbulo, Endereço de destino, Endereço de origem, tamanho, checksum.")

questao1 = input("Digite sua resposta: ")

if(questao1 == 'e'):
    print("Voce acertou")
else:
    print("Voce errou")

respostas = int(input("Digite sua quantas perguntas voce acertou: "))

if respostas >= 5:
    print("Parabens! Voce foi aprovado")
else:
    print("Voce nao passou, boa sorte na proxima!")

gabarito = input("Voce deseja ver o gabarito")
respostas = print("1.B")
respostas = print("2.B")
respostas = print("3.E")
respostas = print("4.A")
respostas = print("5.E")

if(gabarito == 'sim'):
    print(f"Aqui estao as respostas corretas {respostas}")
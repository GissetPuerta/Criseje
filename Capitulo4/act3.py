pais = str(input("Digite su pais: "))
match pais:
    case 'Italia':
        print('ð®ð¹')
    case 'Brasil':
        print('ð§ð·')
    case 'Colombia':
        print('ð¨ð´')
    case 'EspaÃ±a':
        print('ðªð¸')
    case 'Francia':
        print('ð«ð·')
    case _:
        print("Unknown Pais")
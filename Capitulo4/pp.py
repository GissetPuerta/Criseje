can_fly=bool(input('¿Puede volar?  '))
human=bool(input('¿Es humano? '))
has_a_mask=bool(input('¿Tiene mascara? '))


if can_fly is True:
    if human is True:
        if has_a_mask is True:
            print("iroman")
        if has_a_mask is False:
            print("captain marvel") 
    if human is False:
        if has_a_mask is True:
            print("Ronan Accuser")
        if has_a_mask is False:
            print("vision")
            
elif can_fly is False:
    if human is True :
        if has_a_mask is True:
            print("spiderman")
        if has_a_mask is False :
            print("hulk") 
    else :
        if has_a_mask is True:
            print("Black Bolt")
        if has_a_mask is False:
            print("Thanos")
            
            
            acep=int(edad==>18<65)+(peso==>50)+(pulso==>50<110)+(plaquetas==>150000)

if edad>18<65 , peso>50 , pulso>50<110 , plaquetas>150000:
    print("Apto para donar sangre")

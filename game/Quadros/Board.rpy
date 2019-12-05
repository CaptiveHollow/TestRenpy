label suspeito1:

    "goddamit CAAARL"
    "why the hell would he do that"
    "mas será que é mesmo?"

    menu:
        "Sim.":
            # aumenta o valor da variavel em 1
            $ suspeito1 += 1
            jump continua

        "Não.":
            call screen murderboard

label suspeito2:
    "antes de tudo"
    "queria mandar um abraço pra galera do cachurros"
    "mas será que é mesmo?"
    menu:
        "Sim.":
            $ suspeito2 += 1
            jump continua

        "Não.":
            call screen murderboard


label suspeito3:
    "It's the bear jew"
    "the polish bear jew"
    "mas será que é mesmo?"
    menu:
        "Sim.":
            $ suspeito3 += 1
            jump continua

        "Não.":
            call screen murderboard


label suspeito4:
    "o gato hitler sempre foi um suspeito o tempo todo"
    "Heil Kitler"
    "mas será que é mesmo?"
    menu:
        "Sim.":
            $ suspeito4 += 1
            jump continua

        "Não.":
            call screen murderboard



label suspeito5:
    "acho que ele é o suspeito"
    "mas será que é mesmo?"
    menu:
        "Sim.":
            $ suspeito5 += 1
            jump continua
        "Não.":
            call screen murderboard


label viti:
    "essa é a vitima"
    "pena que morreu"
    "GOSTOSA"
    call screen murderboard





label continua:
    "ta bom"
    "ja chega dessa merda"
    #  de acordo com a variavel mostra o resultado indicado
    if  suspeito1 == 1:
        "acho que suspeito 1 é o culpado"
    elif  suspeito2 == 1:
        "acho que suspeito 2 é o culpado"
    elif  suspeito3 == 1:
        "acho que suspeito 3 é o culpado"
    elif  suspeito4 == 1:
        "acho que suspeito 4 é o culpado"
    elif  suspeito5 == 1:
        "acho que suspeito 5 é o culpado"

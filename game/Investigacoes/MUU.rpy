
label vaca:
    "a vaca longa chegou"
    "ela é longa"
    "desista"
    pause 0.5
    call screen debug

label vaca2:
    "a vaca ainda é longa"
    "desista"
    "antes que seja tarde"
    pause 0.5
    call screen debug

label acabar:
    "OK"
    "Acho que é isso por hoje"
    "ou sera que não??"

    # faz uma escolha
    menu:
        "Continuar a investigação.":
            # pausa o jogo por 0.5 segundo
            pause 0.5
            call screen debug

        "parar de investigar.":
            jump continuar

label continuar:
    "ok"
    " agora que eu consegui escapar da vaca"
    "(pelo menos por enquanto)"
    "É hora de ir pra casa e revisar tudo"
    "(E também porque preciso dar aquela cagada, vai entupir o encanamento do prédio)"
    "INVESTIGATION TIME"
label murder:
    "now"
    "vamo assistir um porno de konosuba"
    scene quadro
    with fade
    call screen murderboard

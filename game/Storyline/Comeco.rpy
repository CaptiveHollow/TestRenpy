label inicio:
    # chamar a cena com trancição "fade"
    scene scene2
    with fade
    # monologo comum
    "Hoje o dia está muito ensolarado, os pássaros estão cantando, isso me lembra do kakapo.. como eu queria ter um kakapo."

    "Decidi ir me encontrar com meu melhor amigo, William, para discutirmos sobre o cavalo e sua tropa."

    "Quando eramos crianças, sempre tivemos essa discussão: o cavalo é gay ou não? Eis a questão."

    # fala de outro personagem
    a "Eae gay, tá tao serio pq???"
    # mostrar o personagem na direção indicada
    show alex at right

    show will2 at left


    "William vira pra mim e me olha putasso, ele não gosta de ser chamado de gay, mesmo sendo."

    "É AGORA OU NUNCA"

    a "William... sobre aquele assunto do cavalo ser gay.."

    a "Eu poderia provar seu cu?"

    #  esconder o personages
    hide alex
    hide will2

    # mostrar o personagem
    show alex2 at right
    with dissolve
    show will3 at left
    with dissolve

    a "to com tanto tezão que eu comeria até uma vaca."

    w "MOOOOOOOOO"

    "gay"

    "cavalo gay"

    w "o cavalo é \"gay?\""
    menu:
        "o cavalo é gay":
            jump penis

        "o cavalo não é gay":
            jump penis

label penis:

    #  desativa o skip
    $ config.allow_skipping = False

# escolhe a rota aleatoriamente
if tropa == 1:
    jump cavalogay
elif tropa == 2:
    jump cavalonaogay

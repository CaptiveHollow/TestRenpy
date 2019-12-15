
# nivel de suspeita do protagonista
define suspeito1 = 0
define suspeito2 = 0
define suspeito3 = 0
define suspeito4 = 0
define suspeito5 = 0

#  nivel de relacionamento do protagonista
define relacio1 = 0
define relacio2 = 0
define relacio3 = 0
define relacio4 = 0
define relacio5 = 0

# saude mental do protagonista
define mentalHealth = 0

# rota definida pelo sistema
define tropa = renpy.random.choice([1,2])

# Nomes Personagens
define a = Character('Alec', color="#c8ffc8")
define w = Character('William', color="af3562")
define m = Character('Me', color="#c8c8ff")

# define musicas
define song1 = "audio/vaco.mp3"
define seong2 = "audio/Dosed.mp3"
# play music "mozart.ogg"

# imagens do mural de investigação
define sus1 = "images/quadro/Carl.png"
define sus2 = "images/quadro/churro.jpg"
define sus3 = "images/quadro/dobro.jpg"
define sus4 = "images/quadro/gato.jpg"
define sus5 = "images/quadro/kibes.jpg"
define vitima = "images/quadro/Igor.png"
define jornal = "images/quadro/nal.png"

# cenarios
image scene1 = "images/scenario/Scene1.jpg"
image scene2 = "images/scenario/Scene2.jpg"
image scene3 = "images/scenario/bedroom.jpg"
image quadro = "images/quadro/quadro.jpg"


# personagens
image alex = "images/chars/alec.png"
image alex2 = "images/chars/alec2.png"
image alex3 = "images/chars/alec3.png"
image will1 = "images/chars/wili.png"
image will2 = "images/chars/willan1.png"
image will3 = "images/chars/willan2.png"

# icones do modo de investigação
define icone = "images/Others/icone.png"
define seta = "images/Others/seta.png"

# definindo nosso cenario para investigação
screen debug():

    draggroup:

        drag:
            drag_name "VACA"
            child icone
            draggable False
            clicked Jump("vaca")
            xpos 100 ypos 100

        drag:
            drag_name "VA"
            child icone
            draggable False
            clicked Jump("vaca2")
            xpos 500 ypos 100

        drag:
            drag_name "SETA"
            child seta
            draggable False
            clicked Jump("acabar")
            xpos 10 ypos 800

#  definindo nosso mural de investigação
screen murderboard():

    draggroup:

        drag:
            drag_name "SUS1"
            child sus1
            draggable False
            clicked Jump("suspeito1")
            xpos 100 ypos 100

        drag:
            drag_name "SUS2"
            child sus2
            draggable False
            clicked Jump("suspeito2")
            xpos 500 ypos 100


        drag:
            drag_name "SUS3"
            child sus3
            draggable False
            clicked Jump("suspeito3")
            xpos 1000 ypos 100

        drag:
            drag_name "SUS4"
            child sus4
            draggable False
            clicked Jump("suspeito4")
            xpos 1500 ypos 100

        drag:
            drag_name "SUS5"
            child sus5
            draggable False
            clicked Jump("suspeito5")
            xpos 2000 ypos 100

        drag:
            drag_name "VITIMA"
            child vitima
            draggable False
            clicked Jump("viti")
            xpos 500 ypos 390



# Inicio da historia
label start:
    # toca a musica
    # play music "audio/vaco.mp3"
    # play music "<from 23 to 30>audio/vaco.mp3"
    # chamar o metodo "inicio"
    jump inicio

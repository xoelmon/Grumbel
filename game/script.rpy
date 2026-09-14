#personajes
define gru = Character('Grumbler', color="#C15602")
define ma = Character('Madre', color="#c10f02") 
define hu1 = Character('Ramón', color="#98c102")
define hu2 = Character('Pepe', color="#027bc1")


#inicio del juego
label start:

    $ renpy.movie_cutscene("intro_xvid.avi")

    play music bso_dark

    scene bg_bosque2
    with fade

    "Grumbler de 3 años de edad, vive en una pequeña cueva con sus padres ogros, 
    en una zona alejada y tranquila. Sin embargo, estos últimos dias los animales 
    están más nerviosos de lo normal. Grumbler lleva unas cuantas noches teniendo 
    la misma pesadilla..."

    scene bg_cuevadentro

    show grumbler
    with fade

    gru "Aaaahh!"

    show madre at left
    with fade        

    ma "Tranquilo hijo ha sido una pesadilla."
    gru "Que miedo mamá."
    ma "Vuelve a dormir pequeñajo..."

    scene black
    with fade
    play sound fx_pelea

     
    hu1 "Muere sucio ogro."

    scene bg_cuevadentro

    show grumbler at right
    with fade   

    gru "MAMA, PAPA, NOOOOO!"

    show humano1 at left 
    show humano2
    play music 'audio/fx_fuego.mp3'
    with fade

    hu1 "¡Mira al pequeñajo!"

    hu2 "Déjalo vivir, no vale para nada. ¡Vámonos!"

    stop music

    play music bso_tranqui

    scene black
    with dissolve



    scene bg_fueracueva
    with fade

    show grumbler
    with fade

    gru "Os echaré de menos queridos padres. snif, snif..."

    menu:
        "Voy en busca de los asesinos y cobro mi venganza.": 
            jump viaje


        "Soy pacífico y mis padres ejem..., mejor me quedo en casa.":
            jump casa


label viaje:

    scene black
    with dissolve

    scene bg_bosque2
    with fade

    show grumbler

    gru "Llevo 17 dias caminando y aún no he encontrado ningún rastro, espera!, qué es eso?"

    show humo2 at topright


    menu:
        "Voy hacia ese humo que se ve a lo lejos.":
            jump humo

        "Sigo atravesando por la maleza del bosque.":
            jump maleza


label casa:

    play sound fx_over
    scene bg_gameover
    with fade

    "Te quedas en la cueva y te mueres de hambre. FIN."

    return


label humo:

    play sound fx_fuego
    scene black
    with dissolve

    scene bg_bosque3
    show humano1 at left
    show humano2
    with fade


    "Grumbler se encuentra ante una encrucijada, ¿que podrá hacer?"

    menu:
        "Ataco a machete y gritando":
            jump machete

        "Espero a que se haga de noche y por sorpresa...":
            jump noche

        "Retrocedo y busco quien me ayude a reventarlos.":
            jump ayuda

        "Me subo a un árbol para vigilarlos.":
            jump arbol

    stop sound


label maleza:

    play sound fx_over
    scene bg_gameover
    with fade

    "Te quedas enredado en unas hiedras y te mueres de hambre. FIN."

    return


label machete:

    play sound fx_over
    scene bg_gameover
    with dissolve

    "Con un rencor desmesurado avanzas y gritando en cólera, fallas tu primer ataque, lo cual te deja 
    completamente vendido y, los asquerosos humanos te degollan en un abrir y cerrar de ojos. FIN."

    return


label noche:
    
    play sound fx_over
    scene bg_gameover
    with dissolve

    "Te escondes detrás de un árbol, te quedas dormido y cuando te das cuenta, dos lobos te están 
    comiendo las piernas. FIN."

    return

label ayuda:

    play sound fx_over
    scene bg_gameover
    with dissolve

    "Retrocedes y encuentras una antigua aldea donde te forjas como luchador y algún dia... FIN."

    return

label arbol:

    play sound fx_ole
    scene bg_gamewin
    show grumbler
    with fade

    "Te encuentras subido al árbol, das un paso en falso, tú y un montón de ramas afiladas caéis 
    en picado encima de los humanos atravesando sus entrañas, 
    dejando sus cuerpos a merced de los cuervos. ¡ENHORABUENA SACIASTE TU SED DE SANGRE! FIN."

    return
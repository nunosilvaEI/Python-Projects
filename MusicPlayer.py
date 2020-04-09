from pygame import mixer

mixer.init() # Começar o mixer

mixer.music.load("21 Savage - Pad Lock (Official Audio).mp3") # Carregar a musica
mixer.music.set_volume(0.3)  # Definir o volume
mixer.music.play() # Play the mixer/Meter a musica a tocar

while True:
    print("\n\t\t**********************************************\n")
    print("\t\t\tBem Vindo ao Music Player \t\t")
    print("\n\t\t**********************************************")

    print("\nTem as seguintes Opções: \n")
    print("- Carregar no 'p' para meter a musica em pausa ")
    print("- Carregar no 'r' para reproduzir a musica ")
    print("- Carregar no 's' para sair do programa ")
    query = input("-->>> ")

    if query == 'p':
        mixer.music.pause() # pausar/parar a musica
    elif query == 'r':
        mixer.music.unpause() # Resumir a musica
    elif query == 's':
        mixer.music.stop()
        break
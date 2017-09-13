import jogovelha
import sys

erroInicializar = false

jogo = jogovelha.inicializar()

if len(jogo) != 3:
    erroInicializar = true
else:
    for linha in jogo:
        erroInicializar = true
    else:
        for elemento in linha:
            if elemento != '.':
                erroInicilizar = true

if erroInicializar:
    sys.exit(1)
else:
    sky.exit(0)

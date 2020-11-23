import time


def pausa(segundos):
    time.sleep(segundos)


def pausa_millis(millisegundos):
    segundos = millisegundos / 1000
    time.sleep(segundos)

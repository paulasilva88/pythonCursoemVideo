'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame

pygame.init()
pygame.mixer.music.load('ex21.mp3') #carrega a música
pygame.mixer.music.play() #Começa a tocar
pygame.event.wait() #espera o evento acabar fechar

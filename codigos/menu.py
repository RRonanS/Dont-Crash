import PySimpleGUI as Sg
from .leitura import get_recorde

versao = 1.0


def menu():
    size = 300, 310
    background = 'black'
    text_color = 'red'
    fonte = 'arial 15'
    fonte2 = 'arial 10'
    frame = Sg.Frame('',
                     [[Sg.Text('Dont Crash', text_color=text_color,
                               background_color=background, font=fonte)],
                      [Sg.Button('Jogar', button_color=background,
                                 border_width=2, font=fonte, key='jogar')],
                      [Sg.Text('', font=fonte, visible=True,
                               background_color=background)],
                      [Sg.Text('', font=fonte, visible=True,
                               background_color=background)],
                      [Sg.Text('', font=fonte, visible=True,
                               background_color=background)],
                      [Sg.Text('', font=fonte, visible=True,
                               background_color=background)],
                      [Sg.Text('', font=fonte2, visible=True,
                               background_color=background)],
                      [Sg.Text(f'Versão {versao}', text_color='white',
                               background_color=background,
                               font=fonte2, key='versao')],
                      [Sg.Text(f'Recorde {get_recorde()}', text_color='white',
                               background_color=background,
                               font=fonte2, key='recorde')]],
                     background_color=background, border_width=0,
                     element_justification='ce', size=size)
    tela = Sg.Window('Dont Crash', [[frame]],
                     background_color=background, size=size, element_justification='ce')
    while True:
        e, v = tela.read()
        if e is None:
            tela.close()
            return False
        elif e == 'jogar':
            return True


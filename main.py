import PySimpleGUI as sg


tab1_layout = [
    [sg.Text('Введите температуру:')],
    [sg.Input(key='-INPUT-')],
    [sg.Button('Конвертировать')]
]


tab2_layout = [
    [sg.Text('Выберите опцию подсчета:')],
    [sg.Combo(['Цельсий в Фаренгейт', 'Фаренгейт в Цельсий', 'Цельсий в Кельвин'], key='-OPTION-')],
    [sg.Button('Конвертировать')]
]


tab3_layout = [
    [sg.Text('Результат:', size=(15, 1), justification='center')],
    [sg.Text(size=(40, 1), key='-RESULT-')]
]


tab_group_layout = [
    [sg.Tab('Ввод значения', tab1_layout), sg.Tab('Выбор опции', tab2_layout), sg.Tab('Результат', tab3_layout)]
]


layout = [[sg.TabGroup(tab_group_layout)]]
window = sg.Window('Конвертер температуры', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Конвертировать':
        if values['-OPTION-'] == 'Цельсий в Фаренгейт':
            result = float(values['-INPUT-']) * 1.8 + 32
        elif values['-OPTION-'] == 'Фаренгейт в Цельсий':
            result = (float(values['-INPUT-']) - 32) / 1.8
        elif values['-OPTION-'] == 'Цельсий в Кельвин':
            result = float(values['-INPUT-']) + 273.15
        window['-RESULT-'].update(f'Результат: {result}')

window.close()

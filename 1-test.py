import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    favorites_names = []
    history_text = ft.Text(value="История приветствий:")
    fs_names = ft.Text(value='Избарнные имена:')
    current_name = ''
    # greeting_text.value = 'Привет'
    # greeting_text.color = ft.Colors.GREEN
    
    def on_button_click(_):
        # print(name_input.value)
        name = name_input.value.strip()
        nonlocal current_name
        current_name = name
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None
            
            greeting_history.append(f"{timestamp} - {name}")
            if len(greeting_history)>5:
                greeting_history.pop(0)
            print('\n',*greeting_history,sep='\n')
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history) 

            


        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        # print(greeting_text)
        page.update()
    def favorites_button_click(_):
        favorites_names.append(current_name)
        fs_names.value = 'Избарнные имена:\n' + '\n'.join(favorites_names)
        page.update()

        print(favorites_names)

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()

    

    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    favorites_button = ft.ElevatedButton(text='Добавить в избранное', on_click=favorites_button_click)

    # page.add(greeting_text, name_input, button_text, history_text )

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)





    page.add(view_greeting_text, ft.Row([name_input, button_elevated, clear_button]), ft.Row([history_text,favorites_button],ft.MainAxisAlignment.SPACE_BETWEEN),fs_names)


ft.app(target=main)
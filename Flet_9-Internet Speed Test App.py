import flet as ft

import speedtest
from time import sleep


def main(page: ft.Page):
    page.title = 'Internet Speed Test'
    page.fonts = {
        "AVELIRE": 'fonts/AVELIRE.otf',
        'Magnolia': 'fonts/Magnolia.ttf',
        'Carymoon Basekine Italic': 'fonts/Carymoon Basekine Italic.otf',
        'font1': 'fonts/font1.otf',
        'font2': 'fonts/font2.ttf', 'font3': 'fonts/font3.ttf',
        'font4': 'fonts/font4.otf'
    }
    page.padding = 30
    page.window_bgcolor = '#115852'
    page.bgcolor = '#B7CCCB'
    page.scroll = True
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # initializing Speed Test Variable

    st = speedtest.Speedtest()

    # Application Title
    app_title = ft.Row([ft.Text(value='Internet', font_family='font3', size=50, color='#115852'),
                        ft.Text(value='Speed', font_family='font3', size=50, color='#115852')]
                       , alignment='center')
    # Container lines
    line1 = ft.Text(value='>Press Start.....', font_family='font4')
    line2 = ft.Text(value='', font_family='font4')
    line3 = ft.Text(value='', font_family='font4')
    progess1 = ft.ProgressBar(width=400, color='#115852', opacity=0)
    progess_text1 = ft.Text('  ', font_family='font4', opacity=0)
    progess_row1 = ft.Row([progess_text1, progess1])
    line4 = ft.Text(value='', font_family='font4')
    line5 = ft.Text(value='', font_family='font4')
    line6 = ft.Text(value='', font_family='font4')
    progess2 = ft.ProgressBar(width=400, color='#115852', opacity=0)
    progess_text2 = ft.Text('  ', font_family='font4', opacity=0)
    progess_row2 = ft.Row([progess_text2, progess2])
    line7 = ft.Text(value='', font_family='font4')
    line8 = ft.Text(value='', font_family='font4')

    lines = ft.Column([line1, line2, line3, progess_row1, line4, line5, line6, progess_row2, line7, line8])

    # Internet Speed Container-terminal
    speed_container = ft.Container(content=lines,
                                   width=200, height=100, border_radius=30, bgcolor='#FFFFFF', padding=20,
                                   animate=ft.animation.Animation(1000, 'bounceOut'))

    # Container Resizer
    def animate_speed_container(e):
        #if the user wants to check the speed for second time
        progess_row1.opacity = 0
        progess1.opacity = 0
        progess1.value = None
        progess_row2.opacity = 0
        progess2.opacity = 0
        progess2.value = None
        line1.value = ''
        line2.value = ''
        line3 .value= ''
        line4 .value= ''
        line5 .value= ''
        line6 .value= ''
        line7 .value= ''
        line8 .value= ''
        speed_container.update()

        speed_container.width = 750
        speed_container.height = 400
        line1.value = '>> Calculating download speed,Please Wait...'
        speed_container.update()
        sleep(1)

        ideal_server = st.get_best_server()  # to connect to the best possible server in our region
        city = ideal_server['name']
        country = ideal_server['country']
        country_code = ideal_server['cc']
        line2.value = f'>> Finding the best possible servers in {city},{country},({country_code})'
        speed_container.update()
        sleep(1)

        line3.value = '>> Connection established ,status OK,fetching download speed'
        speed_container.update()
        sleep(1)

        progess_row1.opacity = 1
        progess1.opacity = 1
        speed_container.update()
        sleep(1)

        download_speed = st.download() / 1024 / 1024  # bytes per sec to bits per sec
        progess1.value = 1  # completed progress
        line4.color = '#115852'
        line4.value = f'>> The download speed is {str(round(download_speed, 2))} Mbps'
        speed_container.update()
        sleep(1)

        line5.value = '>> Calculating upload speed,please wait...'
        speed_container.update()
        sleep(1)

        line6.value = '>> Executing upload script,hold on'
        speed_container.update()
        sleep(1)

        progess_row2.opacity = 1
        progess2.opacity = 1
        speed_container.update()
        sleep(1)

        upload_speed = st.upload() / 1024 / 1024  # bytes per sec to bits per sec
        progess2.value = 1
        line7.color = '#115852'
        line7.value = f'>> The upload speed is {str(round(upload_speed, 2))} Mbps'
        speed_container.update()
        sleep(1)

        line8.value = '>> Task completed successfully\n\n>> App Developer : Sharma G ,Linkedin Profile:https://www.linkedin.com/in/sharma-g-124923253'
        speed_container.update()

    # Components
    page.add(
        app_title,
        speed_container,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_speed_container, icon_size=50,
                      icon_color='#115852', animate_size=True)
    )


ft.app(target=main, assets_dir='assets',view=ft.WEB_BROWSER)

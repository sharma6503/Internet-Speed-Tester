import flet as ft

import speedtest
from time import sleep
from  typewriter_control import Typewriter

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
    line1 = Typewriter(value='>Press Start.....', font_family='font4')
    line2 = Typewriter(value='', font_family='font4')
    line3 = Typewriter(value='', font_family='font4')
    progess1 = ft.ProgressBar(width=400, color='#115852', opacity=0)
    progess_text1 =Typewriter('  ', font_family='font4', transperancy=False)
    progess_row1 = ft.Row([progess_text1, progess1])
    line4 = Typewriter(value='', font_family='font4')
    line5 = Typewriter(value='', font_family='font4')
    line6 = Typewriter(value='', font_family='font4')
    progess2 = ft.ProgressBar(width=400, color='#115852', opacity=0)
    progess_text2 = Typewriter('  ', font_family='font4',transperancy=False)
    progess_row2 = ft.Row([progess_text2, progess2])
    line7 = Typewriter(value='', font_family='font4')
    line8 = Typewriter(value='', font_family='font4')

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
        line1.text = ''
        line1.update()
        line2.text= ''
        line2.update()
        line3 .text= ''
        line3.update()
        line4 .text= ''
        line4.update()
        line5 .text= ''
        line5.update()
        line6 .text= ''
        line6.update()
        line7 .text= ''
        line7.update()
        line8 .text= ''
        line8.update()
        speed_container.update()

        speed_container.width = 750
        speed_container.height = 400
        line1.text = '>> Calculating download speed,Please Wait...'
        speed_container.update()
        sleep(1)
        line1.update()  

        ideal_server = st.get_best_server()  # to connect to the best possible server in our region
        city = ideal_server['name']
        country = ideal_server['country']
        country_code = ideal_server['cc']
        line2.text = f'>> Finding the best possible servers in {city},{country},({country_code})'
        line2.update()
        speed_container.update()
        sleep(1)

        line3.text = '>> Connection established ,status OK,fetching download speed'
        line3.update()
        speed_container.update()
        sleep(1)

        progess_row1.opacity = 1
        progess1.opacity = 1
        speed_container.update()
        sleep(1)

        download_speed = st.download() / 1024 / 1024  # bytes per sec to bits per sec
        progess1.value = 1  # completed progress
        line4.color = '#115852'
        line4.text = f'>> The download speed is {str(round(download_speed, 2))} Mbps'
        line4.update()
        speed_container.update()
        sleep(1)

        line5.text = '>> Calculating upload speed,please wait...'
        line5.update()
        speed_container.update()
        sleep(1)

        line6.text = '>> Executing upload script,hold on'
        line6.update()
        speed_container.update()
        sleep(1)

        progess_row2.opacity = 1
        progess2.opacity = 1
        speed_container.update()
        sleep(1)

        upload_speed = st.upload() / 1024 / 1024  # bytes per sec to bits per sec
        progess2.value = 1
        line7.color = '#115852'
        line7.text = f'>> The upload speed is {str(round(upload_speed, 2))} Mbps'
        line7.update()
        speed_container.update()
        sleep(1)

        line8.text = '>> Task completed successfully\n\n>> App Developer : Sharma G ,Linkedin Profile:https://www.linkedin.com/in/sharma-g-124923253'
        line8.update()
        speed_container.update()

    # Components
    page.add(
        app_title,
        speed_container,
        ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=animate_speed_container, icon_size=50,
                      icon_color='#115852', animate_size=True)
    )


ft.app(target=main, assets_dir='assets',view=ft.WEB_BROWSER)

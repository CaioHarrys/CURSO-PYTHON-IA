

from cep import buscar_endereco
import flet as ft



def main(page: ft.Page):
    #Configurando a tela
    page.theme_mode=ft.ThemeMode.SYSTEM
    page.window.width=300
    page.window.heigth=100
    page.title='Buscador de CEP'
    page.bgcolor=ft.Colors.INDIGO_50
    page.window.always_on_top=True #utilizar essa linha somente durante o desenvolvimento mantem o app sempre a frente
    page.vertical_alignment=ft.MainAxisAlignment.CENTER #centraliza verticalmente
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    campo_cep = ft.TextField(
        label='Digite seu cep',
        color=ft.Colors.CYAN_900
    )

    icone=ft.Icon(
        name=ft.Icons.LOCATION_ON,
        size=70,
        color=ft.Colors.RED_300
        )
    
    campo_resposta=ft.Text(
        value='', #aqui é onde aparece os dados recebidos
        color=ft.Colors.RED_300,
        text_align=ft.TextAlign.CENTER
    )

    btn_buscar=ft.ElevatedButton(
        text='Buscar',
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.WHITE,
        width=100,
        icon=ft.Icons.SEARCH,
        on_click=lambda evento: buscar_endereco(campo_cep.value, campo_resposta)
    )

    #coloando os itens na janela
    page.add(
        icone,
        campo_resposta,
        campo_cep,
        btn_buscar
        
    )

ft.app(main)

import flet as ft  

def main(page: ft.Page):  
    texto = ft.Text("Hello, Flet!")  

    def mudar_texto(e):  
        texto.value = "Você clicou no botão!"  
        page.update()  # Atualiza a página para mostrar o texto atualizado  

    botao = ft.ElevatedButton("Clique Aqui", on_click=mudar_texto)  

    page.add(ft.SafeArea(texto, botao))  

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
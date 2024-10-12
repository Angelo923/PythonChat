# Tela Inicial:
    # Título: Hashzap
    # Botão: Iniciar Chat
        # quando clicar no botão: 
        # abrir um Popup/modal/alert
            # Título: Bem vindo ao Hashzap
            # Caixa de Texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # quando clicar no botão 
                # sumir com título 
                # sumir com o botão iniciar Chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem: "Digite sua mensagem" 
                    # Botão enviar
                        # quando clicar no botão enviar 
                        # enviar a mensagem 
                        # limpar a caixa de mensagem
# pip install flet
# importar o flet

import flet as ft
from datetime import datetime

# criar uma função principal para roda o seu aplicativo
def main(pagina: ft.Page):
    # titulo
    titulo = ft.Text("CapeZap")

    def enviar_mensagem_tunel(mensagem):
        # executar para todos usuários
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        #pega a mensagem digitada
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{data_e_hora_em_texto} - {nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        
        # limpar a caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        # atualizaq a pagina
        pagina.update()

    # carregar o campo de enviar mensagem: "Digite sua mensagem" 
    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem",
                                         on_submit=enviar_mensagem)

    # Botão enviar
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Deixar o campo de mensagem e o botão na mesma linha
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        # fechar o pop up 
        popup.open = False

        # sumir com o título 
        pagina.remove(titulo)

        # sumir com o botão Iniciar Chat
        pagina.remove(botao) 

        # carregar o chat 
        pagina.add(chat)

        # carregar o campo de enviar mensagem 
        # Carregar o botão enviar
        pagina.add(linha_enviar)

        # adicion ar no chat a mensagem "(nome do usuário) entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        # Atualizar a tela 
        pagina.update()

    # criar o popup
    titulo_popup = ft.Text("Bem vindo ao CapeZap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,
                           actions=[botao_popup])

    # botão inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True

        # Atualizar a tela 
        pagina.update()

        # o que acontece quando clica no botão
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # colocar elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)

# executar essa função com o flet
ft.app(target=main, view=ft.AppView.WEB_BROWSER)

#Falta fazer deploy num servidor - pesquisar: flet deploy no google.
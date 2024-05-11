# Importando bibliotecas
import customtkinter as ctk
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)

defaultTheme = gsettings.applyedTheme

# Função que será chamada para criar a GUI
def createAboutGui(anexwindow):
    aboutGuiFrame = ctk.CTkFrame(anexwindow, fg_color="transparent", corner_radius=0)
    aboutGuiFrame.grid(row=0, column=1, sticky="nswe")
    aboutGuiFrame.grid_columnconfigure(0, weight=1)
    aboutGuiFrame.grid_rowconfigure(0, weight=1)

    centralizeFrame = ctk.CTkFrame(aboutGuiFrame, fg_color=defaultTheme["accent-color"], corner_radius=0)
    centralizeFrame.grid(row=0, column=0, sticky="ew")

    titleLabel = ctk.CTkLabel(centralizeFrame, text="AI Writer Companion", font=ctk.CTkFont(size=30, weight='bold'))
    titleLabel.pack(pady=5)

    descriptionLabel = ctk.CTkLabel(centralizeFrame, text="Obrigado por utilizar o AI Writer Companion!\nO que você está utilizando é uma versão em desenvolvimento que foi feito em 2 dias (com mais de 24 horas apenas de trabalho) como uma ferramenta para ajudar escritores a justamente fazer suas criações, assim como também foi criado como uma entrada para a competição final do curso #ImersãoAI da Alura\n\nEste também é minha primeira ferramenta em Python! Então além de ainda não estar completa, existe muito código a ser melhorado também, ainda mais levando em conta o curto prazo de desenvolvimento para alguém que ainda por cima estava aprendendo esta linguagem de programação do zero. Ainda sim, a ferramenta já é funcional e eu espero que ela ajudem vocês na escrita.\n\nCriado por: Luisovc1812\nDiscord: @luisovc1812", font=ctk.CTkFont(size=15), wraplength=500, justify="center")
    descriptionLabel.pack(pady=5)

    infoLabel = ctk.CTkLabel(centralizeFrame, text="Versão 0.1 (Dev)\nAI Writer Companion - Sob licença CC BY-SA 4.0\n\n As empresas e marcas Google e Alura não tem afiliação direta com esta ferramenta, mas foram\n utilizados da tecnologia do Google AI Studio e Gemini 1.5 Pro que são propriedades da Google,\n assim como a empresa Alura foi mencionado por este projeto também ser uma entrada para\n um de seus eventos.\nA logotipo e o banner foram feitos com ajuda da geração de imagens do Gemini.\nTodos os direitos para seus respectivos donos.", font=ctk.CTkFont(size=12), text_color="gray")
    infoLabel.pack(pady=5)

    return aboutGuiFrame
# Importando bibliotecas
import customtkinter as ctk
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)

defaultTheme = gsettings.applyedTheme

# Função que será chamada para criar a GUI
def createSettingsGui(anexwindow):
    global settingsGuiFrame
    settingsGuiFrame = ctk.CTkFrame(anexwindow, fg_color="transparent", corner_radius=0)
    settingsGuiFrame.grid(row=0, column=1, sticky="nswe")
    settingsGuiFrame.grid_columnconfigure(0, weight=1)
    settingsGuiFrame.grid_rowconfigure(0, weight=1)

    centralizeFrame = ctk.CTkFrame(settingsGuiFrame, fg_color=defaultTheme["accent-color"], corner_radius=0)
    centralizeFrame.grid(row=0, column=0, sticky="ew")
    centralizeFrame.grid_columnconfigure(0, weight=5)
    centralizeFrame.grid_columnconfigure(1, weight=1)
    centralizeFrame.grid_rowconfigure(0, weight=1)
    centralizeFrame.grid_rowconfigure(1, weight=1)
    centralizeFrame.grid_rowconfigure(2, weight=1)

    titleLabel = ctk.CTkLabel(centralizeFrame, text="• Configurações •", font=ctk.CTkFont(size=30, weight='bold'))
    titleLabel.grid(row=0, column=0, columnspan=2, pady=10)

    deleteApiKeyLabel = ctk.CTkLabel(centralizeFrame,text="Remover chave de API", font=ctk.CTkFont(size=15, weight="bold"), anchor="w")
    deleteApiKeyLabel.grid(row=1, column=0, sticky="ew", padx=15, pady=10)

    deleteApiKeyButton = ctk.CTkButton(centralizeFrame, fg_color=defaultTheme["danger-color"], text_color="white", text="Remover", command=removeApiKeyButtonPress)
    deleteApiKeyButton.grid(row=1, column=1, sticky="ew", padx=15, pady=10)
    
    versionLabel = ctk.CTkLabel(centralizeFrame, text="Futuras versões contarão com mais opções de personalização,\ncomo alterar as configurações padrões dos filtros de bloqueio.", font=ctk.CTkFont(size=12), text_color="gray")
    versionLabel.grid(row=2, column=0, columnspan=2, pady=10)

    return settingsGuiFrame

def removeApiKeyButtonPress():
    gsettings.mainSettings["api_key"] = ""
    gsettings.saveConfigsChange()
    from gui.maingui import startApiCheck
    settingsGuiFrame.destroy()
    startApiCheck()
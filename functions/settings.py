# Importando bibliotecas
import json
import os

# Configurações

mainSettings = {}

applyedTheme = {}

# Identifica o local do arquivo de tema independentemente de qual diretório este programa está localizado.
with open(os.path.join(os.path.curdir, "style", "themes", "defaultBlack.json"), 'r') as themeFile:
    applyedTheme = json.load(themeFile)

# Identifica o local do arquivo de configurações Independentemente de qual diretório este programa está localizado.
with open(os.path.join(os.path.curdir, "settings.json"), "r") as settingsFile:
    mainSettings = json.load(settingsFile)

# Salvar alterações de configurações
def saveConfigsChange():
    with open(os.path.join(os.path.curdir, "settings.json"), "w") as settingsFile:
        json.dump(mainSettings, settingsFile, indent=4)
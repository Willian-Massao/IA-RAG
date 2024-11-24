#!/bin/bash
if [ -w "./target" ]; then
    mkdir target
    mkdir data
else
    echo "Sem permissão para criar a pasta!!, execute como root ou altere as permissões para continuar."
    exit 1
fi

# Verificar se o Python está instalado
if command -v python3 &>/dev/null; then
    echo "Python já está instalado."
else
    echo "Python não encontrado. Instalando..."
    # Instalar Python (Ubuntu/Debian)
    sudo apt update
    sudo apt install -y python3
fi

# Verificar se o pip está instalado
if command -v pip3 &>/dev/null; then
    echo "pip já está instalado."
else
    echo "pip não encontrado. Instalando..."
    # Instalar pip para Python 3 (Ubuntu/Debian)
    sudo apt install -y python3-pip
fi

pip install -r requirements.txt

# Verificar se o Ghostscript (gs) está instalado
if command -v gs &>/dev/null; then
    echo "Ghostscript (gs) já está instalado."
else
    echo "Ghostscript (gs) não encontrado. Instalando..."

    # Verificar a distribuição para usar o gerenciador de pacotes correto
    if command -v apt &>/dev/null; then
        # Para distribuições baseadas no Debian/Ubuntu
        sudo apt update
        sudo apt install -y ghostscript
    elif command -v yum &>/dev/null; then
        # Para distribuições baseadas no Red Hat (CentOS, Fedora, etc.)
        sudo yum install -y ghostscript
    elif command -v dnf &>/dev/null; then
        # Para Fedora
        sudo dnf install -y ghostscript
    else
        echo "Gerenciador de pacotes não identificado. Instale o Ghostscript manualmente."
        exit 1
    fi
fi
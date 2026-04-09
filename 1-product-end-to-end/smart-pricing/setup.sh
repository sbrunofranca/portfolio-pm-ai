#!/bin/bash

# Setup Script - Smart Pricing
# Como usar: bash setup.sh

echo "🚀 Iniciando setup do Smart Pricing Project..."

# 1. Criar ambiente virtual (opcional)
if [ ! -d "venv" ]; then
    echo "📦 Criando virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
fi

# 2. Instalar dependências
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# 3. Criar pastas necessárias
mkdir -p data/raw
mkdir -p data/processed

# 4. Validar instalação
echo "✅ Setup completo!"
echo ""
echo "Próximos passos:"
echo "1. python scripts/01-analyze-elasticity.py"
echo "2. python scripts/02-generate-recommendations.py"
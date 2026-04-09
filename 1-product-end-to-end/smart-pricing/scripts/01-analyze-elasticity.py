#!/usr/bin/env python
"""
Script 1: Analisa elasticidade de preço
Como rodar: python scripts/01-analyze-elasticity.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from src.data_loader import DataLoader
from src.elasticity_analyzer import ElasticityAnalyzer
import pandas as pd

def main():
    print("="*70)
    print("ANÁLISE DE ELASTICIDADE DE PREÇO")
    print("="*70)
    
    # Carrega dados
    loader = DataLoader('data/raw/sample_sales.csv')
    df = loader.load()
    print(f"\n✅ Dataset carregado: {len(df)} linhas")
    
    # Prepara dados semanais
    df_weekly = loader.prepare_weekly_data()
    print(f"✅ Dados agregados: {len(df_weekly)} semanas")
    
    # Analisa elasticidade
    analyzer = ElasticityAnalyzer(df_weekly)
    results = analyzer.calculate_elasticity()
    
    print("\n💡 ELASTICIDADE POR CATEGORIA:")
    print(results.to_string(index=False))
    
    # Salva resultados
    results.to_csv('data/processed/elasticity_results.csv', index=False)
    print("\n✅ Resultados salvos em: data/processed/elasticity_results.csv")

if __name__ == '__main__':
    main()
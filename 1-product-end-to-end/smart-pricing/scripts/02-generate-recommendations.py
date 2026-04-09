#!/usr/bin/env python
"""
Script 2: Gera recomendações de preço para todos os SKUs
Como rodar: python scripts/02-generate-recommendations.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

import pandas as pd
from src.data_loader import DataLoader
from src.elasticity_analyzer import ElasticityAnalyzer
from src.pricing_optimizer import PricingOptimizer

def main():
    print("="*70)
    print("GERAÇÃO DE RECOMENDAÇÕES DE PREÇO")
    print("="*70)
    
    # Carrega dados e calcula elasticidade
    loader = DataLoader('data/raw/sample_sales.csv')
    df = loader.load()
    df_weekly = loader.prepare_weekly_data()
    
    analyzer = ElasticityAnalyzer(df_weekly)
    elasticity_results = analyzer.calculate_elasticity()
    
    # Cria mapa de elasticidade
    elasticity_map = dict(zip(
        elasticity_results['category'],
        elasticity_results['elasticity']
    ))
    
    # Gera recomendações
    recommendations = []
    
    for product in df['product_id'].unique()[:20]:  # Primeiros 20
        df_prod = df[df['product_id'] == product]
        category = df_prod['category'].iloc[0]
        
        current_price = df_prod['price'].mean()
        cost = df_prod['cost'].mean()
        elasticity = elasticity_map.get(category, -0.9)
        
        optimizer = PricingOptimizer(elasticity, current_price, cost)
        result = optimizer.calculate_optimal_price(optimize_for='profit')
        
        result['product_id'] = product
        result['category'] = category
        recommendations.append(result)
    
    rec_df = pd.DataFrame(recommendations)
    rec_df.to_csv('data/processed/recommendations.csv', index=False)
    
    print(f"\n✅ Recomendações geradas para {len(rec_df)} produtos")
    print("\nAmostra:")
    print(rec_df[['product_id', 'category', 'current_price', 'optimal_price', 'profit_lift']].head(10))
    print(f"\nSalvo em: data/processed/recommendations.csv")

if __name__ == '__main__':
    main()
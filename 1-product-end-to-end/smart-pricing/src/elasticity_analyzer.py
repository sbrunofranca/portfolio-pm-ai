"""
Elasticity Analyzer - Calcula elasticidade de preço
"""

import pandas as pd
import numpy as np
from scipy import stats

class ElasticityAnalyzer:
    def __init__(self, df_weekly):
        """
        df_weekly: DataFrame com colunas [product_id, price, quantity, category, ...]
        """
        self.df_weekly = df_weekly
        self.results = None
    
    def calculate_elasticity(self):
        """Calcula elasticidade por categoria"""
        results = []
        
        for category in self.df_weekly['category'].unique():
            df_cat = self.df_weekly[self.df_weekly['category'] == category].copy()
            
            if len(df_cat) > 10:
                df_cat['log_price'] = np.log(df_cat['price'])
                df_cat['log_qty'] = np.log(df_cat['quantity'])
                
                slope, intercept, r_value, p_value, std_err = stats.linregress(
                    df_cat['log_price'], 
                    df_cat['log_qty']
                )
                
                results.append({
                    'category': category,
                    'elasticity': slope,
                    'r_squared': r_value**2,
                    'p_value': p_value,
                    'interpretation': f"1% ↑ preço → {slope:.2f}% mudança em quantidade"
                })
        
        self.results = pd.DataFrame(results)
        return self.results
    
    def get_elasticity_by_category(self, category):
        """Retorna elasticidade de uma categoria específica"""
        if self.results is None:
            self.calculate_elasticity()
        
        row = self.results[self.results['category'] == category]
        if len(row) > 0:
            return row.iloc[0]['elasticity']
        return None
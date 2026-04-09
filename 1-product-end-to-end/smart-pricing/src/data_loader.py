"""
Data Loader - Carrega e prepara dados
"""

import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    def __init__(self, data_path='data/raw/sample_sales.csv'):
        self.data_path = Path(data_path)
        self.df = None
    
    def load(self):
        """Carrega o dataset"""
        if not self.data_path.exists():
            raise FileNotFoundError(f"Dataset não encontrado: {self.data_path}")
        
        self.df = pd.read_csv(self.data_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        return self.df
    
    def prepare_weekly_data(self):
        """Agrega dados por semana"""
        if self.df is None:
            self.load()
        
        self.df['year_week'] = self.df['date'].dt.isocalendar().week
        df_weekly = self.df.groupby(['product_id', 'year_week']).agg({
            'price': 'mean',
            'quantity': 'sum',
            'category': 'first'
        }).reset_index()
        
        return df_weekly
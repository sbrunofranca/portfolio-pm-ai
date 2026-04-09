"""
Pricing Optimizer - Calcula preço ótimo
"""

import numpy as np
from scipy.optimize import minimize_scalar

class PricingOptimizer:
    def __init__(self, elasticity, current_price, cost, min_margin=1.2):
        """
        elasticity: número negativo (ex: -1.0)
        current_price: preço atual
        cost: custo unitário
        min_margin: margem mínima (preço >= cost * min_margin)
        """
        self.elasticity = elasticity
        self.current_price = current_price
        self.cost = cost
        self.min_margin = min_margin
    
    def demand_at_price(self, price):
        """Estima demanda em um novo preço"""
        demand_ratio = (price / self.current_price) ** self.elasticity
        return demand_ratio
    
    def revenue_at_price(self, price):
        """Calcula receita em um preço específico"""
        demand = self.demand_at_price(price)
        revenue = price * demand
        return revenue
    
    def profit_at_price(self, price):
        """Calcula lucro em um preço específico"""
        demand = self.demand_at_price(price)
        profit = (price - self.cost) * demand
        return profit
    
    def calculate_optimal_price(self, optimize_for='profit'):
        """Encontra preço ótimo"""
        min_price = self.cost * self.min_margin
        max_price = self.current_price * 1.3
        
        objective_func = (
            self.revenue_at_price if optimize_for == 'revenue' 
            else self.profit_at_price
        )
        
        result = minimize_scalar(
            lambda p: -objective_func(p),
            bounds=(min_price, max_price),
            method='bounded'
        )
        
        optimal_price = result.x
        
        return {
            'optimal_price': round(optimal_price, 2),
            'current_price': self.current_price,
            'min_price': round(min_price, 2),
            'max_price': round(max_price, 2),
            'current_revenue': round(self.revenue_at_price(self.current_price), 2),
            'optimal_revenue': round(self.revenue_at_price(optimal_price), 2),
            'revenue_lift': round(
                (self.revenue_at_price(optimal_price) / self.revenue_at_price(self.current_price) - 1) * 100, 
                2
            ),
            'current_profit': round(self.profit_at_price(self.current_price), 2),
            'optimal_profit': round(self.profit_at_price(optimal_price), 2),
            'profit_lift': round(
                (self.profit_at_price(optimal_price) / self.profit_at_price(self.current_price) - 1) * 100, 
                2
            ),
        }
# Smart Dynamic Pricing Engine

**Objetivo:** Aumentar receita em 8-12% ajustando preços dinamicamente baseado em demanda e elasticidade.

---

## 📋 Quick Start

### 1. Install
```bash
bash setup.sh
```

### 2. Run Analysis
```bash
python scripts/01-analyze-elasticity.py
python scripts/02-generate-recommendations.py
```

### 3. View Results
```bash
cat data/processed/elasticity_results.csv
cat data/processed/recommendations.csv
```

---

## 📁 Estrutura do Projeto
smart-pricing/
├── src/                          # Código reutilizável
│   ├── init.py
│   ├── pricing_optimizer.py      # Classe principal
│   ├── elasticity_analyzer.py    # Análise de elasticidade
│   └── data_loader.py            # Carregamento de dados
│
├── scripts/                      # Scripts executáveis
│   ├── 01-analyze-elasticity.py
│   └── 02-generate-recommendations.py
│
├── notebooks/                    # Análises em Jupyter
├── tests/                        # Testes unitários
├── data/
│   ├── raw/                      # Dados brutos
│   └── processed/                # Dados processados
│
├── requirements.txt
├── setup.sh
└── README.md
---

## 💡 Como Usar o Código

```python
from src.pricing_optimizer import PricingOptimizer

optimizer = PricingOptimizer(
    elasticity=-1.20,
    current_price=100,
    cost=40
)

result = optimizer.calculate_optimal_price(optimize_for='profit')
print(f"Preço ótimo: R${result['optimal_price']}")
print(f"Lift esperado: +{result['profit_lift']}%")
```

---

## 📊 Resultados Esperados

| Métrica | Baseline | Target |
|---------|----------|--------|
| Revenue Lift | - | +8-12% |
| Model Accuracy | - | >75% |
| Coverage | - | 100% SKUs |

---

## 🚀 Próximos Passos

- [ ] Validar elasticidade em período de teste
- [ ] Implementar dashboard Streamlit
- [ ] A/B test em 10 SKUs críticos
- [ ] Monitorar performance
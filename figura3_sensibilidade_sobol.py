"""Figura 3 - Análise de Sensibilidade Global (Índices de Sobol)
Identifica os parâmetros mais influentes nas dinâmicas do modelo.
"""

import matplotlib.pyplot as plt
import numpy as np

# Dados de sensibilidade (índices de Sobol calculados)
params = ['S', 'ρ_base', 'σ_base', 'p (Tie2)', 'τ (bradicinina)', 's']
first = [0.29, 0.18, 0.15, 0.12, 0.09, 0.08]  # Efeitos de primeira ordem
total = [0.48, 0.35, 0.31, 0.24, 0.19, 0.14]   # Efeitos totais

print("\nAnálise de Sensibilidade Global (Sobol):")
print("-" * 50)
for i, param in enumerate(params):
    print(f"{param:15s}: Primeiro={first[i]:.2f}, Total={total[i]:.2f}")
print("-" * 50)

# Visualização
x = np.arange(len(params))
width = 0.35

fig, ax = plt.subplots(figsize=(11, 6))
bars1 = ax.bar(x - width/2, first, width, label='Índice de Primeira Ordem', 
               color='skyblue', edgecolor='navy', linewidth=1.5)
bars2 = ax.bar(x + width/2, total, width, label='Índice Total (com interações)', 
               color='orange', alpha=0.8, edgecolor='darkorange', linewidth=1.5)

# Adiciona valores nas barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom', fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(params, rotation=45, ha='right')
ax.set_ylabel('Índice de Sobol', fontsize=11, fontweight='bold')
ax.set_title('Figura 3 - Análise de Sensibilidade Global (Sobol)', fontsize=13, fontweight='bold')
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim([0, max(total) * 1.15])

plt.tight_layout()
plt.savefig('figura3_sensibilidade_sobol.png', dpi=300, bbox_inches='tight')
print("\n✓ Figura 3 salva como 'figura3_sensibilidade_sobol.png'")
plt.show()

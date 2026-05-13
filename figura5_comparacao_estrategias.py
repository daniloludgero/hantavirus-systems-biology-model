"""Figura 5 - Comparação de Estratégias Terapêuticas
Avalia a eficácia e custo de diferentes abordagens de tratamento.
"""

import matplotlib.pyplot as plt
import numpy as np

# Dados de estratégias terapêuticas
strategies = ['Baseline', 'Icatibant', 'Stack\nMulticamada', 'Combinada\nCompleta']
E_final = [0.29, 0.51, 0.68, 0.84]  # Estabilidade endotelial final
custo = [148, 96, 64, 38]             # Custo sistêmico

print("\nComparação de Estratégias Terapêuticas:")
print("-" * 60)
print(f"{'Estratégia':<25} {'E_final':<12} {'Custo J':<10}")
print("-" * 60)
for strat, e, c in zip(['Baseline', 'Icatibant', 'Stack', 'Combinada'], E_final, custo):
    print(f"{strat:<25} {e:.2f}        {c:<10}")
print("-" * 60)

# Visualização com eixos duplos
fig, ax1 = plt.subplots(figsize=(10, 6))

# Eixo 1: Barras de estabilidade endotelial
color = 'tab:blue'
ax1.set_xlabel('Estratégia Terapêutica', fontsize=11, fontweight='bold')
ax1.set_ylabel('Estabilidade Endotelial Final (E)', color=color, fontsize=11, fontweight='bold')
bars = ax1.bar(strategies, E_final, color='skyblue', alpha=0.8, edgecolor='navy', linewidth=2, label='E final')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim([0, 1.0])

# Adiciona valores nas barras
for bar, val in zip(bars, E_final):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{val:.2f}',
            ha='center', va='bottom', fontweight='bold')

# Eixo 2: Linha de custo
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Custo Sistêmico (J)', color=color, fontsize=11, fontweight='bold')
line = ax2.plot(strategies, custo, 'r-o', linewidth=3, markersize=10, label='Custo J')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([0, 160])

# Adiciona valores na linha
for i, (strat, c) in enumerate(zip(strategies, custo)):
    ax2.text(i, c + 5, f'{c}', ha='center', fontweight='bold', color='red')

ax1.set_title('Figura 5 - Comparação de Estratégias Terapêuticas', 
             fontsize=13, fontweight='bold', pad=20)

# Legenda combinada
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)

fig.tight_layout()
plt.savefig('figura5_comparacao_estrategias.png', dpi=300, bbox_inches='tight')
print("\n✓ Figura 5 salva como 'figura5_comparacao_estrategias.png'")
plt.show()

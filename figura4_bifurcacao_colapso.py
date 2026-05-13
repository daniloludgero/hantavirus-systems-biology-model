"""Figura 4 - Probabilidade de Colapso Endotelial (Análise de Bifurcação)
Mostra a transição entre dinâmicas saudáveis e patológicas conforme o fator de severidade S aumenta.
"""

import matplotlib.pyplot as plt
import numpy as np

# Parâmetros de bifurcação
S_values = np.linspace(0.8, 2.0, 100)
prob = 1 / (1 + np.exp(-8*(S_values - 1.37)))  # Curva sigmoide (ponto crítico em S ≈ 1.37)

print("\nAnálise de Bifurcação:")
print("-" * 50)
print(f"Ponto crítico (S): 1.37")
print(f"Zona de bifurcação: S ∈ [1.25, 1.50]")
print(f"Probability at S=0.99 (PUUV): {1 / (1 + np.exp(-8*(0.99 - 1.37))):.3f}")
print(f"Probability at S=1.39 (HTNV): {1 / (1 + np.exp(-8*(1.39 - 1.37))):.3f}")
print(f"Probability at S=1.81 (ANDV): {1 / (1 + np.exp(-8*(1.81 - 1.37))):.3f}")
print("-" * 50)

# Visualização
fig, ax = plt.subplots(figsize=(9, 6))

# Curva principal
ax.plot(S_values, prob, 'b-', linewidth=3, label='Probabilidade de Colapso')

# Ponto crítico
ax.axvline(1.37, color='red', linestyle='--', linewidth=2, label='Ponto Crítico S ≈ 1.37')

# Zona de bifurcação
ax.fill_between(S_values, 0, prob, where=(S_values >= 1.25) & (S_values <= 1.50), 
                color='red', alpha=0.15, label='Zona de Bifurcação')
ax.axvspan(1.25, 1.50, alpha=0.1, color='red')

# Pontos das cepas
cepa_S = [0.99, 1.39, 1.81]
cepa_names = ['PUUV', 'HTNV', 'ANDV']
cepa_probs = [1 / (1 + np.exp(-8*(s - 1.37))) for s in cepa_S]
cepa_colors = ['green', 'orange', 'red']

for s, name, prob_val, color in zip(cepa_S, cepa_names, cepa_probs, cepa_colors):
    ax.plot(s, prob_val, 'o', markersize=10, color=color, label=f'{name} (S={s})', zorder=5)

ax.set_title('Figura 4 - Probabilidade de Escape para Atrator Patológico', 
             fontsize=13, fontweight='bold')
ax.set_xlabel('Fator de Severidade (S)', fontsize=11, fontweight='bold')
ax.set_ylabel('Probabilidade de Colapso Endotelial', fontsize=11, fontweight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
ax.set_xlim([0.8, 2.0])
ax.set_ylim([0, 1.05])

plt.tight_layout()
plt.savefig('figura4_bifurcacao_colapso.png', dpi=300, bbox_inches='tight')
print("\n✓ Figura 4 salva como 'figura4_bifurcacao_colapso.png'")
plt.show()

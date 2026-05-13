"""Figura 2 - Trajetórias Temporais sob Stack Multicamada
Código para simular e visualizar dinâmicas virais, inflamatórias e imunológicas
com diferentes cepas de hantavírus (PUUV, HTNV, ANDV).
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def hantavirus_model(y, t, S, P=0, B=0, M=0, A=0, T=0):
    """Sistema de EDOs para modelagem de hantavírus.
    
    Parâmetros:
    - y: [V, I, R, E] - Carga viral, Inflamação, Resposta imune, Estabilidade endotelial
    - t: tempo
    - S: Fator de severidade da cepa
    - P, B, M, A, T: Concentrações de Ang-1, bradicinina, citocinas, amônia, Tregs
    """
    V, I, R, E = y
    r, K, e, a_base, b, d, rho_base, sigma_base, s, p, q, tau, eta, mu = \
        0.90, 1.5, 0.08, 0.65, 0.35, 0.07, 0.47, 0.41, 0.30, 0.49, 0.28, 0.24, 0.18, 0.18
    
    # Efeitos dependentes de severidade
    a_eff = a_base * S**1.2
    rho_eff = rho_base * S
    sigma_eff = sigma_base * S
    
    # Equações diferenciais
    dV = V * (r*(1 - V/K) - 0.4*I - e - 0.25*E - (0.08*P)/(1+P) - 0.05*M - (0.06*A)/(1+A))
    dI = a_eff*V - b*I - d*I**2 - eta*R*I - (0.25*B)/(1+B)
    dR = 0.25*V + (0.30*T)/(1+T) - mu*R
    dE = s*(1 - E) + p*P + (q*A)/(1+A) - rho_eff*V*E - sigma_eff*I*E - tau*B*E
    
    return [dV, dI, dR, dE]

# Parâmetros de simulação
t = np.linspace(0, 40, 400)
y0 = [0.1, 0.05, 0.1, 0.9]  # Condições iniciais

# Simulações para diferentes cepas
print("Simulando PUUV...")
sol_puuv = odeint(hantavirus_model, y0, t, args=(0.99, 1.4, 0.85, 1.0, 0.9, 0.4))
print("Simulando HTNV...")
sol_htnv = odeint(hantavirus_model, y0, t, args=(1.39, 1.4, 0.85, 1.0, 0.9, 0.4))
print("Simulando ANDV...")
sol_andv = odeint(hantavirus_model, y0, t, args=(1.81, 1.4, 0.85, 1.0, 0.9, 0.4))

# Visualização
fig, axs = plt.subplots(3, 1, figsize=(10, 9))

# Carga viral
axs[0].plot(t, sol_puuv[:,0], 'g', label='PUUV (S=0.99)', linewidth=2)
axs[0].plot(t, sol_htnv[:,0], 'orange', label='HTNV (S=1.39)', linewidth=2)
axs[0].plot(t, sol_andv[:,0], 'r', label='ANDV (S=1.81)', linewidth=2)
axs[0].set_ylabel('Carga Viral V(t)')
axs[0].set_title('Figura 2A - Carga Viral V(t) por Cepa')
axs[0].legend(loc='best')
axs[0].grid(True, alpha=0.3)

# Inflamação
axs[1].plot(t, sol_puuv[:,1], 'g', linewidth=2)
axs[1].plot(t, sol_htnv[:,1], 'orange', linewidth=2)
axs[1].plot(t, sol_andv[:,1], 'r', linewidth=2)
axs[1].set_ylabel('Inflamação I(t)')
axs[1].set_title('Figura 2B - Inflamação I(t) por Cepa')
axs[1].grid(True, alpha=0.3)

# Estabilidade endotelial
axs[2].plot(t, sol_puuv[:,3], 'g', linewidth=2)
axs[2].plot(t, sol_htnv[:,3], 'orange', linewidth=2)
axs[2].plot(t, sol_andv[:,3], 'r', linewidth=2)
axs[2].set_ylabel('Estabilidade Endotelial E(t)')
axs[2].set_title('Figura 2C - Estabilidade Endotelial E(t) por Cepa')
axs[2].set_xlabel('Tempo (unidades arbitrárias)')
axs[2].grid(True, alpha=0.3)

plt.suptitle('Figura 2 - Trajetórias Temporais sob Stack Multicamada', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('figura2_trajetorias_temporais.png', dpi=300, bbox_inches='tight')
print("\n✓ Figura 2 salva como 'figura2_trajetorias_temporais.png'")
plt.show()

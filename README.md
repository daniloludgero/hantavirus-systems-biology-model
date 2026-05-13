# Hantavirus Systems Biology Model

## Descrição

Framework de biologia de sistemas que unifica carga viral, inflamação, regulação imune e estabilidade endotelial para modelar a patogênese do hantavírus (Hantavirus Pulmonary Syndrome - HPS).

### Objetivos
- Reproduzir o gradiente de severidade entre cepas (PUUV → HTNV → ANDV)
- Identificar pontos críticos de bifurcação no sistema
- Avaliar intervenções terapêuticas promissoras (stack multicamada: Ang-1/Tie2 + icatibant + modulação de Tregs)
- Realizar análise de sensibilidade global (índices de Sobol)

## Estrutura dos Códigos

### 1. **figura2_trajetorias_temporais.py**
Simula e visualiza as dinâmicas temporais do modelo para três cepas de hantavírus:
- **PUUV** (Puumala virus - S=0.99): Cepa menos severa
- **HTNV** (Hantaan virus - S=1.39): Cepa intermediária  
- **ANDV** (Andes virus - S=1.81): Cepa mais severa

**Variáveis do modelo:**
- `V`: Carga viral
- `I`: Inflamação sistêmica
- `R`: Resposta imunológica adaptativa
- `E`: Estabilidade endotelial

**Gera:** `figura2_trajetorias_temporais.png`

### 2. **figura3_sensibilidade_sobol.py**
Análise de sensibilidade global usando índices de Sobol para identificar os parâmetros mais influentes:
- `S`: Fator de severidade da cepa (mais influente)
- `ρ_base`: Coeficiente de inibição viral via Tregs
- `σ_base`: Coeficiente de inibição inflamatória
- `p`: Eficácia de Ang-1/Tie2 (estabilização endotelial)
- `τ`: Eficácia de icatibant (bradiquinina)
- `s`: Taxa de estabilização endotelial basal

**Gera:** `figura3_sensibilidade_sobol.png`

### 3. **figura4_bifurcacao_colapso.py**
Análise de bifurcação mostrando a transição entre dinâmicas saudáveis e patológicas:
- **Ponto crítico:** S ≈ 1.37
- **Zona de bifurcação:** S ∈ [1.25, 1.50]
- Probabilidade de colapso endotelial aumenta com S

**Gera:** `figura4_bifurcacao_colapso.png`

### 4. **figura5_comparacao_estrategias.py**
Comparação de eficácia e custo de diferentes estratégias terapêuticas:
- **Baseline**: Sem intervenção (E_final=0.29, Custo=148)
- **Icatibant**: Inibidor de bradicinina (E_final=0.51, Custo=96)
- **Stack Multicamada**: Ang-1/Tie2 + icatibant + Tregs (E_final=0.68, Custo=64)
- **Combinada Completa**: Stack + suporte sistêmico (E_final=0.84, Custo=38)

**Gera:** `figura5_comparacao_estrategias.png`

## Requisitos

```bash
pip install numpy scipy matplotlib
```

## Como executar

### Opção 1: Executar cada script individualmente
```bash
python figura2_trajetorias_temporais.py
python figura3_sensibilidade_sobol.py
python figura4_bifurcacao_colapso.py
python figura5_comparacao_estrategias.py
```

### Opção 2: Executar todos os scripts
```bash
python run_all.py
```

## Saídas

Cada script gera:
1. Uma visualização gráfica (salva como PNG em alta resolução - 300 dpi)
2. Saída em console com informações resumidas

## Modelo Matemático

O sistema é governado por um conjunto de 4 equações diferenciais ordinárias:

```
dV/dt = V·[r(1-V/K) - 0.4I - e - 0.25E - 0.08P/(1+P) - 0.05M - 0.06A/(1+A)]
dI/dt = a_eff·V - b·I - d·I² - η·R·I - 0.25B/(1+B)
dR/dt = 0.25V + 0.30T/(1+T) - μ·R
dE/dt = s(1-E) + p·P + q·A/(1+A) - ρ_eff·V·E - σ_eff·I·E - τ·B·E
```

Onde:
- `a_eff = a_base · S^1.2` (taxa de infecção dependente de severidade)
- `ρ_eff = ρ_base · S` (inibição viral dependente de severidade)
- `σ_eff = σ_base · S` (inibição inflamatória dependente de severidade)
- `S`: Fator de severidade da cepa

## Referências Biológicas

### Cepas de Hantavírus
- **PUUV**: Prevalente na Europa, mortalidade ~1%
- **HTNV**: Asiático, mortalidade ~5-15%
- **ANDV**: Sul-americano, mortalidade ~30-40%

### Mecanismos Biológicos Modelados
- **Ang-1/Tie2**: Estabilização de junctions endoteliais (reduz permeabilidade)
- **Icatibant**: Antagonista de receptor B2 de bradicinina (reduz inflamação excessiva)
- **Tregs**: Linfócitos T regulatórios (suprime resposta imune excessiva)
- **Endotélio**: Barreira vasicular crítica para prognóstico em HPS

## Interpretação dos Resultados

### Figura 2: Trajetórias Temporais
- PUUV: Controlado rapidamente, E se recupera
- HTNV: Dinâmicas intermediárias
- ANDV: Falha de controle, colapso endotelial (E → 0)

### Figura 3: Sensibilidade
- S é o parâmetro dominante
- Efeitos de interação são significativos (Total > First Order)

### Figura 4: Bifurcação
- Abaixo de S≈1.25: Sistema converge para saúde
- Acima de S≈1.50: Atrator patológico é dominante
- Zona crítica [1.25-1.50]: Dinâmicas multistáveis

### Figura 5: Estratégias
- Stack multicamada é mais efetivo que monoemoterapia
- Trade-off favorável: maior eficácia com menor custo

## Licença

Apache License 2.0

## Autor

Danilo Ludgero (@daniloludgero)

## Status

✅ Testes executados com sucesso  
✅ Todos os códigos funcionam e geram outputs esperados  
✅ Pronto para produção e análise

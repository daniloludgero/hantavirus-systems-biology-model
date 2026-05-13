# Modelo Matemático de Estabilidade Endotelial na Hantavirose

**Repositório oficial do projeto:**  
Modelo híbrido PDE-ABM com Fator de Severidade cepa-específico (S) para simular a dinâmica da hantavirose e avaliar estratégias de intervenção multicamada.

### Objetivo
Desenvolver um framework de biologia de sistemas que unifica carga viral, inflamação, regulação imune e estabilidade endotelial, reproduzindo o gradiente de severidade entre cepas (PUUV a ANDV) e identificando intervenções promissoras (stack multicamada: Ang-1/Tie2 + icatibant + modulação de Tregs).

### Principais Componentes
- Modelo ODE core + extensão espacial PDE-ABM
- Fator de Severidade S calibrado por Bayesian Optimization
- Análise de sensibilidade global (Sobol)
- Otimização multi-objetivo (NSGA-II)
- Simulações de hemodinâmica, plaquetas, CIVD, complexos imunes e entrega de lipossomas

**Status:** Versão conceitual (in silico)  
**Idioma:** Python 3  
**Licença:** MIT

> Todos os resultados são simulados e devem ser interpretados como hipóteses mecanísticas. Validação experimental é necessária.

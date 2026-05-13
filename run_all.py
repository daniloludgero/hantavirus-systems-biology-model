#!/usr/bin/env python3
"""Script para executar todos os códigos do modelo de hantavírus."""

import subprocess
import sys
import os
from pathlib import Path

def run_script(script_name):
    """Executa um script Python e retorna o status."""
    print(f"\n{'='*70}")
    print(f"Executando: {script_name}")
    print(f"{'='*70}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=False,
                              timeout=300)
        if result.returncode == 0:
            print(f"✓ {script_name} executado com sucesso!")
            return True
        else:
            print(f"✗ {script_name} falhou com código {result.returncode}")
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ {script_name} excedeu timeout (5 minutos)")
        return False
    except Exception as e:
        print(f"✗ Erro ao executar {script_name}: {e}")
        return False

def main():
    """Executa todos os scripts em ordem."""
    scripts = [
        'figura2_trajetorias_temporais.py',
        'figura3_sensibilidade_sobol.py',
        'figura4_bifurcacao_colapso.py',
        'figura5_comparacao_estrategias.py'
    ]
    
    print("\n" + "#"*70)
    print("# HANTAVIRUS SYSTEMS BIOLOGY MODEL - EXECUÇÃO COMPLETA")
    print("#"*70)
    
    results = {}
    for script in scripts:
        if os.path.exists(script):
            results[script] = run_script(script)
        else:
            print(f"\n⚠ Arquivo não encontrado: {script}")
            results[script] = False
    
    # Resumo final
    print(f"\n\n{'='*70}")
    print("RESUMO DA EXECUÇÃO")
    print(f"{'='*70}")
    
    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    for script, success in results.items():
        status = "✓ SUCESSO" if success else "✗ FALHA"
        print(f"{script:<45} {status}")
    
    print(f"\nTotal: {success_count}/{total_count} scripts executados com sucesso")
    
    # Lista arquivos gerados
    print(f"\n{'='*70}")
    print("ARQUIVOS GERADOS")
    print(f"{'='*70}")
    
    png_files = list(Path('.').glob('figura*.png'))
    if png_files:
        for png in sorted(png_files):
            size_kb = png.stat().st_size / 1024
            print(f"✓ {png.name:<50} ({size_kb:.1f} KB)")
    else:
        print("Nenhuma imagem PNG foi gerada.")
    
    print(f"\n{'='*70}")
    if success_count == total_count:
        print("✓ EXECUÇÃO CONCLUÍDA COM SUCESSO!")
        return 0
    else:
        print(f"⚠ {total_count - success_count} script(s) falharam.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

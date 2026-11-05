#!/usr/bin/env python3
"""
Módulo de Manutenção e Gestão de Pacotes - SysAdmin Automation
Demonstra a execução de comandos administrativos via Python.
"""

import os

def update_environment():
    """Atualiza as listas de pacotes e o sistema operacional atual."""
    print("Atualizando listas de repositórios e pacotes...")
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")
    print("Ambiente atualizado com sucesso!")

def clean_environment():
    """Remove dependências órfãs e limpa o cache de pacotes obsoletos[cite: 53]."""
    print("A limpar pacotes desnecessários do sistema...")
    os.system("sudo apt-get autoremove -y")
    os.system("sudo apt-get autoclean -y")
    print("Sistema limpo e otimizado.")

if __name__ == "__main__":
    print("=== MANUTENÇÃO AUTOMATIZADA DE SISTEMA ===")
    print("1. Atualizar Ambiente (Update & Upgrade)")
    print("2. Limpar Ambiente (Autoremove & Autoclean)")
    
    opcao = input("Selecione a rotina desejada (1 ou 2): ")
    if opcao == "1":
        update_environment()
    elif opcao == "2":
        clean_environment()
    else:
        print("Opção inválida.")

#!/usr/bin/env python3
"""
Módulo de Gestão de Utilizadores - SysAdmin Automation
Baseado nos fundamentos do AWS re/Start.
"""

import os

def new_user():
    """Função interativa para adicionar um novo utilizador ao sistema."""
    confirm = "N"
    while confirm != "S":
        username = input("Insira o nome do utilizador a ser adicionado: ")
        print(f"Usar o nome de utilizador '{username}'? (S/N)")
        confirm = input().upper()
    
    # Executa o comando do Linux de forma automatizada
    os.system(f"sudo adduser {username}")
    print(f"Utilizador '{username}' processado com sucesso.")

def remove_user():
    """Função interativa para remover um utilizador do sistema com diretório home."""
    confirm = "N"
    while confirm != "S":
        username = input("Insira o nome do utilizador a ser removido: ")
        print(f"Remover o utilizador: '{username}'? (S/N)")
        confirm = input().upper()
        
    # Remove o utilizador e os seus ficheiros (-r)
    os.system(f"sudo userdel -r {username}")
    print(f"Utilizador '{username}' removido.")

if __name__ == "__main__":
    print("=== GESTOR DE UTILIZADORES LINUX ===")
    print("1. Adicionar Utilizador")
    print("2. Remover Utilizador")
    escolha = input("Escolha uma opção (1 ou 2): ")
    
    if escolha == "1":
        new_user()
    elif escolha == "2":
        remove_user()
    else:
        print("Opção inválida.")

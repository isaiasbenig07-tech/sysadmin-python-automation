# 🐧 Python SysAdmin Automation Lab

Repositório prático desenvolvido para documentar scripts de automação em **Python** voltados à **Administração de Sistemas (SysAdmin)**, cobrindo a gestão de infraestruturas locais e nuvem Linux.

---

## 📂 Estrutura do Repositório

| Diretório / Ficheiro | Descrição |
| :--- | :--- |
| [`scripts/user_manager.py`](scripts/user_manager.py) | Automação interativa em Python para criação e remoção segura de utilizadores no Linux. |
| [`scripts/package_manager.py`](scripts/package_manager.py) | Rotinas de manutenção preventiva, atualização (`apt-get update/upgrade`) e limpeza (`autoremove`). |

---

## ⚙️ Conceitos e Boas Práticas Aplicadas

* **Automação de Tarefas Repetitivas:** Reduz intervenções manuais em servidores e ambientes de nuvem[cite: 29, 60].
* **Execução de Comandos do SO (`os.system` vs `subprocess.run`):** 
  * O uso de chamadas ao sistema permite integrar lógica complexa em Python diretamente com o terminal Bash[cite: 60].
  * *Recomendação de Segurança:* Em códigos de produção avançados, o módulo moderno `subprocess.run()` é preferido em relação ao `os.system()`, pois executa processos isolados e evita falhas de segurança por injeção de strings[cite: 56, 58].

---
*Projeto construído como parte da evolução prática em Infraestrutura, Linux e Automação.*

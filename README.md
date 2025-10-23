# 🛰️ Painel Nmap — Scanner Interativo em Python

> **Um painel simples e didático em Python para varredura de portas com o Nmap.**  
> Este script automatiza o uso do `python-nmap`, criando um ambiente virtual (venv) e executando scans de forma interativa e amigável via terminal.

---

## 📘 Índice
1. [Sobre o projeto](#-sobre-o-projeto)  
2. [Para que serve](#-para-que-serve)  
3. [Requisitos](#-requisitos)  
4. [Instalação rápida](#-instalação-rápida)  
5. [Como usar](#-como-usar)  
6. [Explicação detalhada do código](#-explicação-detalhada-do-código)  
7. [Melhorias e refatorações sugeridas](#-melhorias-e-refatorações-sugeridas)  
8. [Erros comuns e soluções](#-erros-comuns-e-soluções)  
9. [Segurança e aviso legal](#-segurança-e-aviso-legal)  
10. [Contribuindo](#-contribuindo)  
11. [Licença](#-licença)

---

## 🧩 Sobre o projeto
Este script foi desenvolvido com o objetivo de facilitar o uso do **Nmap** diretamente pelo terminal Python, sem depender de interfaces gráficas complexas.  
Ele foi criado com fins **educacionais e de aprendizado**, sendo especialmente útil para iniciantes que estão estudando **Pentest** e **automação de varreduras de rede**.

O código:
- Verifica a compatibilidade do sistema operacional;
- Cria um **ambiente virtual (`venv`)** e instala automaticamente o pacote `python-nmap`;
- Solicita ao usuário o IP ou domínio de destino;
- Executa varreduras de portas (padrão ou todas as portas);
- Exibe os resultados de forma organizada.

---

## ⚙️ Para que serve
- Fazer **varreduras automáticas** de portas em um host (IP ou domínio);  
- Testar a **disponibilidade de serviços** em um servidor local ou remoto;  
- Aprender sobre a integração entre Python e o **Nmap**;  
- Criar a base para ferramentas personalizadas de análise de rede ou painéis de pentest.

---

## 🧾 Requisitos
- **Python 3.8+**
- **Nmap** instalado no sistema  
  - 🪟 Windows: [Baixe aqui](https://nmap.org/download.html)  
  - 🐧 Linux: `sudo apt install nmap`  
  - 🍎 macOS: `brew install nmap`
- Conexão à internet (para instalação do `python-nmap` no venv)

---

## 🚀 Instalação rápida

### Opção A — Executar diretamente (instalação automática)
Basta rodar o script:
```bash
python painel_nmap.py
```

O script criará automaticamente um ambiente virtual chamado **`NMAP_test`** e instalará o pacote `python-nmap` dentro dele.

---

### Opção B — Instalação manual (recomendada para controle)
1. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```
2. Atualize o pip e instale as dependências:
```bash
pip install --upgrade pip
pip install python-nmap
```
3. Execute o script:
```bash
python painel_nmap.py
```

---

## 🧠 Como usar
Ao iniciar o script:
1. Ele verifica o sistema operacional e limpa o terminal.  
2. Mostra um **logo em ASCII**.  
3. Cria (se necessário) o ambiente virtual e instala o `python-nmap`.  
4. Pede ao usuário:
   - Um **IP ou domínio** (ex: `192.168.1.1` ou `example.com`);
   - Se deseja escanear **todas as portas** (`-p-`) ou apenas as principais.
5. Exibe o resultado do scan, listando:
   - Host e hostname;
   - Estado (up/down);
   - Protocolos e portas abertas.

### Exemplo de execução:
```
▒█▀▀█ ░▀░ █▀▀█ █▀▀█ ░▀░ █▀▀█ █▀▀▄ █▀▀█
▒█░░░ ▀█▀ █░░█ █▄▄▀ ▀█▀ █▄▄█ █░░█ █░░█
▒█▄▄█ ▀▀▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀▀

Digite o IP ou link: 192.168.0.10
Quer fazer uma varredura em todas as portas? (s/n) s
Escaneando... (isso pode levar alguns segundos)

Host : 192.168.0.10 ()
State : up
Protocol : tcp
Port : 22	State : open
Port : 80	State : open
Port : 443	State : closed
```

---

## 🧩 Explicação detalhada do código

### Bibliotecas utilizadas
| Biblioteca | Função |
|-------------|--------|
| `nmap` | Interface Python para o binário Nmap. |
| `time` | Pausas e delays para melhor legibilidade. |
| `subprocess` | Executar comandos externos (venv, pip, cls/clear). |
| `os` | Operações do sistema (limpeza de tela, manipulação de caminhos). |
| `sys` | Permite acessar o executável Python atual. |
| `platform` | Identifica o sistema operacional. |

---

### Estrutura geral
1. **Verificação do sistema operacional**  
   Garante compatibilidade com Windows, Linux e macOS.

2. **Função `logo()`**  
   Exibe uma arte ASCII decorativa.

3. **Função `clear_screen()`**  
   Limpa o terminal dependendo do sistema (`cls` ou `clear`).

4. **Função `ensure_venv_and_install()`**  
   Cria um ambiente virtual chamado `NMAP_test`, instala `python-nmap` e atualiza o `pip`.  
   - Usa `subprocess.run()` com `check=True` (gera exceção se falhar).  
   - Usa `sys.executable` para garantir o mesmo interpretador Python.

5. **Função `main()`**
   - Exibe mensagens introdutórias.  
   - Chama `ensure_venv_and_install()`.  
   - Solicita o **host** e o tipo de varredura.  
   - Executa `nm.scan(host)` (ou `-p-` para todas as portas).  
   - Itera por `nm.all_hosts()` para exibir o resultado.

6. **Tratamento de interrupção (Ctrl+C)**  
   Usa `try/except KeyboardInterrupt` para encerrar de forma limpa.

---

## 🔧 Melhorias e refatorações sugeridas
- **Adicionar `argparse`**: permitir argumentos via linha de comando.  
- **Salvar saída em JSON/CSV**: útil para logs e relatórios.  
- **Verificar presença do binário `nmap`**: usar `shutil.which('nmap')`.  
- **Adicionar logging**: trocar `print` por `logging`.  
- **Suporte a múltiplos hosts**: aceitar uma lista de hosts e escanear em paralelo.

---

## ⚠️ Erros comuns e soluções

### `nmap.PortScannerError: Failed to run nmap: [Errno 2] No such file or directory`
- Causa: o binário `nmap` não está instalado ou não está no `PATH`.
- Solução: Instale o Nmap no sistema e verifique se `nmap` funciona no terminal.

### `SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes ... malformed \N character escape`
- Causa: strings contendo barras invertidas no Windows podem acionar escapes.
- Solução: use `os.path.join`, `os.path.normpath`, ou prefixe strings com `r'...'`.

### Erro ao criar venv: `FileNotFoundError: ... venv python not found`
- Causa: criação do venv falhou ou executável esperado não existe.
- Solução: verifique permissões e tente criar o venv manualmente (`python -m venv NMAP_test`).

---

## 🔒 Segurança e aviso legal
- **Aviso legal**: varredura de portas contra hosts que você não possui ou não tem autorização explícita é **ilegal** em muitos países. Use este script apenas em redes/hosts que você administra ou para os quais tem permissão.
- Ao rodar varreduras com privilégios elevados, você pode alterar comportamento do sistema — execute com cautela.
- Não compartilhe dados sensíveis, resultados de varreduras ou informações pessoais sem consentimento.

---

## 🤝 Contribuindo
Se desejar contribuir:
1. Abra uma _issue_ descrevendo o bug/feature.
2. Faça um fork e crie uma branch `feature/nome` ou `fix/issue-id`.
3. Submeta um _pull request_ com descrição clara e testes quando aplicável.

Sugestões de issues:
- Adicionar `argparse`.
- Salvar saída em JSON.
- Implementar verificação de `nmap` com `shutil.which`.

---

## 📄 Licença
Escolha uma licença para o projeto (por exemplo, MIT) e coloque um arquivo `LICENSE` no repositório. Sugestão curta para README:

```
MIT License

Copyright (c) 2025 SeuNome

[texto da licença...]
```

---

## 📎 Snippets úteis

### Verificar se nmap está no PATH
```python
import shutil
if shutil.which("nmap") is None:
    print("Aviso: o binário 'nmap' não está no PATH. Instale o nmap primeiro.")
```

### Sugestão: usar argparse para CLI
```python
import argparse

parser = argparse.ArgumentParser(description="Painel Nmap simples")
parser.add_argument("host", nargs='?', help="IP ou domínio para scan")
parser.add_argument("--all-ports", action="store_true", help="Scan em todas as portas (-p-)")
parser.add_argument("--venv", default="NMAP_test", help="Diretório do venv")
args = parser.parse_args()
```


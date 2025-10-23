import nmap
import time
import subprocess
import os
import sys #usado para sys.executable (caminho para o Python que está executando o script).
import platform

print("Verificando se seu sistema é compativel...")
if platform.system() not in ['Windows', 'Darwin', 'Linux', 'MacOs']:
    print("Sistema operacional não suportado.")
    sys.exit(1)
time.sleep(3)
subprocess.run("cls" if os.name == "nt" else "clear")

print("Esse Painel foi feito para ajudar a utilizar o Nmap, ele faz um scaner nas \n principais portas.")
print("Caso esteja no windows, recomendo abrir o CMD como Administrador.")
time.sleep(4)
subprocess.run("cls" if os.name == "nt" else "clear")

#Função que cria um Logo no estilo ASCII
def logo():
    print("▒█▀▀█ ░▀░ █▀▀█ █▀▀█ ░▀░ █▀▀█ █▀▀▄ █▀▀█ \n"
          "▒█░░░ ▀█▀ █░░█ █▄▄▀ ▀█▀ █▄▄█ █░░█ █░░█ \n"
          "▒█▄▄█ ▀▀▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ")

#Comando para limpar o terminal
def clear_screen():
    #Detecta o sistema via os.name
    os.system("cls" if os.name == "nt" else "clear") #nt -> WIndows -> executa cls se não executa clear. (Linux/MacOs)

#Função importante — tenta criar um virtualenv e instalar python-nmap dentro dele.
def ensure_venv_and_install(venv_dir="NMAP_test"):
    # Caminhos portáveis
    venv_dir = os.path.normpath(venv_dir) #torna o caminho portátil (remove barras duplicadas, etc).
    
    #Define o caminho do executável Python dentro do venv dependendo do OS:
    if os.name == "nt":
        venv_python = os.path.join(venv_dir, "Scripts", "python.exe")
    else: #padrão do venv no Windows (Scripts\python.exe) e Unix (bin/python).
        venv_python = os.path.join(venv_dir, "bin", "python")

    # Cria venv se não existir
    if not os.path.isdir(venv_dir):
        print("Criando virtualenv...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True) #Usa sys.executable para chamar o mesmo Python que está rodando o script e criar o venv (python -m venv NMAP_test).
        #check=True: se o comando falhar, lança subprocess.CalledProcessError
        time.sleep(1)

    # Usa o python do venv para instalar python-nmap
    print("Instalando dependências no venv (python-nmap)...")
    time.sleep(2)
    
    #Usa o python do venv para atualizar pip e instalar python-nmap.
    try:
        subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        subprocess.run([venv_python, "-m", "pip", "install", "python-nmap"], check=True)
    except FileNotFoundError:
        print("Erro: não foi encontrado o executável do venv em:", venv_python)
        print("Verifique se o venv foi criado corretamente ou rode o script com permissões adequadas.")
        return False
    except subprocess.CalledProcessError as e:
        print("Erro ao instalar pacotes:", e)
        return False
    """
check=True

Faz com que subprocess.run levante uma exceção (subprocess.CalledProcessError) se o comando retornar código de saída diferente de zero (ou seja, se falhar).

Sem check=True você teria que verificar CompletedProcess.returncode manualmente.
    """
    return True


def main():
    logo()
    # Se quiser, crie e instale no venv (opcional)
    success = ensure_venv_and_install("NMAP_test")
    if not success:
        print("Continuando sem venv (certifique-se de ter python-nmap instalado no sistema).")
        time.sleep(2)

    print("Olá, eu fiz esse script para auxiliar na varredura de portas.")
    time.sleep(4)
    clear_screen()
    logo()
    print("Basta digitar o IP ou o domínio (ex: 192.168.1.1 ou example.com).")
    time.sleep(5)
    clear_screen()
    logo()

    host = input("Digite o IP ou link: ").strip()
    if not host:
        print("Nenhum host informado. Saindo.")
        return


    nm = nmap.PortScanner()
    try:
        print("Escaneando... (isso pode levar alguns segundos)")
        scan_all_ports = input("Quer fazer uma varredura em todos as portas? (s/n)").lower() == 's'
        if scan_all_ports:
            nm.scan(host, arguments='-p-')
        else:
            nm.scan(host)
    except nmap.PortScannerError as e:
        print("Erro do nmap:", e)
        print("Observação: o pacote python-nmap é uma interface. Você precisa ter o binário 'nmap' instalado no sistema.")
        print("No Windows, instale o Nmap: https://nmap.org/download.html")
        return
    except Exception as e:
        print("Erro ao escanear:", e)
        return

    for h in nm.all_hosts():
        print(f"Host : {h} ({nm[h].hostname()})")
        print(f"State : {nm[h].state()}")
        for proto in nm[h].all_protocols():
            print(f"Protocol : {proto}")
            lport = nm[h][proto].keys()
            for port in sorted(lport):
                print(f"Port : {port}\tState : {nm[h][proto][port]['state']}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")


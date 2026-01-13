import os
import platform

def check_linux_security():
    print("[*] Verificando seguridad en Linux...")
    # Verifica si el firewall UFW está activo
    status = os.popen('ufw status').read()
    if "active" in status:
        print("[+] Firewall UFW: ACTIVO")
    else:
        print("[!] Firewall UFW: INACTIVO - Riesgo detectado")

def check_windows_security():
    print("[*] Verificando seguridad en Windows...")
    # Verifica si el servicio de Windows Defender está corriendo
    status = os.popen('sc query WinDefend').read()
    if "RUNNING" in status:
        print("[+] Windows Defender: EJECUTÁNDOSE")
  
if _name_ == "_main_":
    system = platform.system()
    if system == "Linux":
        check_linux_security()
    elif system == "Windows":
        check_windows_security()

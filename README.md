# 🛡️ Sistema de Aseguramiento (Hardening) de Sistemas

Este repositorio contiene una guía detallada y scripts básicos para fortalecer la seguridad de entornos Windows y Linux, reduciendo la superficie de ataque frente a amenazas comunes.

## 🐧 Hardening en Linux (Ubuntu/Debian)
Puntos clave implementados y documentados:
* *Gestión de Usuarios:* Deshabilitar el acceso root por SSH y configurar sudo.
* *Políticas de Contraseñas:* Configuración de libpam-pwquality para exigir contraseñas complejas.
* *Firewall (UFW):* Configuración de reglas básicas (bloqueo total de entrada, permitir solo puertos necesarios).
* *Actualizaciones:* Configuración de unattended-upgrades para parches de seguridad automáticos.

## 🪟 Hardening en Windows 10/11/Server
* *Políticas de Grupo (GPO):* Desactivar ejecución de macros y PowerShell para usuarios no administrativos.
* *Servicios innecesarios:* Desactivación de servicios como SMBv1 (vulnerable a Ransomware).
* *Windows Defender:* Configuración de protección en tiempo real y protección contra manipulaciones.

## 📜 Script de Auditoría Rápida (Python)
He incluido un script básico que verifica si ciertos servicios críticos están activos.

# -*- coding: utf-8 -*-
import requests

# Primera webhook que me pasaste
WEBHOOK = "https://discord.com/api/webhooks/1458969826671198376/RXcxTIPwKXKR-LRQOV3mbxcx47Vvxs3XfJSqZ894LAZfp-_IP_N542pxhSnyx7cn8lgO"

print("Enviando mensaje de prueba a la primera webhook...")
print(f"Webhook ID del canal: 1458959364458025164")

# Mensaje de prueba con instrucciones claras
try:
    response = requests.post(
        WEBHOOK,
        json={
            "content": "=== MENSAJE DE PRUEBA ===\n\nEste mensaje aparecio en el canal con ID: **1458959364458025164**\n\nPor favor dime:\n1. Cual es el NOMBRE de este canal?\n2. Es este el canal 1457771004813246748? (SI/NO)"
        },
        timeout=10
    )
    
    if response.status_code in [200, 204]:
        print("\nEXITO! Mensaje enviado correctamente")
        print("\nAhora revisa Discord y dime:")
        print("- En que canal aparecio?")
        print("- Ese canal tiene el ID 1457771004813246748?")
        print("\nSi NO es ese canal, necesito crear/obtener")
        print("la webhook del canal 1457771004813246748")
    else:
        print(f"\nERROR: {response.status_code}")
        print(f"Response: {response.text}")
        
except Exception as e:
    print(f"\nEXCEPCION: {e}")

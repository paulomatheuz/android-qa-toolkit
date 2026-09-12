import subprocess


try:
    resultado = subprocess.run(
        ["adb", "devices"],
        capture_output=True,
        text=True
    ) 
    if resultado.returncode == 0:
        linhas = resultado.stdout.strip().splitlines()
        if len(linhas) > 1:
            dados_dispositivo = linhas[1].split()
            numero_serie = dados_dispositivo[0]
            estado = dados_dispositivo[1]
            print(f"Numero de serie: {numero_serie}")
            if estado == "device":
                print("Aparelho conectado e autorizado!")
            else:
                print(f"Estado do aparelho: {estado}")
        else:
            print("Nenhum aparelho conectado!")
    else:
        print("ADB retornou um erro!")
except FileNotFoundError:
    print("ADB não encontrado!")
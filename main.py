import subprocess

def consultar_getprop(propriedade):
    resultado = subprocess.run(
        ["adb", "shell", "getprop", propriedade],
        capture_output=True,
        text=True
    )

    if resultado.returncode == 0:
        return resultado.stdout.strip()
    else:
        return None

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


                fabricante = consultar_getprop("ro.product.manufacturer")
                if fabricante is not None:
                    print(f"Fabricante: {fabricante}")
                else:
                    print("Não foi possível consultar o fabricante!")


                modelo = consultar_getprop("ro.product.model")
                if modelo is not None:
                    print(f"Modelo: {modelo}")
                else:
                    print("Não foi possível consultar o modelo!")


                versao_android = consultar_getprop("ro.build.version.release")
                if versao_android is not None:
                    print(f"Versão Android: {versao_android}")
                else:
                    print("Não foi possível consultar a versão do android!")


                resultado_bateria = subprocess.run(
                    ["adb", "shell", "dumpsys", "battery"],
                    capture_output=True,
                    text=True
                )

                if resultado_bateria.returncode == 0:
                    linhas_bateria = resultado_bateria.stdout.splitlines()
                    nivel_bateria = None
                    for linha in linhas_bateria:
                        if linha.strip().startswith("level:"):
                            partes = linha.split(":")
                            nivel_bateria = int(partes[1].strip())
                            print(f"Bateria: {nivel_bateria}%")
                            if nivel_bateria < 20:
                                print("Bateria baixa!")
                    if nivel_bateria is None:
                        print("Nível da bateria não encontrado na saída!")
                else:
                    print("Não foi possível consultar o nível da bateria!")
            elif estado == "unauthorized":
                print(f"{estado}: desbloqueie o celular e aceite a autorização USB")
            elif estado == "offline":
                print(f"{estado}: verifique o cabo/conexão e reinicie o ADB")
            else:
                print(f"Estado do aparelho: {estado}")
        else:
            print("Nenhum aparelho conectado!")
    else:
        print("ADB retornou um erro!")
except FileNotFoundError:
    print("ADB não encontrado!")
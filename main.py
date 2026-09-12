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
            print(linhas[1])
        else:
            print("Nenhum aparelho conectado!")
    else:
        print("ADB retornou um erro!")
except FileNotFoundError:
    print("ADB não encontrado!")

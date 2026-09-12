import subprocess


try:
    result = subprocess.run(["adb", "--version"])
    if result.returncode == 0:
        print("ADB disponivel!")
    else:
        print("ADB retornou um erro!")
except FileNotFoundError:
    print("ADB não encontrado!")
    
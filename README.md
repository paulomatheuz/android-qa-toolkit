# Android QA Toolkit

Aplicação de terminal desenvolvida em Python para auxiliar testes e diagnósticos básicos de aparelhos Android por meio do Android Debug Bridge (ADB).

O projeto está sendo construído de forma incremental, com foco no aprendizado prático de Python, automação, comunicação com dispositivos Android, tratamento de erros, Git e GitHub.

## Status

🚧 Em desenvolvimento

A aplicação identifica um aparelho conectado, informa seu número de série e o estado da conexão com o ADB. Quando o aparelho está conectado e autorizado, consulta e exibe o fabricante, o modelo, a versão do Android e o nível da bateria.

O programa é executado no computador. Python continua sendo a linguagem principal, e o ADB é a ferramenta externa utilizada para a comunicação com o aparelho.

## Contexto

Este projeto nasceu da minha experiência profissional com atendimento ao público e diagnóstico de software e hardware em dispositivos móveis. O contato diário com rotinas de diagnóstico automatizado despertou a ideia de construir uma ferramenta própria para aprofundar meus conhecimentos em programação e explorar novas formas de auxiliar testes em aparelhos Android.

O Android QA Toolkit é um projeto pessoal e educacional. Ele não utiliza nem reproduz sistemas internos, processos proprietários, informações confidenciais ou dados de clientes e não representa meu empregador ou qualquer fabricante de dispositivos.

## Funcionalidades atuais

- verifica se o executável ADB está disponível;
- consulta a lista de aparelhos reconhecidos pelo ADB;
- informa quando nenhum aparelho está conectado;
- exibe o número de série e o estado do primeiro aparelho encontrado;
- identifica aparelhos conectados e autorizados (`device`);
- orienta o usuário nos estados `unauthorized` e `offline`;
- consulta fabricante, modelo e versão do Android;
- consulta o nível atual da bateria;
- alerta quando a bateria está abaixo de 20%;
- informa quando o nível da bateria não é encontrado;
- trata falhas individuais nas consultas;
- utiliza a função `consultar_getprop()` para evitar repetição de código.

As consultas são executadas somente quando o aparelho está conectado e autorizado.

## Requisitos

- Python 3;
- [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools), com o comando `adb` disponível no `PATH`;
- aparelho Android com depuração USB ativada;
- autorização da conexão USB no aparelho;
- cabo USB com suporte à transferência de dados;
- Git, caso o repositório seja obtido com `git clone`.

O desenvolvimento e os testes atuais são realizados no Windows com Python 3.14.7. A aplicação utiliza somente a biblioteca padrão do Python.

## Como executar

Clone o repositório e entre na pasta:

```powershell
git clone https://github.com/paulomatheuz/android-qa-toolkit.git
cd android-qa-toolkit
```

Confirme que o ADB está disponível:

```powershell
adb --version
```

Confira a conexão do aparelho:

```powershell
adb devices
```

Execute o programa:

```powershell
python main.py
```

## Exemplo

```text
Numero de serie: ABC123456789
Aparelho conectado e autorizado!
Fabricante: samsung
Modelo: SM-S942B
Versão Android: 16
Bateria: 100%
```

Quando nenhum aparelho está conectado:

```text
Nenhum aparelho conectado!
```

Quando a conexão ainda não foi autorizada:

```text
unauthorized: desbloqueie o celular e aceite a autorização USB
```

## Tecnologias e conceitos praticados

- Python;
- Android Debug Bridge (ADB);
- módulo `subprocess`;
- funções e valores de retorno;
- condicionais e indentação;
- listas, strings e conversão para inteiros;
- captura de saída com `stdout`;
- códigos de retorno com `returncode`;
- tratamento de exceções;
- laços `for`;
- depuração de caminhos de sucesso e falha;
- versionamento incremental com Git e GitHub.

## Limitações atuais

- considera somente o primeiro aparelho listado pelo ADB;
- não permite selecionar um dispositivo pelo número de série;
- recomenda-se conectar apenas um aparelho ou emulador;
- depende do ADB configurado no `PATH`;
- consulta apenas informações básicas;
- ainda não executa testes automatizados de software ou hardware;
- possui somente interface de terminal;
- a execução em Linux e macOS ainda não foi validada.

## Próximos passos

- consultar o nível da API do Android;
- melhorar o tratamento de múltiplos aparelhos;
- adicionar novas informações úteis para QA;
- criar testes automatizados;
- manter a documentação atualizada conforme o projeto evoluir.

Cada evolução deve ser pequena, compreensível, testada e registrada em um commit significativo.

## Segurança

Use o ADB somente em aparelhos próprios ou para os quais você tenha autorização. A depuração USB concede acesso significativo ao dispositivo e deve ser desativada quando não estiver em uso.

Desenvolvido por [Paulo Matheus](https://github.com/paulomatheuz).

Você também pode me encontrar no [LinkedIn](https://www.linkedin.com/in/paulo-matheus-b6b1a63a3/).

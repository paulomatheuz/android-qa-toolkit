# Android QA Toolkit

Aplicação de terminal desenvolvida em Python para auxiliar testes e diagnósticos básicos de aparelhos Android por meio do Android Debug Bridge (ADB).

O projeto está sendo construído de forma incremental, com foco no aprendizado prático de Python, automação, comunicação com dispositivos Android, tratamento de erros, Git e GitHub.

## Status

🚧 Em desenvolvimento

A primeira versão de consulta básica identifica um aparelho conectado, informa seu número de série e o estado da conexão com o ADB. Quando o aparelho está conectado e autorizado, consulta e exibe o fabricante, o modelo e a versão do Android.

O programa é executado no computador. Python continua sendo a linguagem principal, e o ADB é a ferramenta externa utilizada para a comunicação com o aparelho.

## Contexto

Este projeto nasceu da minha experiência profissional com atendimento ao público e diagnóstico de software e hardware em dispositivos móveis. O contato diário com rotinas de diagnóstico automatizado despertou a ideia de construir uma ferramenta própria para aprofundar meus conhecimentos em programação e explorar novas formas de auxiliar testes em aparelhos Android.

O Android QA Toolkit é um projeto pessoal e educacional. Ele não utiliza nem reproduz sistemas internos, processos proprietários, informações confidenciais ou dados de clientes e não representa meu empregador ou qualquer fabricante de dispositivos.

## Funcionalidades atuais

- consulta a lista de aparelhos reconhecidos pelo ADB;
- informa quando o executável ADB não é encontrado ou quando a listagem retorna um erro;
- informa quando nenhum aparelho está conectado;
- exibe o número de série e o estado do primeiro aparelho encontrado;
- identifica o estado `device` e informa que o aparelho está conectado e autorizado;
- informa outros estados retornados pelo ADB, como `unauthorized` ou `offline`;
- consulta fabricante, modelo e versão do Android quando o estado é `device`;
- verifica o código de retorno de cada consulta e mostra uma mensagem específica em caso de falha.

As consultas ao fabricante, ao modelo e à versão do Android têm verificações independentes. Se uma delas retornar um código de erro, o programa ainda tenta executar as consultas seguintes.

## Requisitos

- Python 3;
- [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools) com o comando `adb` disponível no `PATH`;
- aparelho Android com a depuração USB ativada e a conexão autorizada no aparelho;
- cabo USB com suporte à transferência de dados;
- Git, caso o repositório seja obtido pelo comando `git clone`.

O desenvolvimento e os testes atuais estão sendo realizados no Windows, com Python 3.14.7. A aplicação utiliza somente a biblioteca padrão do Python; não há dependências Python externas para instalar.

## Como executar

Clone o repositório e entre na pasta do projeto:

```powershell
git clone https://github.com/paulomatheuz/android-qa-toolkit.git
cd android-qa-toolkit
```

Confirme que o ADB está disponível:

```powershell
adb --version
```

Conecte somente um aparelho, autorize a depuração USB nesse computador e confira a conexão:

```powershell
adb devices
```

Quando o estado do aparelho for `device`, execute:

```powershell
python main.py
```

Exemplo com um aparelho autorizado (número de série fictício; os demais valores variam conforme o aparelho):

```text
Numero de serie: ABC123456789
Aparelho conectado e autorizado!
Fabricante: samsung
Modelo: SM-S942B
Versão Android: 16
```

Exemplo sem aparelho conectado:

```text
Nenhum aparelho conectado!
```

Se o estado for diferente de `device`, o programa informa esse estado e não realiza as consultas às propriedades do aparelho.

## Tecnologias

- Python;
- Android Debug Bridge (ADB);
- módulo `subprocess` da biblioteca padrão;
- Git e GitHub.

## Conceitos praticados

Durante o desenvolvimento deste projeto, estou praticando:

- variáveis, strings e listas;
- condicionais e indentação;
- módulos e imports;
- execução de comandos externos;
- captura e tratamento da saída de processos;
- separação entre a saída textual (`stdout`) e o código de retorno (`returncode`);
- tratamento de exceções;
- depuração e verificação dos caminhos de sucesso e falha;
- versionamento incremental com Git.

## Limitações atuais

- considera somente o primeiro aparelho listado pelo ADB e não oferece seleção de dispositivo;
- deve ser utilizado com apenas um aparelho ou emulador conectado: as consultas ainda não selecionam o destino pelo número de série;
- depende do ADB instalado e configurado no `PATH`;
- consulta apenas informações básicas; ainda não consulta bateria, memória ou armazenamento;
- ainda não executa testes de software ou hardware;
- possui somente uma interface de terminal;
- a execução em Linux e macOS ainda não foi validada no projeto.

## Próximos passos

- praticar funções para organizar as consultas repetidas, conforme a evolução do aprendizado;
- melhorar as mensagens de falha e o tratamento dos diferentes estados de conexão;
- manter a documentação atualizada conforme novas funcionalidades forem concluídas.

Cada evolução deve ser pequena, compreensível, testada e registrada em um commit significativo.

## Segurança

Use o ADB somente em aparelhos próprios ou para os quais você tenha autorização. A depuração USB concede acesso significativo ao dispositivo e deve ser desativada quando não estiver em uso.

## Autor

Desenvolvido por [Paulo Matheus](https://github.com/paulomatheuz).

Você também pode me encontrar no [LinkedIn](https://www.linkedin.com/in/paulo-matheus-b6b1a63a3/).

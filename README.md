# Android QA Toolkit

Aplicação de terminal desenvolvida em Python para auxiliar testes e diagnósticos básicos de aparelhos Android por meio do Android Debug Bridge (ADB).

O projeto está sendo construído de forma incremental, com foco no aprendizado prático de Python, automação, comunicação com dispositivos Android, tratamento de erros, Git e GitHub.

## Status

🚧 Em desenvolvimento

Atualmente, a aplicação identifica a presença de um aparelho conectado e informa o número de série e o estado da conexão com o ADB.

## Contexto

Este projeto nasceu da minha experiência profissional com atendimento ao público e diagnóstico de software e hardware em dispositivos móveis. O contato diário com rotinas de diagnóstico automatizado despertou a ideia de construir uma ferramenta própria para aprofundar meus conhecimentos em programação e explorar novas formas de auxiliar testes em aparelhos Android.

O Android QA Toolkit é um projeto pessoal e educacional. Ele não utiliza nem reproduz sistemas internos, processos proprietários, informações confidenciais ou dados de clientes e não representa meu empregador ou qualquer fabricante de dispositivos.

## Funcionalidades atuais

- verifica se o ADB está disponível no computador;
- lista aparelhos reconhecidos pelo ADB;
- informa quando nenhum aparelho está conectado;
- exibe o número de série do primeiro aparelho encontrado;
- identifica se o aparelho está conectado e autorizado;
- informa outros estados retornados pelo ADB, como `unauthorized` ou `offline`.

## Requisitos

- Python 3;
- Android SDK Platform-Tools com o comando `adb` disponível no `PATH`;
- aparelho Android com a depuração USB ativada;
- cabo USB com suporte à transferência de dados.

O desenvolvimento e os testes atuais estão sendo realizados no Windows.

## Como executar

Clone o repositório:

```bash
git clone https://github.com/paulomatheuz/android-qa-toolkit.git
cd android-qa-toolkit
```

Confirme que o ADB está disponível:

```bash
adb --version
```

Conecte e autorize o aparelho e execute:

```bash
python main.py
```

Exemplo com um aparelho autorizado:

```text
Numero de serie: ABC123456789
Aparelho conectado e autorizado!
```

Exemplo sem aparelho conectado:

```text
Nenhum aparelho conectado!
```

## Tecnologias

- Python;
- Android Debug Bridge (ADB);
- módulo `subprocess` da biblioteca padrão;
- Git e GitHub.

## Conceitos praticados

Durante o desenvolvimento deste projeto, estou praticando:

- variáveis, strings e listas;
- condicionais;
- módulos e imports;
- execução de comandos externos;
- captura e tratamento da saída de processos;
- códigos de retorno;
- tratamento de exceções;
- depuração;
- versionamento incremental com Git.

## Limitações atuais

- considera somente o primeiro aparelho listado pelo ADB;
- depende do ADB instalado e configurado no `PATH`;
- ainda não coleta informações detalhadas do aparelho;
- ainda não executa testes de software ou hardware;
- possui somente uma interface de terminal.

## Próximos passos

- consultar fabricante, modelo e versão do Android;
- melhorar o tratamento dos diferentes estados de conexão;
- manter a documentação atualizada conforme novas funcionalidades forem concluídas.

## Segurança

Use o ADB somente em aparelhos próprios ou para os quais você tenha autorização. A depuração USB concede acesso significativo ao dispositivo e deve ser desativada quando não estiver em uso.

## Autor

Desenvolvido por [Paulo Matheus](https://github.com/paulomatheuz).

Você também pode me encontrar no [LinkedIn](https://www.linkedin.com/in/paulo-matheus-b6b1a63a3/).


# Sistema de Gerenciamento de PDFs e Consultas com LangChain

Este repositório contém uma série de scripts que ajudam no gerenciamento e processamento de arquivos PDF, utilizando a biblioteca LangChain para consultas e integração com bancos de dados vetoriais. O sistema também monitoriza diretórios e automatiza o processamento de arquivos.

## Estrutura do Projeto

- **`start.sh`**: Script de inicialização. Verifica se os diretórios necessários estão presentes e inicia o processo de monitoramento e regeneração de PDFs.
- **`regen_pdf.py`**: Script responsável por regenerar arquivos PDF usando o Ghostscript.
- **`install.sh`**: Script de instalação para configurar o ambiente, incluindo a criação de diretórios necessários, instalação de dependências e verificação de pacotes como Ghostscript e Python.
- **`query_data.py`**: Script para realizar consultas ao banco de dados vetorial usando LangChain, retornando respostas com base em documentos carregados.
- **`populate_database.py`**: Script que carrega documentos PDF, os divide em partes menores e adiciona esses fragmentos ao banco de dados vetorial para futuras consultas.
- **`requirements.txt`**: Arquivo de dependências do Python.

## Como Usar

### 1. Instalação

Para começar, execute o script `install.sh` para configurar o ambiente:

```bash
bash install.sh
```

Isso irá:

- Criar os diretórios `target` e `data`, se não existirem.
- Verificar e instalar o Python, o `pip` e o Ghostscript (caso não estejam instalados).
- Instalar as dependências do projeto listadas no `requirements.txt`.

### 1.5 Variavies de ambiente (Opcional)

Preencha os dados do servidor `OLLAMA` no arquivo `.env.example` para obter a conexão com o mesmo

```.env
OLLAMA_MODEL="llama3.1:latest"
OLLAMA_SERVER_IP="http://0.0.0.0:11434"
```

Em seguida renomeie para `.env`.

Caso não faça essa etapa os valores padrôes serão
```
OLLAMA_MODEL="mistral"
OLLAMA_SERVER_IP="http://localhost:11434"
```

### 2. Regeneração de PDFs

O script `regen_pdf.py` é responsável por monitorar a pasta `./target` e, ao detectar a criação de novos arquivos PDF, utiliza o Ghostscript para regenerar esses arquivos em uma versão "reparada", salvando-os na pasta `./data`.

Para iniciar o monitoramento, basta executar o script `start.sh`:

```bash
bash start.sh
```

Este script verificará se as pastas necessárias estão presentes e, se tudo estiver correto, iniciará o processo de monitoramento.

### 3. Carregar Documentos para o Banco de Dados

Para carregar documentos PDF para o banco de dados vetorial e permitir consultas, execute o script `populate_database.py`. O script irá carregar todos os PDFs da pasta `data`, dividir os documentos em partes menores e adicionar essas partes ao banco de dados.

Caso queira reiniciar o banco de dados, utilizando o argumento `--reset`, execute o comando:

```bash
python3 populate_database.py --reset
```

Isso apagará o banco de dados existente e o recriará com os novos documentos.

### 4. Consultas ao Banco de Dados

Para realizar consultas no banco de dados vetorial, utilize o script `query_data.py`. Ele recebe uma consulta em texto e busca por documentos relacionados no banco de dados.

Exemplo de uso:

```bash
python3 query_data.py "Qual é a capital do Brasil?"
```

O script irá procurar nos documentos carregados no banco de dados e retornará a resposta baseada nos documentos mais relevantes encontrados.

## Como Funciona

### Monitoramento de Arquivos PDF

O script `regen_pdf.py` utiliza o módulo `watchdog` para monitorar mudanças no diretório `./target`. Quando um novo arquivo PDF é criado, o script executa o comando `gs` (Ghostscript) para regenerar o arquivo PDF e salvá-lo na pasta `./data`. A regeneração é feita com a opção `-dPDFSETTINGS=/prepress` para otimizar a qualidade.

### Carregamento de Documentos e Indexação no Banco de Dados

O script `populate_database.py` usa o `PyPDFDirectoryLoader` da biblioteca LangChain para carregar documentos PDF da pasta `data`. Em seguida, os documentos são divididos em partes menores utilizando o `RecursiveCharacterTextSplitter`. Essas partes são adicionadas ao banco de dados vetorial Chroma.

### Consultas ao Banco de Dados

O script `query_data.py` utiliza o LangChain com o modelo `OllamaLLM` para realizar consultas no banco de dados vetorial. Ele usa a função `similarity_search_with_score` para buscar os documentos mais relevantes, gera um prompt com o contexto e a consulta, e obtém uma resposta do modelo.

## Dependências

O sistema depende das seguintes bibliotecas:

- `pypdf`: Para manipulação de arquivos PDF.
- `langchain`: Framework para construção de cadeias de processamento de linguagem natural.
- `chromadb`: Banco de dados vetorial utilizado para armazenar e recuperar documentos.
- `pytest`: Para testes automatizados.
- `boto3`: SDK da AWS para interação com serviços da Amazon.
- `watchdog`: Para monitoramento de arquivos e diretórios.
- `langchain_community`, `langchain_ollama`, `langchain_chroma`: Bibliotecas complementares para integração com modelos de linguagem e bancos de dados vetoriais.

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Agendamento Automático

O script `start.sh` também adiciona uma tarefa ao cron para garantir que o processo de regeneração de PDFs seja executado automaticamente todos os dias à meia-noite.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

**Nota**: Certifique-se de que você tenha as permissões necessárias para criar e modificar arquivos e pastas no sistema.

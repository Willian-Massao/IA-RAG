
# Projeto de Treinamento de IA

Este repositório contém os scripts necessários para treinar e interagir com uma IA. Abaixo estão as instruções detalhadas para configurar e usar os scripts fornecidos.

## Requisitos

Antes de executar os scripts, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas Python necessárias (consulte o arquivo `requirements.txt` ou os comentários nos scripts para saber as dependências exatas)
- PDF que será utilizado para treinamento da IA (coloque-o no diretório `target`)

## Passo 1: Configuração Inicial

1. **Executar o script `install.sh`**:
   O primeiro passo para configurar o ambiente é rodar o script `install.sh`. Este script irá instalar todas as dependências necessárias.

   Execute o seguinte comando para instalar as dependências:

   ```bash
   ./install.sh
   ```

2. **Executar o script `start.sh`**:
   Após a instalação, execute o script `start.sh` para iniciar o ambiente ou os serviços necessários para o funcionamento do sistema.

   Execute o seguinte comando para iniciar o ambiente:

   ```bash
   ./start.sh
   ```

## Passo 2: Preparar os Dados

Para treinar a IA, você precisa fornecer um PDF que será processado e filtrado para extrair as informações necessárias.

1. **Colocar o PDF no diretório `target`**:
   Coloque o arquivo PDF que será utilizado para o treinamento no diretório `target`. O script irá ler o arquivo, filtrá-lo e preparar os dados.

2. **Filtragem do PDF**:
   Após colocar o PDF no diretório `target`, execute o script para limpar os dados extraídos do PDF:

   ```bash
   ./limpar_pdf.sh
   ```

   Este script irá limpar e filtrar os dados do PDF para que possam ser utilizados no treinamento da IA.

## Passo 3: Treinamento da IA

Após filtrar os dados, você pode treinar a IA.

1. **Executar o script `populate_database.py`**:
   Este script irá preencher o banco de dados com as informações extraídas do PDF, que serão usadas para o treinamento da IA.

   Execute o script Python da seguinte forma:

   ```bash
   python populate_database.py
   ```

   Isso vai treinar a IA com as informações do PDF filtrado.

## Passo 4: Interagir com a IA

Após o treinamento, você pode interagir com a IA para fazer perguntas baseadas no conteúdo que foi treinado.

1. **Executar o script `query_data.py`**:
   O script `query_data.py` permite que você faça perguntas à IA usando o parâmetro `"text"`, que será comparado com o que foi ensinado durante o treinamento.

   Exemplo de comando para interagir com a IA:

   ```bash
   python query_data.py "Qual é o conteúdo sobre X?"
   ```

   A IA irá buscar a resposta no banco de dados treinado e retornar a resposta correspondente.

## Conclusão

Agora você está pronto para treinar e interagir com a IA! Se houver algum erro ou dúvida, consulte os logs gerados pelos scripts ou abra uma issue no GitHub para mais informações.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

# n8n-nodes-difyai

[![npm version](https://img.shields.io/npm/v/n8n-nodes-difyai.svg)](https://www.npmjs.com/package/n8n-nodes-difyai)
[![License: MIT](https://img.shields.io/npm/l/n8n-nodes-difyai.svg)](LICENSE)

Este pacote é um nó da comunidade para o [n8n](https://n8n.io) que integra a **Dify API**.  
Ele permite enviar mensagens de chat, converter áudio em texto e fazer upload de arquivos diretamente pela API do Dify.

## Funcionalidades

- **Enviar Mensagem de Chat:**  
  Envie mensagens de chat para a API do Dify com suporte aos modos de resposta *streaming* ou *blocking*.  
  Suporta o envio de arquivos via configuração dinâmica (com opções para URLs remotas ou uploads locais).

- **Áudio para Texto:**  
  Converta arquivos de áudio em texto enviando dados binários.

- **Upload de Arquivo:**  
  Faça upload de arquivos utilizando `multipart/form-data`.

## Instalação no n8n

Para instalar este nó da comunidade no n8n:

1. **Acesse as Configurações do n8n:**
   - No editor do n8n, vá para `Settings` > `Community Nodes`.

2. **Instale o Nó da Comunidade:**
   - Clique em `Install`.
   - No campo `Enter npm package name`, insira `n8n-nodes-difyai`.
   - Marque a opção `I understand the risks of installing unverified code from a public source`.
   - Clique em `Install` para concluir a instalação.

Para mais detalhes sobre a instalação de nós da comunidade, consulte a [documentação oficial do n8n](https://docs.n8n.io/integrations/community-nodes/installation/).

## Configuração de Credenciais

Antes de usar o nó, configure as credenciais do **DifyApi** no n8n:

- **Base URL:**  
  Informe a URL base da API do Dify, por exemplo:  
  `https://dify.com/v1`  
  (O nó força HTTPS e garante que a URL termine com `/v1`)

- **API Key:**  
  Sua chave de API fornecida pelo Dify.

## Operações do Nó

### 1. Enviar Mensagem de Chat

Envie uma requisição de mensagem de chat para a API do Dify.

**Parâmetros:**

- **User ID:** Identificador único do usuário.
- **Query:** Conteúdo da mensagem de chat.
- **Conversation ID:** (Opcional) ID da conversa para continuidade.
- **Response Mode:** Selecione entre *Streaming* e *Blocking*.
- **Files:** (Opcional) Adicione um ou mais arquivos.  
  Para cada arquivo, configure:
  - **Type:** Tipo do arquivo (Áudio, Personalizado, Documento, Imagem, Vídeo).
  - **Transfer Method:** Selecione entre *Remote URL* e *Local File*.
  - **URL:** (Exibido quando *Remote URL* é selecionado) Forneça a URL do arquivo.
  - **Upload File ID:** (Exibido quando *Local File* é selecionado) Forneça o ID do arquivo enviado via API de Upload de Arquivo.

### 2. Áudio para Texto

Converta um arquivo de áudio em texto.

- Utilize o campo **Binary Property** para informar o nome da propriedade binária que contém o arquivo de áudio.
- O nó envia o arquivo para a API e retorna o texto convertido.

### 3. Upload de Arquivo

Faça upload de um arquivo para a API do Dify.

- Utilize o campo **Binary Property** para informar o nome da propriedade binária que contém o arquivo.
- O nó realiza o upload e retorna os detalhes do arquivo (ID, nome, tamanho, etc.).

## Uso no n8n

1. **Adicione o nó DifyAI** ao seu workflow no editor do n8n.
2. **Selecione a operação desejada** (Enviar Mensagem de Chat, Áudio para Texto ou Upload de Arquivo).
3. **Configure os parâmetros do nó** e atribua as credenciais **DifyApi**.
4. **Conecte o nó** ao seu fluxo de trabalho e execute-o para interagir com a API do Dify.

## Licença

Este pacote é licenciado sob a [Licença MIT](LICENSE).

---

Para mais informações sobre a instalação e uso de nós da comunidade no n8n, consulte a [documentação oficial](https://docs.n8n.io/integrations/community-nodes/installation/).

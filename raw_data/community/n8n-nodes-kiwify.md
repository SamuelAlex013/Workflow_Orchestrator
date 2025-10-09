# n8n-nodes-kiwify

![logo](logo.png)

Este é um node da comunidade n8n que permite integrar com a API da Kiwify. Ele possibilita acessar vários serviços e dados da Kiwify dentro dos seus workflows do n8n.

[Kiwify](https://kiwify.com.br/) é uma plataforma de vendas de produtos digitais que permite criadores venderem cursos, ebooks e outros conteúdos digitais.

## Instalação

Siga o [guia de instalação](https://docs.n8n.io/integrations/community-nodes/installation/) na documentação de nodes da comunidade do n8n.

## Operações

### Conta
- **Obter Detalhes da Conta**: Recupera detalhes sobre sua conta Kiwify

### Produtos
- **Listar Produtos**: Obtenha uma lista de todos os produtos
  - **Page Size** (opcional): Número de produtos a retornar por página (padrão: 10)
  - **Page Number** (opcional): Número da página a recuperar (padrão: 1)
- **Consultar Produto**: Obtenha os detalhes de um produto específico
  - **ID Do Produto** (obrigatório): ID do produto a ser consultado

### Vendas
- **Listar Vendas**: Obtenha uma lista de todas as vendas
  - **Data De Início** (obrigatório): Data de início para buscar vendas (formato: YYYY-MM-DD)
  - **Data De Fim** (obrigatório): Data de fim para buscar vendas (formato: YYYY-MM-DD)
  - **Status** (opcional): Filtrar vendas por status
  - **Método De Pagamento** (opcional): Filtrar vendas por método de pagamento
  - **ID Do Produto** (opcional): Filtrar vendas por ID do produto
  - **Detalhes Completos Da Venda** (opcional): Se deve retornar detalhes completos da venda
- **Consultar Venda**: Obtenha os detalhes de uma venda específica
  - **ID Da Venda** (obrigatório): ID da venda a ser consultada
- **Reembolsar Venda**: Reembolse uma venda específica
  - **ID Da Venda** (obrigatório): ID da venda a ser reembolsada
  - **Chave PIX** (opcional): Chave PIX para reembolso
- **Consultar Estatísticas De Vendas**: Obtenha estatísticas de vendas
  - **Data De Início** (obrigatório): Data de início para estatísticas (formato: YYYY-MM-DD)
  - **Data De Fim** (obrigatório): Data de fim para estatísticas (formato: YYYY-MM-DD)
  - **ID Do Produto** (opcional): ID do produto para estatísticas específicas

### Afiliados
- **Listar Afiliados**: Obtenha uma lista de todos os afiliados
  - **Tamanho Da Página** (opcional): Número de afiliados a retornar por página (padrão: 10)
  - **Número Da Página** (opcional): Número da página a recuperar (padrão: 1)
  - **Status** (opcional): Filtrar afiliados por status (ativo, bloqueado, recusado)
  - **ID Do Produto** (opcional): Filtrar afiliados por ID do produto
  - **Buscar** (opcional): Termo de busca para filtrar afiliados
- **Consultar Afiliado**: Obtenha detalhes de um afiliado específico
  - **ID Do Afiliado** (obrigatório): ID do afiliado a ser consultado
- **Editar Afiliado**: Edite informações de um afiliado específico
  - **ID Do Afiliado** (obrigatório): ID do afiliado a ser editado
  - **Comissão** (opcional): Nova comissão do afiliado
  - **Status** (opcional): Novo status do afiliado (ativo, bloqueado, recusado)

### Webhooks
- **Listar Webhooks**: Obtenha uma lista de todos os webhooks
  - **Tamanho Da Página** (opcional): Número de webhooks a retornar por página (padrão: 10)
  - **Número Da Página** (opcional): Número da página a recuperar (padrão: 1)
  - **ID Do Produto** (opcional): Filtrar webhooks por ID do produto
  - **Buscar** (opcional): Termo de busca para filtrar webhooks
- **Consultar Webhook**: Obtenha detalhes de um webhook específico
  - **ID Do Webhook** (obrigatório): ID do webhook a ser consultado
- **Criar Webhook**: Crie um novo webhook
  - **Nome Do Webhook** (obrigatório): Nome do webhook
  - **URL Do Webhook** (obrigatório): URL de destino do webhook
  - **Produtos** (opcional): ID do produto específico ou "all" para todos os produtos (padrão: "all")
  - **Triggers** (obrigatório): Eventos que irão disparar o webhook
  - **Token** (opcional): Token personalizado para o webhook
- **Atualizar Webhook**: Atualize um webhook específico
  - **ID Do Webhook** (obrigatório): ID do webhook a ser atualizado
  - **Nome Do Webhook** (obrigatório): Nome do webhook
  - **URL Do Webhook** (obrigatório): URL de destino do webhook
  - **Produtos** (opcional): ID do produto específico ou "all" para todos os produtos (padrão: "all")
  - **Triggers** (obrigatório): Eventos que irão disparar o webhook
  - **Token** (opcional): Token personalizado para o webhook
- **Deletar Webhook**: Delete um webhook específico
  - **ID Do Webhook** (obrigatório): ID do webhook a ser deletado

### Eventos
- **Listar Participantes**: Obtenha uma lista de participantes de eventos
  - **ID Do Produto** (obrigatório): ID do produto para listar participantes
  - **Check-in Realizado** (opcional): Filtrar por participantes que fizeram check-in
  - **Tamanho Da Página** (opcional): Número de participantes a retornar por página (padrão: 10)
  - **Número Da Página** (opcional): Número da página a recuperar (padrão: 1)
  - **Data De Criação - Início** (opcional): Data de início para filtrar por data de criação (formato: YYYY-MM-DD)
  - **Data De Criação - Fim** (opcional): Data de fim para filtrar por data de criação (formato: YYYY-MM-DD)
  - **Data De Atualização - Início** (opcional): Data de início para filtrar por data de atualização (formato: YYYY-MM-DD)
  - **Data De Atualização - Fim** (opcional): Data de fim para filtrar por data de atualização (formato: YYYY-MM-DD)
  - **External ID** (opcional): Filtrar por External ID do participante
  - **Batch ID** (opcional): Filtrar por Batch ID do lote
  - **Telefone** (opcional): Filtrar por telefone do participante
  - **CPF** (opcional): Filtrar por CPF do participante
  - **ID Do Pedido** (opcional): Filtrar por ID do pedido

### Financeiro
- **Consultar Saldos**: Obtenha todos os saldos da conta
- **Consultar Saldo Específico**: Obtenha um saldo específico por Legal Entity ID
  - **Legal Entity ID** (obrigatório): ID da entidade legal para consultar saldo específico
- **Listar Saques**: Obtenha uma lista de todos os saques
  - **Legal Entity ID** (opcional): Filtrar saques por Legal Entity ID
  - **Tamanho Da Página** (opcional): Número de saques a retornar por página (padrão: 10)
  - **Número Da Página** (opcional): Número da página a recuperar (padrão: 1)
- **Consultar Saque**: Obtenha detalhes de um saque específico
  - **ID Do Saque** (obrigatório): ID do saque a ser consultado
- **Realizar Saque**: Solicite a realização de um saque
  - **Valor Do Saque** (obrigatório): Valor do saque a ser solicitado (em centavos)
  - **Legal Entity ID** (obrigatório): ID da entidade legal para consultar saldo específico

## Credenciais

Para usar este node, você precisa configurar as credenciais da API da Kiwify:

1. **Client ID**: Seu Client ID da API Kiwify
2. **Client Secret**: Seu Client Secret da API Kiwify
3. **Account ID**: Seu Account ID da Kiwify

### Como obter suas credenciais:

1. Faça login no seu painel da Kiwify
2. Navegue para Apps > API > Criar Chave API
3. Copie o `client_id`
4. Copie o `client_secret`
5. Copie o `account_id` da mesma página

O node automaticamente gerenciará o fluxo OAuth 2.0:
1. Usando seu Client ID e Client Secret para obter um access token
2. Usando o access token e Account ID para requisições subsequentes da API

### Fluxo de Autenticação:

O node implementa o fluxo OAuth 2.0 completo conforme especificado na documentação da API da Kiwify:

1. **Requisição de Token**: `POST /oauth/token` com client_id e client_secret
2. **Requisições da API**: Usa o access_token retornado no cabeçalho Authorization junto com x-kiwify-account-id

Para mais informações sobre autenticação, visite a [documentação da API da Kiwify](https://docs.kiwify.com.br/api-reference/general).

## Recursos

* [Documentação de nodes da comunidade n8n](https://docs.n8n.io/integrations/community-nodes/)
* [Documentação da API da Kiwify](https://docs.kiwify.com.br/api-reference/general)

## Licença

[MIT](https://github.com/99labdev/n8n-nodes-kiwify/blob/master/LICENSE.md)

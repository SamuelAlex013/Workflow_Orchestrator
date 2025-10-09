# n8n-nodes-tiny-erp

Este é um node personalizado para o n8n que permite integração com o Tiny ERP.

## Instalação

Para instalar este node personalizado no seu n8n, siga os passos abaixo:

1. Vá até a pasta raiz da sua instalação do n8n
2. Execute o comando:
```bash
npm install n8n-nodes-tiny-erp
```

## Configuração

1. No n8n, vá até as configurações de credenciais
2. Adicione uma nova credencial do tipo "Tiny ERP API"
3. Insira seu token de acesso da API do Tiny ERP

## Funcionalidades

### Produtos
- **Obter Produtos**: Lista produtos com suporte a paginação
  - Parâmetro: Número de páginas

### Pedidos
- **Obter Dados de Pedido**: Consulta informações detalhadas de um pedido
  - Parâmetro obrigatório: Número do pedido

### Usuários
- **Obter Dados de Usuário**: Consulta informações de usuários
  - Parâmetros opcionais:
    - Nome do usuário
    - Mês de nascimento
    - CPF
    - Flag para obter todos os usuários

## Desenvolvimento

Para contribuir com o desenvolvimento:

1. Clone o repositório
2. Instale as dependências:
```bash
npm install
```
3. Compile o código:
```bash
npm run build
```
4. Para desenvolvimento com recompilação automática:
```bash
npm run dev
```

## Licença

MIT 
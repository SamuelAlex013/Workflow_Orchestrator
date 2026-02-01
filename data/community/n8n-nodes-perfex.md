# n8n-nodes-perfex

Um nó n8n para integração com o **Perfex CRM** através do módulo WON API com **compatibilidade total**.

## 🚀 Versão 0.2.0 - Melhorias Importantes

### ✅ **Compatibilidade Total com WON API**
- **Autenticação corrigida**: Agora usa header `Authorization` conforme padrão WON API
- **Endpoints corretos**: Todos os endpoints seguem o padrão `/won_api/won/api/`
- **Operação JOIN**: Implementada para associação de clientes por CNPJ/CPF
- **Tratamento de erros aprimorado**: Códigos de status específicos e mensagens detalhadas
- **Validações robustas**: CPF/CNPJ, email, datas e JSON

### 🔧 **Melhorias Técnicas**
- **Paginação**: Suporte a `limit` e `page` em todas as operações de listagem
- **Validação de dados**: Formatação automática de CNPJ/CPF, validação de email e datas
- **Tratamento de arrays**: Conversão automática de strings para arrays (membros, assignees, items)
- **Mensagens de erro específicas**: Códigos 401, 404, 422 com mensagens contextuais

## Instalação

Para instalar este nó n8n:

```bash
npm install n8n-nodes-perfex
```

## Configuração

Para usar este nó, você precisará configurar as credenciais do Perfex CRM:

1. **URL Base**: A URL base do seu Perfex CRM (ex: `https://seu-perfex.com`)
2. **API Token**: O token da API do Perfex CRM (único campo necessário para autenticação)

### Como obter o API Token

1. Acesse seu Perfex CRM
2. Vá em **Setup** → **Staff**
3. Edite um usuário staff
4. Na aba **API**, gere ou copie o token de API existente

## Recursos Disponíveis

Este nó oferece operações completas para os seguintes recursos do Perfex:

### 📋 Clients (Clientes)
- **Create**: Criar novo cliente
- **Read**: Obter dados de um cliente específico
- **Update**: Atualizar dados de um cliente
- **Delete**: Remover um cliente
- **List**: Listar todos os clientes
- **🆕 Join**: Associar cliente por CNPJ/CPF (novo!)

### 👤 Contacts (Contatos)
- **Create**: Criar novo contato
- **Read**: Obter dados de um contato específico
- **Update**: Atualizar dados de um contato
- **Delete**: Remover um contato
- **List**: Listar todos os contatos

### 🎯 Leads (Leads)
- **Create**: Criar novo lead
- **Read**: Obter dados de um lead específico
- **Update**: Atualizar dados de um lead
- **Delete**: Remover um lead
- **List**: Listar todos os leads

### 📊 Projects (Projetos)
- **Create**: Criar novo projeto
- **Read**: Obter dados de um projeto específico
- **Update**: Atualizar dados de um projeto
- **Delete**: Remover um projeto
- **List**: Listar todos os projetos

### ✅ Tasks (Tarefas)
- **Create**: Criar nova tarefa
- **Read**: Obter dados de uma tarefa específica
- **Update**: Atualizar dados de uma tarefa
- **Delete**: Remover uma tarefa
- **List**: Listar todas as tarefas

### 💰 Invoices (Faturas)
- **Create**: Criar nova fatura
- **Read**: Obter dados de uma fatura específica
- **Update**: Atualizar dados de uma fatura
- **Delete**: Remover uma fatura
- **List**: Listar todas as faturas

## 🆕 Novos Recursos v0.2.0

### Operação JOIN para Clientes
Permite associar clientes existentes usando CNPJ/CPF:

```javascript
// Exemplo de uso da operação JOIN
{
  "resource": "client",
  "operation": "join",
  "vat": "12.345.678/0001-90"
}
```

### Paginação Avançada
Todas as operações de listagem agora suportam:

```javascript
{
  "operation": "getAll",
  "options": {
    "limit": 50,        // Máximo de registros por página
    "page": 2,          // Número da página
    "filters": "{\"active\": 1, \"country\": \"Brasil\"}"
  }
}
```

### Validações Automáticas

#### CNPJ/CPF
- Remoção automática de caracteres especiais
- Validação de tamanho (11 dígitos para CPF, 14 para CNPJ)
- Formatação automática

#### Email
- Validação de formato em contatos e leads
- Regex robusto para verificação

#### Datas
- Validação de formato YYYY-MM-DD
- Aplicado em tarefas e faturas

#### JSON
- Validação de arrays em faturas (items)
- Conversão automática de strings para arrays

## Como Usar

1. **Adicionar Credenciais**: Configure sua URL base e API Token do Perfex
2. **Escolher Recurso**: Selecione o recurso desejado (Client, Contact, Lead, etc.)
3. **Escolher Operação**: Selecione a operação (Create, Read, Update, Delete, List, Join)
4. **Preencher Parâmetros**: Complete os campos necessários para a operação
5. **Configurar Opções**: Use paginação e filtros conforme necessário

## Exemplos de Uso

### Criar um Cliente com Validação
```javascript
{
  "resource": "client",
  "operation": "create",
  "clientData": {
    "company": "Empresa Exemplo Ltda",
    "vat": "12.345.678/0001-90",  // Será validado e formatado automaticamente
    "phonenumber": "(11) 99999-9999",
    "country": "Brasil",
    "city": "São Paulo"
  }
}
```

### Associar Cliente por CNPJ
```javascript
{
  "resource": "client",
  "operation": "join",
  "vat": "12345678000190"  // Aceita com ou sem formatação
}
```

### Listar com Paginação e Filtros
```javascript
{
  "resource": "client",
  "operation": "getAll",
  "options": {
    "limit": 25,
    "page": 1,
    "filters": "{\"active\": 1, \"country\": \"Brasil\"}"
  }
}
```

### Criar Tarefa com Validação de Data
```javascript
{
  "resource": "task",
  "operation": "create",
  "taskData": {
    "name": "Tarefa Importante",
    "duedate": "2024-12-31",  // Formato validado automaticamente
    "assignees": "1,2,3",     // Convertido para array automaticamente
    "priority": 3
  }
}
```

## Tratamento de Erros

A versão 0.2.0 inclui tratamento robusto de erros:

- **401**: Erro de autenticação (token inválido)
- **404**: Recurso não encontrado
- **422**: Dados inválidos (com detalhes específicos)
- **Conexão**: Erros de rede e timeout
- **Validação**: Erros de formato de dados

## Características Técnicas

- **Total de Operações**: 31 operações (6 recursos × 5 operações + JOIN)
- **Autenticação**: Via API Token com header `Authorization`
- **Endpoints**: Padrão WON API `/won_api/won/api/`
- **Dependências**: axios para requisições HTTP
- **Compatibilidade**: n8n versão 0.107.0+
- **Node.js**: Versão 16.0.0 ou superior
- **Validações**: CPF/CNPJ, email, datas, JSON
- **Paginação**: Suporte completo com limit e page

## Migração da v0.1.x para v0.2.0

### ⚠️ **Mudanças Importantes**

1. **Autenticação**: O header mudou de `X-API-TOKEN` para `Authorization`
2. **Endpoints**: Agora seguem o padrão `/won_api/won/api/`
3. **Nova operação**: JOIN disponível para clientes
4. **Validações**: Dados são validados automaticamente

### 🔄 **Como Migrar**

1. **Atualize o pacote**:
   ```bash
   npm update n8n-nodes-perfex
   ```

2. **Reconfigure credenciais**: As credenciais existentes continuam funcionando

3. **Teste workflows**: Verifique se todos os workflows funcionam corretamente

4. **Aproveite novos recursos**: Use paginação, JOIN e validações automáticas

## Suporte

- **Documentação da API**: [Perfex CRM API Documentation](https://docs.perfexcrm.com/api/)
- **Repositório**: [GitHub](https://github.com/Matheusbaiense/nodeperfex)
- **Issues**: [GitHub Issues](https://github.com/Matheusbaiense/nodeperfex/issues)

## Changelog

### v0.2.0 (2024-12-19)
- ✅ Compatibilidade total com módulo WON API
- ✅ Autenticação corrigida (Authorization header)
- ✅ Endpoints corretos (/won_api/won/api/)
- ✅ Nova operação JOIN para clientes
- ✅ Paginação com limit e page
- ✅ Validações automáticas (CPF/CNPJ, email, datas)
- ✅ Tratamento de erros aprimorado
- ✅ Conversão automática de tipos de dados

### v0.1.5 (2024-12-19)
- ✅ Remoção completa do campo apiKey da interface
- ✅ Simplificação da autenticação

### v0.1.4 (2024-12-19)
- ✅ Campo apiKey tornado opcional
- ✅ Documentação atualizada

### v0.1.3 (2024-12-19)
- ✅ Refatoração completa do código
- ✅ Correção de imports problemáticos
- ✅ 30 operações implementadas

## Licença

MIT License

## Autor

**Matheus Baiense**
- Email: matheusbaiense@gmail.com
- GitHub: [@Matheusbaiense](https://github.com/Matheusbaiense)

## Agradecimentos

- Equipe do n8n por criar uma plataforma incrível
- Equipe do Perfex CRM por desenvolver um CRM robusto
- Todos os contribuidores que ajudaram no projeto

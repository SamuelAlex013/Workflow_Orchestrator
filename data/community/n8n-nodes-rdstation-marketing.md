![Banner image](https://github.com/user-attachments/assets/f9e3d3a4-16dd-4fc5-a8d3-a220e822cb55)

# RD Station Marketing community node for n8n

Este é um community node para n8n que permite integração com a API do RD Station Marketing.

## Funcionalidades

- **Autenticação OAuth2** completa com refresh token automático
- **Gestão de Contatos**: Criar, atualizar, buscar e listar contatos
- **Eventos**: Criar eventos de conversão e personalizados
- **Tratamento de Erros**: Mensagens claras e tratamento robusto de erros
- **Validação**: Validação automática de dados de entrada

## Instalação

Para instalar este community node, siga os passos abaixo:

### Via npm

```bash
npm install n8n-nodes-rdstation-marketing
```

### Via n8n Community Nodes

1. Acesse suas configurações do n8n
2. Navegue até "Community Nodes"
3. Instale `n8n-nodes-rdstation-marketing`

## Configuração

### 1. Criar Aplicativo no RD Station

1. Acesse [RD Station App Store](https://appstore.rdstation.com/pt-BR/publisher)
2. Crie um novo aplicativo
3. Configure as URLs de callback:
   - Para desenvolvimento: `http://localhost:5678/rest/oauth2-credential/callback`
   - Para produção: `https://your-n8n-domain.com/rest/oauth2-credential/callback`
4. Anote o `Client ID` e `Client Secret`

### 2. Configurar Credenciais no n8n

1. No n8n, vá para "Credentials"
2. Crie uma nova credencial "RD Station Marketing OAuth2 API"
3. Insira o `Client ID` e `Client Secret` obtidos no passo anterior
4. Clique em "Connect my account" e autorize o acesso

## Uso

### Contatos

#### Criar ou Atualizar Contato

```json
{
  "email": "contato@exemplo.com",
  "name": "João Silva",
  "job_title": "Desenvolvedor",
  "mobile_phone": "+5511999999999",
  "city": "São Paulo",
  "state": "SP",
  "country": "Brasil",
  "tags": "lead,interessado,developer"
}
```

#### Buscar Contato

- Por email: `contato@exemplo.com`
- Por UUID: `12345678-1234-1234-1234-123456789012`

#### Listar Contatos

- Opção para retornar todos os contatos ou limitar a quantidade
- Paginação automática para grandes volumes

## Recursos

### Contatos
- ✅ Criar/Atualizar contato
- ✅ Buscar contato por email
- ✅ Buscar contato por UUID
- ✅ Listar todos os contatos
- 🔄 Tags (em desenvolvimento)

### Eventos
- 🔄 Criar evento de conversão (em desenvolvimento)
- 🔄 Criar evento personalizado (em desenvolvimento)
- 🔄 Associar eventos a contatos (em desenvolvimento)

### Leads
- 🔄 Informações do funil (em desenvolvimento)

### Oportunidades
- 🔄 Marcar como ganho/perdido (em desenvolvimento)

## Tratamento de Erros

O node possui tratamento robusto de erros da API do RD Station Marketing:

- **Erros de Validação**: Mensagens claras sobre dados inválidos
- **Erros de Autenticação**: Renovação automática de tokens
- **Erros de Rate Limit**: Informações sobre limites da API
- **Erros de Conexão**: Tratamento de falhas de rede

## Desenvolvimento

### Configurar Ambiente de Desenvolvimento

```bash
# Clonar o repositório
git clone https://github.com/olivasdigital/n8n-nodes-rdstation-marketing.git
cd n8n-nodes-rdstation-marketing

# Instalar dependências
npm install

# Compilar
npm run build

# Executar testes de lint
npm run lint

# Corrigir problemas de lint automaticamente
npm run lintfix
```

### Estrutura do Projeto

```
├── credentials/
│   └── RdStationMarketingOAuth2Api.credentials.ts
├── nodes/
│   └── RdStationMarketing/
│       ├── RdStationMarketing.node.ts
│       ├── GenericFunctions.ts
│       └── rdstation.svg
├── dist/                    # Gerado após build
├── package.json
├── tsconfig.json
└── README.md
```

### Testando Localmente

```bash
# Link para teste local
npm link

# No diretório do n8n
npm link n8n-nodes-rdstation-marketing

# Reiniciar o n8n
```

## Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feat/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feat/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Suporte

- 📖 [Documentação da API RD Station Marketing](https://developers.rdstation.com/reference/introducao-rdsm)
- 🐛 [Reportar Issues](https://github.com/olivasdigital/n8n-nodes-rdstation-marketing/issues)
- 💬 [Discussões](https://github.com/olivasdigital/n8n-nodes-rdstation-marketing/discussions)

## Changelog

### v1.0.0
- ✅ Autenticação OAuth2 com RD Station Marketing
- ✅ Consultar contato
- ✅ Criar contato
- ✅ Atualizar contato
- ✅ Listar contatos
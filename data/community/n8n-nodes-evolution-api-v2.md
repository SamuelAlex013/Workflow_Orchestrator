# N8N Evolution API v2 Community Node

Este é um community node para o N8N que permite integração com a Evolution API v2 para WhatsApp.

## 🚀 Funcionalidades

- **Gerenciamento de Instâncias**: Criar, conectar, desconectar e gerenciar instâncias do WhatsApp
- **Envio de Mensagens**: Enviar mensagens de texto e mídia
- **Gerenciamento de Grupos**: Criar grupos e buscar membros
- **Verificação de Chat**: Verificar se um número é WhatsApp
- **Webhooks**: Configurar webhooks para eventos
- **Integrações**: Suporte para integração com Chatwoot

## 📦 Instalação

### Via NPM (Recomendado)

```bash
npm install n8n-nodes-evolution-api-v2
```

### Via N8N Community Nodes

1. Vá para **Settings** > **Community Nodes**
2. Clique em **Install**
3. Digite: `n8n-nodes-evolution-api-v2`
4. Clique em **Install**

## 🔧 Configuração

### Credenciais

1. Crie uma nova credencial do tipo **Evolution API**
2. Configure:
   - **Server URL**: URL do seu servidor Evolution API
   - **API Token**: Token de autenticação da API

### Recursos Disponíveis

#### Instância
- **Criar Instância**: Cria uma nova instância do WhatsApp
- **Buscar Instâncias**: Lista todas as instâncias disponíveis
- **Conectar Instância**: Conecta a uma instância específica
- **Reiniciar Instância**: Reinicia uma instância
- **Estado da Conexão**: Verifica o estado da conexão
- **Logout**: Faz logout de uma instância
- **Deletar Instância**: Remove uma instância
- **Definir Presença**: Define o status de presença

#### Mensagem
- **Enviar Texto**: Envia uma mensagem de texto
- **Enviar Imagem**: Envia uma imagem com legenda

#### Grupo
- **Criar Grupo**: Cria um novo grupo
- **Buscar Membros**: Lista membros de um grupo

#### Chat
- **Verificar WhatsApp**: Verifica se um número é WhatsApp

#### Evento
- **Webhook**: Configura webhooks para eventos

#### Integração
- **Chatwoot**: Configura integração com Chatwoot

## 🛠️ Desenvolvimento

### Pré-requisitos

- Node.js 18+
- npm ou yarn

### Instalação Local

```bash
git clone https://github.com/jfcardososantos/n8n-nodes-evolution-api-v2.git
cd n8n-nodes-evolution-api-v2
npm install
```

### Scripts Disponíveis

```bash
# Build do projeto
npm run build

# Desenvolvimento com watch
npm run dev

# Linting
npm run lint

# Formatação
npm run format

# Release (patch, minor, major)
npm run release:patch
npm run release:minor
npm run release:major
```

## 📝 Exemplos de Uso

### Enviar Mensagem de Texto

```javascript
// Configuração do node
{
  "resource": "message",
  "operation": "sendText",
  "instanceName": "minha-instancia",
  "number": "5511999999999",
  "messageText": "Olá! Esta é uma mensagem de teste."
}
```

### Criar Grupo

```javascript
// Configuração do node
{
  "resource": "group",
  "operation": "createGroup",
  "instanceName": "minha-instancia",
  "subject": "Grupo de Teste",
  "participants": ["5511999999999", "5511888888888"]
}
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**JF Cardoso Santos**
- Email: jfcardososantos@gmail.com
- GitHub: [@jfcardososantos](https://github.com/jfcardososantos)

## 🔗 Links

- [N8N](https://n8n.io/)
- [Evolution API](https://doc.evolution-api.com/)
- [NPM Package](https://www.npmjs.com/package/n8n-nodes-evolution-api-v2)

## 📈 Versionamento

Este projeto usa [SemVer](http://semver.org/) para versionamento. Para ver as versões disponíveis, veja as [tags neste repositório](https://github.com/jfcardososantos/n8n-nodes-evolution-api-v2/tags).

## 🆘 Suporte

Se você encontrar algum problema ou tiver dúvidas, por favor:

1. Verifique a [documentação da Evolution API](https://doc.evolution-api.com/)
2. Abra uma [issue no GitHub](https://github.com/jfcardososantos/n8n-nodes-evolution-api-v2/issues)
3. Entre em contato via email: jfcardososantos@gmail.com 
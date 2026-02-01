# n8n Community Nodes - Guru Digital Manager

[![npm version](https://badge.fury.io/js/n8n-nodes-guru-digital-manager.svg)](https://badge.fury.io/js/n8n-nodes-guru-digital-manager)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![n8n Community](https://img.shields.io/badge/n8n-Community%20Node-orange)](https://n8n.io)

Este pacote contém nodes do n8n para integração com a API do Guru Digital Manager, permitindo automações completas de gestão de contatos, transações e assinaturas.

## 🚀 Características

- ✅ **Gestão Completa de Contatos**: Criar, ler, atualizar e excluir contatos
- ✅ **Controle de Transações**: Gerenciar transações com diferentes status
- ✅ **Assinaturas**: Criar e gerenciar assinaturas de clientes
- ✅ **Autenticação Segura**: Header Auth Authorization
- ✅ **Interface Intuitiva**: Fácil configuração e uso
- ✅ **Tratamento de Erros**: Robustez e confiabilidade

## Instalação

Siga as instruções de instalação para [n8n community nodes](https://docs.n8n.io/integrations/community-nodes/installation/).

## Credenciais

### Guru Digital Manager API

Para usar este node, você precisa configurar as credenciais da API do Guru Digital Manager:

1. **User Token**: Seu token de usuário do Guru (formato: Bearer {user_token})

> **Nota**: Se você encontrar o erro "Node does not have any credentials set", certifique-se de que está usando a versão 1.5.2 ou superior do pacote. Veja [CREDENTIALS_SETUP.md](CREDENTIALS_SETUP.md) para instruções detalhadas de configuração.

## Nodes

### Guru Digital Manager

Este node permite interagir com os recursos da API do Guru Digital Manager:

#### Recursos Suportados

- **Contatos (Contacts)**: Gerenciamento completo de contatos
- **Transações (Transactions)**: Gerenciamento de transações
- **Assinaturas (Subscriptions)**: Gerenciamento de assinaturas

#### Operações Disponíveis

Para cada recurso, as seguintes operações estão disponíveis:

- **Create**: Criar um novo registro
- **Get**: Obter um registro específico por ID
- **Get All**: Listar todos os registros (com opção de limite)
- **Update**: Atualizar um registro existente
- **Delete**: Excluir um registro

#### Campos Específicos

##### Contatos
- Nome
- Email
- Telefone
- Documento (CPF/CNPJ)

##### Transações
- Valor
- Descrição
- Status (Pendente, Concluída, Falhou)

##### Assinaturas
- Plano
- Status (Ativa, Inativa, Cancelada)
- Data de Início

## Desenvolvimento

### Pré-requisitos

- Node.js (versão 16 ou superior)
- npm ou yarn

### Instalação de Dependências

```bash
npm install
```

### Compilação

```bash
npm run build
```

### Desenvolvimento

```bash
npm run dev
```

## Estrutura do Projeto

```
src/
├── credentials/
│   └── GuruDigitalManagerApi.credentials.ts
├── nodes/
│   └── GuruDigitalManager/
│       ├── GuruDigitalManager.node.ts
│       └── guruDigitalManager.svg
└── index.ts
```

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia nosso [Código de Conduta](CODE_OF_CONDUCT.md) antes de contribuir.

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/matheuskuboadapta/guru-digital-manager-community-node/issues)
- **Email**: matheus@adaptaconsultoria.com.br
- **Documentação**: [Exemplos de Uso](examples.md)

## 🙏 Agradecimentos

- [n8n](https://n8n.io) pela plataforma incrível
- [Guru Digital Manager](https://guru.com.br) pela API robusta
- Todos os contribuidores da comunidade

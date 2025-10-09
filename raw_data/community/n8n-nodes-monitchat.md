# n8n-nodes-monitchat

[![NPM version](https://img.shields.io/npm/v/n8n-nodes-monitchat.svg)](https://www.npmjs.com/package/n8n-nodes-monitchat)

Este pacote contém nós personalizados para o [n8n](https://n8n.io) que permitem integração com a plataforma omnichannel [Monitchat](https://monitchat.dev.br/), com foco específico em funcionalidades para WhatsApp.

## Sobre o Monitchat

Monitchat é uma plataforma omnichannel que permite gerenciar comunicações com clientes através de diversos canais, incluindo WhatsApp, Facebook Messenger, Instagram, e-mail, chat ao vivo e mais. Esta integração se concentra nas funcionalidades de comunicação via WhatsApp.

## Instalação

Para instalar este pacote no seu n8n, execute o seguinte comando no diretório raiz da sua instalação n8n:

```bash
npm install n8n-nodes-monitchat
```

Para usuários do pnpm:

```bash
pnpm add n8n-nodes-monitchat
```

## Funcionalidades

Este pacote fornece os seguintes nós para interação com a API Monitchat:

### Nó Monitchat

Este nó contém várias operações para trabalhar com o WhatsApp através da plataforma Monitchat:

#### Operações Disponíveis

1. **Envio de Mensagens**
   - Envie mensagens de texto para contatos do WhatsApp
   - Especifique o número de telefone e a conta WhatsApp para envio

2. **Envio de Comentários**
   - Adicione comentários internos às conversas
   - Útil para colaboração entre atendentes

3. **Encaminhamento de Conversas**
   - Encaminhe conversas para outros usuários da plataforma
   - Possibilidade de adicionar notas ao encaminhar

4. **Encaminhamento para Departamentos**
   - Encaminhe conversas para departamentos específicos
   - Gerencie atendimento por setores

5. **Respostas Automáticas**
   - Configure respostas automáticas para conversas
   - Otimize o tempo de resposta para perguntas frequentes

## Configuração

### Credenciais Necessárias

Para utilizar estes nós, você precisará:

1. Uma conta ativa na plataforma Monitchat
2. Uma API Key válida, que pode ser obtida no painel administrativo do Monitchat

Para configurar as credenciais no n8n:

1. Vá para `Credenciais` no menu do n8n
2. Clique em `Adicionar nova credencial`
3. Selecione o tipo `Monitchat`
4. Insira sua API Key no campo correspondente
5. Salve as credenciais

## Exemplo de Uso

### Envio de Mensagem pelo WhatsApp

1. Adicione o nó `Monitchat` ao seu fluxo de trabalho
2. Selecione a operação "Enviar Mensagem"
3. Configure o número de telefone do destinatário (com código do país)
4. Digite a mensagem a ser enviada
5. Selecione a conta WhatsApp para envio (se houver múltiplas contas disponíveis)
6. Execute o fluxo para enviar a mensagem

## Suporte

Para suporte ou dúvidas sobre este pacote, entre em contato:

- Email: bufalo.pc777@gmail.com
- GitHub: [https://github.com/paulopc777/nodes-start](https://github.com/paulopc777/nodes-start)

## Licença

[MIT](LICENSE.md)
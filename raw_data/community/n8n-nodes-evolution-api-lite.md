# N8N Evolution API Lite

Este é um Community Node para N8N que oferece uma versão simplificada e leve da integração com a **Evolution API v2.2+**. Desenvolvido para fornecer apenas as funcionalidades essenciais de envio de mensagens e verificação de números do WhatsApp.

## 📋 Sobre

Este projeto é baseado no excelente trabalho do [n8n-nodes-evolution-api](https://github.com/oriondesign2015/n8n-nodes-evolution-api) desenvolvido por **OrionDesign**. É uma versão lite que mantém apenas as funcionalidades mais essenciais, removendo a complexidade desnecessária para casos de uso simples.

**Créditos:** [OrionDesign](https://github.com/oriondesign2015) - Projeto original

## ⚙️ Requisitos

Para utilizar o nosso **Community Node**, é necessário atender aos seguintes requisitos:

* **N8N** na versão **1.54.4** ou superior
* **Evolution API** na versão **2.2.0** ou superior

## 📌 Recursos Disponíveis

### Mensagem

✉️ Este recurso concentra as funcionalidades essenciais relacionadas ao envio de mensagens através da Evolution API. Com ele, você pode enviar diversos tipos de conteúdo como textos, imagens, vídeos, áudios, documentos, contatos, listas interativas e botões.

**Lista de operações:**
- ✅ **Enviar Texto**
- ✅ **Enviar Imagem**
- ✅ **Enviar Video**
- ✅ **Enviar Audio**
- ✅ **Enviar Documento**
- ✅ **Enviar Contato**
- ✅ **Enviar Lista**
- ✅ **Enviar Botão**

### Chat

💬 Este recurso disponibiliza ferramentas para o gerenciamento de conversas e interações utilizando a Evolution API.

**Lista de operações:**
- ✅ **Verificar Numero**

## 🚀 Instalação

### Opção 1: Via NPM (Recomendado)

```bash
npm install n8n-nodes-evolution-api-lite
```

### Opção 2: Instalação Manual

1. Clone este repositório
2. Execute `npm install`
3. Execute `npm run build`
4. Copie a pasta `dist` para o diretório de custom nodes do seu N8N

## 🔧 Configuração

### Credenciais

1. **API URL**: URL da sua Evolution API (ex: http://localhost:8080)
2. **API Key**: Sua chave de API da Evolution API
3. **Instance Name**: Nome da instância do WhatsApp

### Exemplos de Uso

#### Enviar Texto
- Resource: Message
- Operation: Send Text
- Number: 5511999999999
- Text: Olá! Esta é uma mensagem de teste.

#### Enviar Imagem
- Resource: Message
- Operation: Send Image
- Number: 5511999999999
- Media URL: https://example.com/image.jpg
- Caption: Veja esta imagem incrível!

#### Verificar Número
- Resource: Chat
- Operation: Verify Number
- Number: 5511999999999

## 🤝 Contribuição

Contribua para o crescimento deste projeto! Você pode ajudar de diversas formas:

* **Pull Requests**: Envie melhorias, correções ou novas funcionalidades.
* **Issues**: Relate problemas ou sugira novas ideias.
* **Sugestões**: Compartilhe suas opiniões e feedbacks.
* **Documentação**: Ajude a melhorar ou expandir a documentação existente.

## 📌 Principais contribuidores

## Star History Chart

## Desenvolvido com ❤️ por OrionDesign

---

**Versão Lite** - Mantendo apenas as funcionalidades essenciais para casos de uso simples.

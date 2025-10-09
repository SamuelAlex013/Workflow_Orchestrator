# n8n-nodes-notebooklm 🧠

**Bilingual README — Português / English**

---

## Português (PT-BR)

Extensão (community node) para integrar **NotebookLM** com automações no n8n.

Funcionalidades incluídas:
- Criar notebook
- Fazer upload de documentos (PDF/DOCX)
- Fazer perguntas (“ask”)
- Listar notebooks
- Deletar notebooks

### Instalação

#### Opção 1: Docker (Recomendado - Mais Fácil)
```bash
# Baixar e executar n8n com o node NotebookLM
docker run -p 5678:5678 enzomine456/n8n-notebooklm:latest

# Ou usar docker-compose
curl -O https://raw.githubusercontent.com/Enzomine456/n8n-nodes-notebooklm/main/docker-compose.public.yml
docker-compose -f docker-compose.public.yml up -d
```

#### Opção 2: NPM (Desenvolvimento)
```bash
npm install n8n-nodes-notebooklm
```

### Desenvolvimento / Teste local

#### Método 1: Docker (Recomendado)
```bash
# Clone o repositório
git clone https://github.com/Enzomine456/n8n-nodes-notebooklm.git
cd n8n-nodes-notebooklm

# Instale as dependências
npm install

# Execute com Docker Compose
npm run dev
# ou
docker-compose up -d

# Acesse o n8n em: http://localhost:5678
# Usuário: admin / Senha: admin123
```

#### Método 2: Instalação Manual
```bash
npm install
npm run build
npm link
# na pasta do n8n:
npm link n8n-nodes-notebooklm
```

### Imagens Docker Disponíveis

#### Imagens Públicas (Docker Hub)
- **`enzomine456/n8n-notebooklm:latest`** - n8n completo com o node NotebookLM
- **`enzomine456/n8n-nodes-notebooklm:latest`** - Apenas o node (para desenvolvimento)

#### Uso Rápido
```bash
# Executar n8n com NotebookLM
docker run -p 5678:5678 enzomine456/n8n-notebooklm:latest

# Acesse: http://localhost:5678
# Usuário: admin / Senha: admin123
```

### Comandos Docker para Desenvolvimento
```bash
# Build da imagem
npm run docker:build

# Executar container
npm run docker:run

# Subir ambiente completo (n8n + node)
npm run docker:compose:up

# Parar ambiente
npm run docker:compose:down

# Ver logs
npm run docker:compose:logs
```

### Credenciais
Suporta:
- API Key
- Service Account JSON (recomendado) — o node troca o JSON por um access token via google-auth-library

### Exemplo de workflow
Importe `workflows/examples/create-and-ask.workflow.json` no n8n.

### Configuração Docker para Produção

Para usar em produção, você pode criar um Dockerfile personalizado que inclui o n8n com o node:

```dockerfile
FROM n8nio/n8n:latest

# Instalar o node customizado
USER root
RUN npm install -g n8n-nodes-notebooklm
USER node

# Configurações adicionais do n8n
ENV N8N_BASIC_AUTH_ACTIVE=true
ENV N8N_BASIC_AUTH_USER=admin
ENV N8N_BASIC_AUTH_PASSWORD=your_secure_password
```

Ou usar o docker-compose.yml fornecido que já está configurado para desenvolvimento e pode ser adaptado para produção.

---

## English (EN)

Community node to integrate **NotebookLM** with n8n automations.

Included features:
- Create notebooks
- Upload documents (PDF/DOCX)
- Ask questions (query)
- List notebooks
- Delete notebooks

### Install
```bash
npm install n8n-nodes-notebooklm
```

### Local development / Testing
```bash
npm install
npm run build
npm link
# in n8n folder:
npm link n8n-nodes-notebooklm
```

### Credentials
Supports:
- API Key
- Service Account JSON (recommended) — exchanged for an access token using google-auth-library

### Example workflow
Import `workflows/examples/create-and-ask.workflow.json` into n8n.

---

Author: Enzo Luis (Enzomine456) — https://github.com/Enzomine456
License: MIT

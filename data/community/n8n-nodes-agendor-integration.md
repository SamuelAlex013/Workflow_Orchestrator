<div align="center">

<table border="0">
<tr>
<td align="center" style="background-color: white; border-radius: 50%; padding: 10px;">
<img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" width="80" alt="n8n Logo" style="background-color: white; border-radius: 50%; padding: 5px;"/>
</td>
<td align="center" style="font-size: 30px; padding: 0 20px;">
<h2>+</h2>
</td>
<td align="center">
<img src="https://raw.githubusercontent.com/leonidasjf/n8n-nodes-agendor-crm/main/assets/agendorlogo.ico" width="80" alt="Agendor Logo"/>
</td>
</tr>
</table>

# 🚀 Agendor CRM - Integração Completa para n8n

**✨ 100% da API Agendor v3 em Português - Versão 2.0.0**

[![npm version](https://badge.fury.io/js/n8n-nodes-agendor-integration.svg)](https://badge.fury.io/js/n8n-nodes-agendor-integration)
[![npm downloads](https://img.shields.io/npm/dm/n8n-nodes-agendor-integration.svg)](https://www.npmjs.com/package/n8n-nodes-agendor-integration)
[![GitHub stars](https://img.shields.io/github/stars/leonidasjf/agendor_crm-n8n-nodes.svg)](https://github.com/leonidasjf/agendor_crm-n8n-nodes)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*🎯 Integração mais completa e intuitiva do Agendor para n8n - Interface 100% em português com estrutura otimizada*

</div>

---

## 🎉 **Novidades da Versão 2.0.0**

### ✨ **Revolucionamos a Experiência**
- **🇧🇷 100% em Português:** Interface completamente traduzida para o mercado brasileiro
- **🎯 Estrutura Otimizada:** 37% menos complexidade mantendo 100% da funcionalidade
- **🚀 Cobertura Completa:** 100% da API Agendor v3 implementada (vs. 25% anterior)
- **🧠 Busca Inteligente:** Operações agrupadas logicamente por critério

### 📊 **De 4 para 8 Resources Completos**
```
✅ Pessoa (5 operações)     ✅ Funil (2 operações)
✅ Empresa (5 operações)    ✅ Produto (2 operações)
✅ Negócio (6 operações)    ✅ Usuário (1 operação)
✅ Tarefa (4 operações)     ✅ Sistema (3 operações)
```

---

## 🎯 **Funcionalidades Destacadas**

### 🔍 **Busca Inteligente Unificada**
Cada resource possui busca unificada com múltiplos critérios:

#### 👤 **Pessoas**
```
Buscar → Por ID | Por E-mail | Por Telefone | Por CPF | Listar Todos
```

#### 🏢 **Empresas**
```
Buscar → Por ID | Por CNPJ | Listar Todos
```

#### 💼 **Negócios**
```
Buscar → Por ID | Por Etapa | Por Responsável | Por Status | Por Empresa | Listar Todos
```

### 🔄 **Operações Anti-Duplicação (Upsert)**
- **Pessoas:** Criar ou atualizar por e-mail/CPF
- **Empresas:** Criar ou atualizar por CNPJ
- **Automático:** Se não existe cria, se existe atualiza

### 📈 **Sincronização e Stream**
- **Atualizações Recentes:** Buscar registros atualizados desde uma data
- **Integração Perfeita:** Ideal para sincronização com outros sistemas
- **Pessoas, Empresas e Negócios:** Todos suportam stream

### 🎯 **Movimentação Inteligente de Negócios**
```
Mover → Alterar Etapa | Alterar Status (Ganho/Perdido) | Alterar Funil
```

### ⚙️ **Sistema e Metadados**
- **Categorias:** Listar todas as categorias
- **Origens de Lead:** Obter origens disponíveis
- **Campos Customizados:** Por tipo (pessoas, empresas, negócios)

---

## 🚀 **Instalação**

### Via npm
```bash
npm install n8n-nodes-agendor-integration
```

### Via Community Nodes (n8n Cloud/Self-hosted)
1. Acesse **Settings** → **Community Nodes**
2. Clique em **Install a community node**
3. Digite: `n8n-nodes-agendor-integration`
4. Clique em **Install**

---

## 🔐 **Configuração**

### 1. Obter Token da API Agendor
1. Acesse sua conta no [Agendor](https://app.agendor.com.br/)
2. Vá em **Configurações** → **Integrações**
3. Clique em **Token de API**
4. Copie seu token

### 2. Configurar Credenciais no n8n
1. No n8n, vá para **Credentials**
2. Clique em **+ Add Credential**
3. Busque por **Agendor API**
4. Preencha:
   - **API Token:** Seu token copiado do Agendor
   - **API URL:** `https://api.agendor.com.br/v3` (padrão)

---

## 📖 **Exemplos de Uso**

### 🔍 **Buscar Pessoa por CPF**
```
Recurso: Pessoa
Operação: Buscar
Tipo de Busca: Por CPF
CPF: 12345678901
Incluir Campos Customizados: true
```

### 🏢 **Criar ou Atualizar Empresa (Anti-duplicação)**
```
Recurso: Empresa
Operação: Criar ou Atualizar
Nome: Empresa XYZ
CNPJ: 12345678000195
E-mail: contato@empresa.com
```

### 💼 **Mover Negócio para Próxima Etapa**
```
Recurso: Negócio
Operação: Mover
Tipo de Movimentação: Alterar Etapa
ID do Negócio: 123456
Nova Etapa: 5
```

### 📊 **Listar Negócios Ganhos Recentemente**
```
Recurso: Negócio
Operação: Buscar
Tipo de Busca: Por Status
Status: Ganho
```

### 📈 **Sincronizar Atualizações**
```
Recurso: Pessoa
Operação: Atualizações Recentes
Data Inicial: 2025-01-01T00:00:00Z
```

### 🌊 **Obter Funis e Etapas**
```
Recurso: Funil
Operação: Listar Funis
```

---

## 🎯 **Casos de Uso Avançados**

### 1. **Pipeline de Lead Qualification**
```
Webhook → Pessoa (Criar ou Atualizar) → Empresa (Criar ou Atualizar) → Negócio (Criar)
```

### 2. **Follow-up Automático**
```
Schedule → Negócio (Buscar por Etapa) → Filter (sem atividade) → Tarefa (Criar)
```

### 3. **Relatório de Performance**
```
Schedule → Negócio (Buscar Ganhos) → Usuário (Listar) → Analytics (Calcular) → Email (Enviar)
```

### 4. **Prevenção de Duplicatas**
```
Webhook → Pessoa (Buscar por E-mail) → IF (não existe) → Pessoa (Criar) ELSE → Pessoa (Atualizar)
```

### 5. **Sincronização Bidirecional**
```
Schedule → Pessoa (Atualizações Recentes) → External System (Update) → Log (Success)
```

---

## 📋 **Resources e Operações Completas**

### 👤 **Pessoa (5 operações)**
- **Buscar:** ID, E-mail, Telefone, CPF, Listar Todos
- **Criar:** Nova pessoa com todos os campos
- **Atualizar:** Pessoa existente
- **Criar ou Atualizar:** Upsert por e-mail/CPF
- **Atualizações Recentes:** Stream de mudanças

### 🏢 **Empresa (5 operações)**
- **Buscar:** ID, CNPJ, Listar Todos
- **Criar:** Nova empresa com todos os campos
- **Atualizar:** Empresa existente
- **Criar ou Atualizar:** Upsert por CNPJ
- **Atualizações Recentes:** Stream de mudanças

### 💼 **Negócio (6 operações)**
- **Buscar:** ID, Etapa, Responsável, Status, Empresa, Listar Todos
- **Criar:** Novo negócio
- **Atualizar:** Negócio existente
- **Mover:** Etapa, Status, Funil
- **Atualizações Recentes:** Stream de mudanças
- **Histórico de Movimentações:** Log de mudanças

### ✅ **Tarefa (4 operações)**
- **Criar:** Nova tarefa
- **Obter:** Tarefa específica
- **Listar:** Múltiplas tarefas
- **Atualizar:** Tarefa existente

### 🌊 **Funil (2 operações)**
- **Listar Funis:** Todos os funis de vendas
- **Listar Etapas:** Etapas dos funis

### 📦 **Produto (2 operações)**
- **Buscar:** ID, Código, Listar Todos
- **Criar:** Novo produto

### 👥 **Usuário (1 operação)**
- **Buscar:** ID, E-mail, Listar Todos

### ⚙️ **Sistema (3 operações)**
- **Obter Categorias:** Todas as categorias
- **Obter Origens de Lead:** Todas as origens
- **Obter Campos Customizados:** Por tipo de entidade

---

## 🔧 **Desenvolvimento**

### Pré-requisitos
- Node.js 18+
- npm/pnpm

### Setup Local
```bash
git clone https://github.com/leonidasjf/agendor_crm-n8n-nodes
cd agendor_crm-n8n-nodes
npm install
npm run build
```

### Scripts Disponíveis
```bash
npm run build      # Build do projeto
npm run dev        # Watch mode para desenvolvimento
npm run lint       # Lint do código
npm run format     # Format do código
```

---

## 📚 **Documentação e Recursos**

### 🔗 **Links Úteis**
- [Documentação Agendor API v3](https://api.agendor.com.br/docs/)
- [n8n Community Nodes](https://docs.n8n.io/integrations/community-nodes/)
- [GitHub Repository](https://github.com/leonidasjf/agendor_crm-n8n-nodes)

### 📖 **Documentação do Projeto**
- `AGENDOR_API_MAPPING.md` - Mapeamento completo da API
- `AGENDOR_NODE_OPTIMIZATION.md` - Estrutura otimizada
- `TRADUCAO_INTERFACE.md` - Guia de tradução
- `AGENDOR_NODE_COMPLETO.md` - Documentação completa

---

## 🤝 **Contribuição**

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/amazing-feature`)
3. Commit suas mudanças (`git commit -m 'Add amazing feature'`)
4. Push para a branch (`git push origin feature/amazing-feature`)
5. Abra um Pull Request

---

## 📊 **Comparação de Versões**

| Aspecto | v1.x | v2.0.0 |
|---------|------|--------|
| **Resources** | 4 | 8 |
| **Operações** | 16 | 28 |
| **Cobertura da API** | ~25% | 100% |
| **Interface** | Inglês | Português |
| **Busca** | Fragmentada | Unificada |
| **Upsert** | ❌ | ✅ |
| **Stream** | ❌ | ✅ |
| **Campos Customizados** | ❌ | ✅ |

---

## 🏷️ **Keywords**

n8n, agendor, crm, automation, workflow, integration, sales, pipeline, leads, brasil, português

---

## ⚖️ **Termos e Responsabilidade**

- **Não-oficial:** Este node não é desenvolvido, mantido ou endossado pela empresa Agendor
- **Independente:** Projeto independente não afiliado ao Agendor
- **Responsabilidade:** O uso é por conta e risco do usuário

---

<div align="center">

**🚀 Desenvolvido por [Leônidas Caldeira](https://github.com/leonidasjf)**

*Transforme seu CRM em uma máquina de automação!*

</div>
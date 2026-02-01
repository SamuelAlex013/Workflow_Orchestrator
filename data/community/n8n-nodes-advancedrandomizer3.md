![Advanced Randomizer node for n8n](./cover.png)

# n8n-nodes-advanced-randomizer

[![Build & Publish](https://github.com/RhadzonyJr/n8n-nodes-advanced-randomizer/actions/workflows/publish.yml/badge.svg)](https://github.com/RhadzonyJr/n8n-nodes-advanced-randomizer/actions)
[![npm (scoped)](https://img.shields.io/npm/v/n8n-nodes-advanced-randomizer)](https://www.npmjs.com/package/n8n-nodes-advanced-randomizer)
[![npm](https://img.shields.io/npm/dw/n8n-nodes-advanced-randomizer)](https://www.npmjs.com/package/n8n-nodes-advanced-randomizer)
[![Bundle size](https://img.shields.io/bundlephobia/min/n8n-nodes-advanced-randomizer)](https://bundlephobia.com/result?p=n8n-nodes-advanced-randomizer)

> **Advanced Randomizer** é um node _community_ para o [n8n](https://n8n.io/) que roteia itens de forma **aleatória**, **percentual** ou **sequencial** para até **10 saídas**.

<table>
<tr><th>Modo</th><th>Descrição</th></tr>
<tr><td><strong>Random</strong></td><td>Escolhe uma saída aleatória para cada item.</td></tr>
<tr><td><strong>Percentage</strong></td><td>Distribui conforme as porcentagens definidas pelo usuário (total 100%).</td></tr>
<tr><td><strong>Sequential</strong></td><td>Envia itens ciclicamente da Saída 1 → 2 → 3 … reiniciando ao final.</td></tr>
</table>

## ✨ Exemplos de uso
- **Testes A/B/n**  
  Divida leads em diferentes campanhas de marketing.
- **Balanceamento de carga**  
  Distribua chamadas de API entre múltiplos webhooks.
- **Roteamento condicional leve**  
  Crie ramificações probabilísticas sem precisar de code node.

---

## 🚀 Instalação

1. Siga o guia oficial para instalar community nodes  
   <https://docs.n8n.io/integrations/community-nodes/installation/>
2. No diretório de instalação do n8n, execute:

```bash
npm install n8n-nodes-advanced-randomizer

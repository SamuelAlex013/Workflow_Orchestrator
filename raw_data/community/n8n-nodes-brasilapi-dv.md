# n8n-nodes-brasilapi-dv

> **Nodes customizados para n8n: consultas automáticas à BrasilAPI (CEP, DDD, CNPJ, FIPE e outros)**

Este pacote adiciona ao n8n vários nodes para buscar informações em diferentes endpoints da [BrasilAPI](https://brasilapi.com.br/), como CEP, DDD, CNPJ, FIPE, entre outros.
Perfeito para automatizar validações, enriquecer dados e turbinar seus workflows!

---

## ⚡ Instalação

No diretório do seu n8n, execute:

```bash 
npm install n8n-nodes-brasilapi-dv
```

Depois, **reinicie o n8n** para ativar os novos nodes.

---

## 🟢 Como usar

1. No editor do n8n, procure por qualquer node que comece com `BrasilAPI` (CEP, DDD, CNPJ, FIPE etc).
2. Adicione o node desejado ao seu workflow.
3. Configure os parâmetros conforme a consulta que precisa.
4. Rode o fluxo normalmente e aproveite a automação!

---

## 📚 Endpoints suportados

* **CEP** – Consulta de endereço via CEP
* **DDD** – Consulta de cidades e estados por DDD
* **CNPJ** – Informações completas de empresas
* **FIPE** – Marcas, modelos e preços de veículos
* **FERIADOS** - Lista os feriados nacionais de determinado ano.

*Novos endpoints da BrasilAPI podem ser adicionados futuramente!*

---

## 🧩 Exemplo de uso

### Consultando um CEP

```json
{
  "cep": "74310-110",
  "state": "GO",
  "city": "Goiânia",
  "neighborhood": "Vila Redenção",
  "street": "Rua 106",
  "service": "correios"
}
```

---

## 🖼️ Visual customizado

Cada node exibe um ícone exclusivo da BrasilAPI para facilitar a identificação visual dentro do n8n.

---

## 🤝 Contribua!

Pull Requests são **muito bem-vindos**!
Sugestões, bugs ou melhorias? Abra uma *issue*!

---

## 📄 Licença

MIT

---

**Autor:** Gabryel Goncalves

---

## ⭐ Dicas extras

* Para exemplos detalhados por endpoint, prints, badges ou links, é só pedir!
* Pode usar este README tranquilamente – ele já está pronto para publicação e está bem completo! 🚀

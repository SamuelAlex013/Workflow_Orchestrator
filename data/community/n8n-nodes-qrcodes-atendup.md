<p align="center">
  <img src="https://img.atendup.com/github/QRCodeAtendUP.png" alt="QR Code AtendUP Logo" style="max-width: 100%;" />
</p>

Um node profissional e personalizável para **n8n**, desenvolvido com foco no mercado brasileiro. Gere QR Codes com múltiplas finalidades, visualmente atrativos e otimizados para o seu fluxo de automações.

---

## 🚀 Principais Funcionalidades

### 📌 Tipos de QR Code Suportados

* **Texto/URL** – Links simples ou mensagens
* **PIX** – Pagamentos via chave PIX, com valor e descrição
* **Wi-Fi** – Conexão automática à rede (SSID, senha, segurança)
* **vCard/Contato** – Nome, telefone, email, empresa e mais
* **Email** – QR para envio de mensagens com assunto e corpo
* **Telefone/SMS** – Chamadas telefônicas e envio de SMS
* **WhatsApp** – Mensagens diretas com número e texto pré-definido

### 🎨 Personalização Avançada

* Cores customizáveis (fundo e frente)
* Tamanhos de 200x200 até 1000x1000px
* Formatos disponíveis: **PNG, JPG, SVG**
* Níveis de correção de erro: L, M, Q, H
* Margens ajustáveis
* Inserção de logo central (marca personalizada)

### 🧹 Templates Visuais

* **Corporativo** – Cinza claro + azul escuro
* **Casual** – Amarelo vibrante + coral
* **E-commerce** – Azul claro + azul escuro

### 🔧 Funcionalidades Extras

* **Batch generation** – Geração em massa de QR Codes
* **Preview automático** – Veja antes de usar
* **Validação inteligente** – Prevenção de erros nos dados
* **Assinatura AtendUP** – Branding sutil no metadado da imagem

---

## 🇧🇷 Funcionalidades para o Brasil

* Total compatibilidade com o sistema **PIX** do Banco Central
* Validação de dados como **CPF, CNPJ e telefones brasileiros**
* Templates otimizados para **empresas nacionais**

---

## 📦 Instalação

Veja o passo a passo completo no arquivo [`INSTALLATION.md`](./INSTALLATION.md)

---

## ⚙️ Como Usar

### 🛠️ Passo a passo

1. Adicione o node `QR Code AtendUP` ao seu fluxo no n8n
2. Escolha o tipo de QR Code
3. Preencha os campos conforme a necessidade
4. Personalize aparência e formato
5. Execute e use como quiser

### 📋 Exemplos

#### QR Code PIX

```json
{
  "qrCodeType": "pix",
  "pixKey": "usuario@empresa.com.br",
  "pixName": "João Silva",
  "pixCity": "São Paulo",
  "pixValue": 50.00,
  "pixDescription": "Pagamento de serviços"
}
```

#### QR Code Wi-Fi

```json
{
  "qrCodeType": "wifi",
  "wifiSSID": "MinhaRede",
  "wifiPassword": "minhasenha123",
  "wifiSecurity": "WPA"
}
```

#### QR Code WhatsApp

```json
{
  "qrCodeType": "whatsapp",
  "whatsappNumber": "5511999999999",
  "whatsappMessage": "Olá! Gostaria de mais informações."
}
```

---

## 📄 Saída do Node

Exemplo de retorno:

```json
{
  "qrCodeType": "pix",
  "qrData": "00020126580014BR.GOV.BCB.PIX...",
  "qrCodeImage": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
  "format": "png",
  "size": 300,
  "generatedBy": "AtendUP - atendup.com",
  "timestamp": "2025-07-24T22:18:06.714Z"
}
```

---

## 💬 Suporte & Contato

Se precisar de ajuda, fale com a gente!
Somos gente como você — e adoramos tecnologia! 🚀

* 🌐 **Site:** [atendup.com](https://www.atendup.com)
* 🛋 **WhatsApp:** [Clique para conversar](https://wa.me/5545999691163)
* 📧 **Email:** [contato@atendup.com](mailto:contato@atendup.com)

---

## 📄 Licença

Distribuído sob licença [MIT](./LICENSE).
Sinta-se livre para usar, melhorar e contribuir com este projeto.

---

> Desenvolvido com ❤️ por [AtendUP](https://www.atendup.com) — Soluções inteligentes que aproximam tecnologia e pessoas.

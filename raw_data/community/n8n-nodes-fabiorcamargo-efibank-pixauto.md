![Banner image](https://gnetbr.com/BJgSIUhlYs)

# n8n-nodes-efibank

O n8n-nodes-efibank é um nó personalizado para o n8n que simplifica a integração com a API Cobranças e a API Pix do Efibank, permitindo a automação de fluxos financeiros, como pagamentos, recebimentos e transações.

[Requisitos](#requisitos) 

[Instalação](#instalação)

[Instalação do nó](#instalação-do-nó)  

[Configuração do nó](#configuração-do-nó)  

## Requisitos

### Versão do Node.js
Este nó personalizado requer uma versão do Node.js compatível com o n8n. A versão mínima necessária é **18.17**, e a versão máxima suportada é **22**.

## Instalação

Para instalar o nó em uma instalação existente do n8n, utilize uma das opções abaixo:

### Instalação via NPM

```bash
$ npm install n8n-nodes-efibank
```

### Instalação via [GIT](https://github.com/efipay/n8n-nodes-efibank)

```bash
$ git clone https://github.com/efipay/n8n-nodes-efibank.git
```


## Instalação do nó

Para instalar corretamente o nó personalizado, siga estas etapas:

1. Instale as dependências:
```bash
npm install
```

2. Compile o código:
```bash
npm run build
```

3. Configure o link para uso local (desenvolvimento):
```bash
npm link
```

4. Inicie o n8n:
```bash
n8n
```

## Configuração do nó

No ambiente do <strong>n8n</strong>, acesse seu workflow e busque pelos nós **Efí Bank Cobranças** e **Efí Bank Pix**

### Configuração do Nó da API Cobranças
Na interface do n8n, configure suas credenciais:
1. Selecione o ambiente (Homologação/Produção);
2. Configure as credenciais Client ID e Client Secret para os dois ambientes. Para obter as credencias da aplicação, você pode acessar [esse tutorial](https://dev.efipay.com.br/docs/api-cobrancas/credenciais#obtendo-as-credenciais-da-aplica%C3%A7%C3%A3o);
3. Clique em Save.

### Configuração do Nó da API Pix
Na interface do n8n, configure suas credenciais:
1. Selecione o ambiente (Homologação/Produção);
2. Configure as credenciais Client ID e Client Secret para os dois ambientes. Para obter as credencias da aplicação, você pode acessar [esse tutorial](https://dev.efipay.com.br/docs/api-cobrancas/credenciais#obtendo-as-credenciais-da-aplica%C3%A7%C3%A3o);
3. Configure o certificado:
   - Gere um certificado em sua conta Efí, seguindo [este guia](https://sejaefi.com.br/central-de-ajuda/api/como-gerar-o-certificado-para-usar-a-api-pix?_gl=1*96b3d4*_gcl_au*MTgzNDQxMDgyMi4xNzQzNTA2MDI5#conteudo);
   - Converta o certificado .p12 fazendo o upload na [página de conversão](https://efipay.github.io/encode-credentials/certificado.html) e clique em "Codificar e Exibir" para obter os dados necessários;
   - Copie o conteúdo do Certificado e cole no campo "Certificado";
   - Copie o conteúdo da Key e cole no campo "Key";
4. Clique em Save.
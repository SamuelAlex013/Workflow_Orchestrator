# n8n-nodes-capivision

Este pacote contém um node personalizado para n8n que implementa funcionalidades de OCR usando múltiplos mecanismos.

## Características

- Suporte a múltiplos mecanismos de OCR:
  - Tesseract.js (sem necessidade de autenticação)
  - OCR.space (requer API Key)
  - AWS Textract (requer credenciais AWS)
- Aceita imagens em formato binário ou base64
- Múltiplos formatos de saída:
  - Texto puro
  - JSON estruturado
  - CSV normalizado
- Suporte a presets de layout para extração direcionada

## Instalação

### Via NPM (recomendado)

```bash
npm install n8n-nodes-capivision
```

### Manual

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/n8n-nodes-capivision.git
```

2. Instale as dependências
```bash
cd n8n-nodes-capivision
npm install
```

3. Compile o código
```bash
npm run build
```

4. Crie um link simbólico (para desenvolvimento)
```bash
npm link
```

5. Na sua instalação n8n, use o link
```bash
cd ~/.n8n
npm link n8n-nodes-capivision
```

## Configuração

### OCR.space
1. Obtenha uma API Key em [OCR.space](https://ocr.space/ocrapi)
2. Adicione uma nova credencial do tipo "OCR.space API" no n8n
3. Insira sua API Key

### AWS Textract
1. Configure um usuário IAM com acesso ao Textract
2. Adicione uma nova credencial do tipo "AWS Textract API" no n8n
3. Insira Access Key ID, Secret Access Key e Region

## Uso

1. Arraste o node "CAPIVISION OCR" para seu workflow
2. Selecione o mecanismo OCR desejado
3. Configure o formato de entrada (binário ou base64)
4. Escolha o formato de saída
5. Opcionalmente, configure um preset de layout

### Exemplo de Preset de Layout

```json
{
  "nome": { "x": 10, "y": 20, "w": 100, "h": 30 },
  "cpf": { "x": 150, "y": 20, "w": 100, "h": 30 }
}
```

## Desenvolvimento

### Estrutura do Projeto

```
n8n-nodes-capivision/
├── nodes/
│   ├── CapivisionOcr.node.ts
│   └── capivision.svg
├── credentials/
│   ├── OcrSpaceApi.credentials.ts
│   └── AwsTextractApi.credentials.ts
├── package.json
├── tsconfig.json
└── README.md
```

### Scripts Disponíveis

- `npm run build`: Compila o código TypeScript
- `npm run dev`: Compila em modo watch
- `npm run format`: Formata o código usando Prettier
- `npm run lint`: Executa o ESLint

### Publicação

1. Atualize a versão no package.json
```bash
npm version patch|minor|major
```

2. Faça o build
```bash
npm run build
```

3. Publique no NPM
```bash
npm publish
```

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

MIT

## Autor

Thawam Michels - [LinkedIn](https://www.linkedin.com/in/thawammichels/) 
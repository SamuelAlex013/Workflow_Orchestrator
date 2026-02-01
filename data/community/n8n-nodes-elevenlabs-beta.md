# n8n-nodes-elevenlabs

Este pacote contém nós para n8n que permitem integrar os serviços da API ElevenLabs em seus workflows, incluindo conversão de texto para fala, fala para texto, efeitos sonoros, e IA conversacional.

## Funcionalidades

### Texto para Voz (Text-to-Speech)
- Converte texto em fala natural usando a API da ElevenLabs
- Suporte para diferentes vozes e modelos
- Opções para ajustar estabilidade, similaridade e estilo
- Múltiplos formatos de saída (MP3, FLAC, WAV, etc.)

### Voz para Texto (Speech-to-Text)
- Conversão de áudio para texto usando a API da ElevenLabs
- Suporte para entrada de áudio via arquivo binário ou URL
- Suporte para os modelos Scribe
- Opções avançadas:
  - Definição de código de idioma
  - Diarização (identificação de diferentes falantes)
  - Timestamps com diferentes granularidades (palavra, caractere)
  - Marcação de eventos de áudio (risos, passos, etc.)

### Voz para Voz (Speech-to-Speech)
- Converte áudio de uma voz para outra
- Mantém o conteúdo original com nova voz
- Suporte para tradução entre idiomas
- Ajustes de similaridade e estabilidade da voz

### Alterador de Voz (Voice Changer)
- Modifica características de voz em arquivos de áudio
- Opções para ajustar similaridade e estabilidade
- Suporte para processamento de fala e canto

### Efeitos Sonoros (Sound Effects)
- Adiciona efeitos sonoros a arquivos de áudio
- Suporte para vários tipos de efeitos (ambiente, eco, reverberação, etc.)
- Controle de intensidade e timing dos efeitos

### Base de Conhecimento (Knowledge Base)
- Consulta bases de conhecimento através da API ElevenLabs
- Integra com documentos e fontes de informação

### Agentes de IA (AI Agents)
- Interação com agentes conversacionais da ElevenLabs
- Gerenciamento de sessões de conversa
- Suporte para respostas em áudio

## Instalação

### No n8n

1. Vá para **Configurações** > **Community Nodes**
2. Selecione **Install**
3. Digite `@thaleslaray/n8n-nodes-elevenlabs` no campo de pesquisa
4. Clique em instalar

### Manualmente

```bash
npm install @thaleslaray/n8n-nodes-elevenlabs
```

## Configuração

1. Obtenha sua chave de API em https://elevenlabs.io/account
2. No n8n, vá para **Credenciais** e adicione uma nova credencial do tipo **ElevenLabs API**
3. Insira sua chave de API no campo correspondente

## Uso

### Node Principal ElevenLabs

O nó principal ElevenLabs fornece acesso a todos os recursos em uma interface unificada, permitindo selecionar:

1. **Recurso**: Escolha entre Text-to-Speech, Speech-to-Text, Speech-to-Speech, Voice Changer, Sound Effects, Knowledge Base ou Agents
2. **Operação**: Selecione a operação específica a realizar com o recurso escolhido
3. **Configurações**: Ajuste os parâmetros específicos para a operação selecionada

### Nós Individuais

Você também pode usar os nós individuais para cada funcionalidade específica:

- **ElevenLabs Text-to-Speech**: Converte texto em fala de alta qualidade
- **ElevenLabs Speech-to-Text**: Transcreve áudio em texto
- **ElevenLabs Speech-to-Speech**: Converte voz de uma pessoa para outra
- **ElevenLabs Voice Changer**: Altera características de voz em arquivos de áudio
- **ElevenLabs Sound Effects**: Adiciona efeitos sonoros a arquivos de áudio
- **ElevenLabs Knowledge Base**: Consulta bases de conhecimento
- **ElevenLabs Agents**: Interage com agentes de IA conversacional

## Formatos de áudio suportados

A API suporta diversos formatos de áudio, incluindo:
- MP3
- WAV
- FLAC
- AAC
- OGG
- MP4
- AIFF
- WebM

## Formatos de vídeo suportados

Também é possível extrair e transcrever o áudio de arquivos de vídeo nos seguintes formatos:
- MP4
- AVI
- MKV
- MOV
- WMV
- FLV
- WebM
- MPEG
- 3GPP

## Exemplos de uso

### Converter texto em voz

1. Adicione o nó "ElevenLabs" ao seu workflow
2. Selecione o recurso "Texto para Voz" e a operação "Converter Texto em Voz"
3. Forneça o ID da voz, o texto a ser convertido e o modelo
4. Nas opções avançadas, ajuste parâmetros como estabilidade e similaridade
5. Execute o workflow para receber o arquivo de áudio gerado

### Transcrever um arquivo de áudio

1. Use um nó HTTP Request para baixar um arquivo de áudio ou use o nó Read Binary File para ler um arquivo local
2. Conecte esse nó ao nó "ElevenLabs" com o recurso "Voz para Texto"
3. Configure o nó para usar o modelo "Scribe v1"
4. Nas opções avançadas, defina o código de idioma desejado
5. Execute o workflow para obter a transcrição

### Adicionar efeitos sonoros a um áudio

1. Forneça um arquivo de áudio via nó anterior
2. Use o nó "ElevenLabs" com o recurso "Efeitos Sonoros"
3. Adicione os efeitos desejados com suas configurações
4. Execute o workflow para obter o áudio com os efeitos aplicados

## Desenvolvimento

1. Clone este repositório
2. Instale as dependências: `npm install`
3. Compile o código: `npm run build`
4. Crie um link simbólico: `npm link`
5. No diretório de instalação do n8n: `npm link @thaleslaray/n8n-nodes-elevenlabs`

## Publicação

1. Atualize a versão no package.json
2. Faça o build: `npm run build`
3. Publique no npm: `npm publish --access public`

## Licença

MIT 
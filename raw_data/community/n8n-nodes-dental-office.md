# n8n-nodes-dental-office

Este é um conector (node package) para n8n que permite integração com a API REST do Dental Office Cloud.

## Descrição

O conector permite que usuários do n8n automatizem fluxos de trabalho conectando dados de clínicas odontológicas com centenas de outros aplicativos suportados pelo n8n.

## Recursos Suportados

- **Usuários**: Criar, listar, obter, atualizar e remover usuários
- **Dentistas**: Gerenciar registros de dentistas
- **Pacientes**: Gerenciar registros de pacientes
- **Agendamentos**: Criar e gerenciar agendamentos, incluindo obter horários disponíveis
- **Cadeiras**: Gerenciar cadeiras odontológicas

## Pré-requisitos

- Conta do Dental Office Cloud no plano "Avançado"
- Credenciais de API (Client ID e Secret)
- URL base da API específica do cliente

## Instalação

```bash
npm install n8n-nodes-dental-office
```

## Configuração

1. No n8n, vá para "Credenciais" e adicione uma nova credencial do tipo "Dental Office API"
2. Preencha os seguintes campos:
   - **URL Base**: Sua URL específica da API (ex: `https://meu-cliente.api.app.dentaloffice.com.br`)
   - **Client ID**: Seu client_id fornecido pelo Dental Office
   - **Secret**: Seu secret fornecido pelo Dental Office

## Uso

1. Adicione o node "Dental Office" ao seu workflow
2. Selecione suas credenciais configuradas
3. Escolha o recurso desejado (Usuário, Dentista, Paciente, etc.)
4. Selecione a operação (Criar, Listar, Obter, etc.)
5. Configure os parâmetros necessários

## Autenticação

O conector gerencia automaticamente a autenticação usando Bearer tokens:
- Solicita um token usando suas credenciais
- Armazena o token em cache por 23 horas
- Renova automaticamente quando necessário

## Recursos Disponíveis

### Usuários
- Criar novo usuário
- Listar usuários com filtros
- Obter usuário específico
- Atualizar dados de usuário
- Remover usuário

### Dentistas
- Criar novo dentista
- Listar dentistas com filtros
- Obter dentista específico
- Atualizar dados de dentista
- Remover dentista

### Pacientes
- Criar novo paciente
- Listar pacientes com filtros
- Obter paciente específico
- Atualizar dados de paciente
- Remover paciente

### Agendamentos
- Criar novo agendamento
- Listar agendamentos
- Obter agendamento específico
- Atualizar agendamento
- Remover agendamento
- Obter horários disponíveis

### Cadeiras
- Criar nova cadeira
- Listar cadeiras
- Obter cadeira específica
- Atualizar cadeira
- Remover cadeira

## Solicitação de Credenciais

Para obter suas credenciais de API (Client ID e Secret), entre em contato com o suporte do Dental Office. Este recurso está disponível apenas para clientes do plano Avançado.

## Tratamento de Erros

O conector inclui tratamento robusto de erros:
- Mensagens de erro claras em português
- Retry automático em caso de expiração de token
- Validação de campos obrigatórios

## Suporte

Para suporte técnico, entre em contato com a equipe do Dental Office ou abra uma issue neste repositório.

## Licença

MIT
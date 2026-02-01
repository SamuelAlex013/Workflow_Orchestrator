# n8n-nodes-portainer

<p align="center"><br>
Este Community Node é uma solução 100% gratuita, criada com o intuito de simplificar e auxiliar toda a comunidade a integrar e utilizar ao máximo os principais recursos oferecidos pelo <b>Portainer</b> em seus projetos no N8N.
</p>
<br>
	
<div align="center">
  <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.npmjs.org%2Fdownloads%2Fpoint%2Flast-year%2Fn8n-nodes-portainer&query=downloads&style=for-the-badge&label=Total%20de%20Downloads&labelColor=%230d1117&color=%23359514&cacheSeconds=30&link=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fn8n-nodes-portainer" alt="Downloads Badge">
  <img src="https://img.shields.io/npm/v/n8n-nodes-portainer?style=for-the-badge&label=Versão&labelColor=%230d1117&color=%23007ACC" alt="Version Badge">
  <img src="https://img.shields.io/npm/l/n8n-nodes-portainer?style=for-the-badge&label=Licença&labelColor=%230d1117&color=%23FFA500" alt="License Badge">
</div>
<br>

<p align="center">
  <a href="mailto:contato@lumiaria.com.br"><img src="https://img.shields.io/badge/Email-Suporte-red?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>     
  <a href="https://github.com/ramonmatias19/n8n-nodes-portainer"><img src="https://img.shields.io/badge/GitHub-Repositório-black?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>     
  <a href="https://www.npmjs.com/package/n8n-nodes-portainer"><img src="https://img.shields.io/badge/NPM-Package-red?style=for-the-badge&logo=npm&logoColor=white" alt="NPM"></a>
</p>

> **Aviso:** Este node foi desenvolvido de forma independente para facilitar integrações com a API pública do Portainer no n8n.  
> Não é afiliado, endossado ou mantido pelo Portainer.  
> Todas as marcas citadas pertencem aos seus respectivos proprietários.

<h1></h1>

<h3>⚙️ Requisitos</h3>

Para utilizar o nosso **Community Node**, é necessário atender aos seguintes requisitos:  
- **N8N** na versão **1.54.4** ou superior  
- **Node.js** na versão **16.0.0** ou superior  
- **Conta ativa** no **Portainer** com token de API  

<h1></h1>

<h3>📌 Recursos Disponíveis</h3>

<h3>🐳 Containers</h3>
📝 Gerenciamento completo de containers Docker com operações avançadas de criação, execução, monitoramento e controle de ciclo de vida.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos containers</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar containers</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Exec</b> - Executar comandos nos containers</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do container</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Logs</b> - Obter logs do container</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os containers</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Stats</b> - Obter estatísticas de uso</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Inspect</b> - Inspecionar detalhes do container</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Pause</b> - Pausar containers em execução</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Restart</b> - Reiniciar containers</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Start</b> - Iniciar containers parados</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Stop</b> - Parar containers em execução</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Unpause</b> - Despausar containers pausados</summary>
	</details>
</details>

<h3>🖼️ Images</h3>
📝 Gerenciamento completo de imagens Docker incluindo build, pull, push, tag e análise de histórico para controle total do ciclo de vida das imagens.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Build</b> - Construir imagens a partir de Dockerfile</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar imagens</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas da imagem</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get History</b> - Obter histórico da imagem</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todas as imagens</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Inspect</b> - Inspecionar detalhes da imagem</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Pull</b> - Baixar imagens do registry</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Push</b> - Enviar imagens para o registry</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Tag</b> - Criar tags para imagens</summary>
	</details>
</details>

<h3>⚙️ Services (Docker Swarm)</h3>
📝 Gerenciamento completo de services Docker Swarm com criação, escalonamento, atualização e monitoramento para orquestração de containers distribuídos.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos services</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar services</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do service</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Logs</b> - Obter logs do service</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os services</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Scale</b> - Escalar number de réplicas</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do service</summary>
	</details>
</details>

<h3>🔐 Secrets (Docker Swarm)</h3>
📝 Gerenciamento seguro de secrets Docker Swarm para armazenamento e distribuição segura de informações sensíveis nos services.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos secrets</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar secrets</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do secret</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os secrets</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Inspect</b> - Inspecionar detalhes do secret</summary>
	</details>
</details>

<h3>📋 Configs (Docker Swarm)</h3>
📝 Gerenciamento de configs Docker Swarm para distribuição de arquivos de configuração e dados não-sensíveis aos services do cluster.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos configs</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar configs</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do config</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os configs</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Inspect</b> - Inspecionar detalhes do config</summary>
	</details>
</details>

<h3>🌐 Edge Groups</h3>
📝 Gerenciamento de grupos de edge computing para organização e controle centralizado de endpoints distribuídos geograficamente.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos grupos de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar grupos de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do grupo</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os grupos de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do grupo</summary>
	</details>
</details>

<h3>📦 Edge Stacks</h3>
📝 Gerenciamento de stacks de edge computing para deployment distribuído de aplicações em múltiplas localizações edge.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos stacks de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar stacks de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do stack</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os stacks de edge</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Status</b> - Obter status de deployment</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do stack</summary>
	</details>
</details>

<h3>🖥️ Nodes (Docker Swarm)</h3>
📝 Gerenciamento de nodes Docker Swarm para monitoramento e controle dos nós do cluster, incluindo status e configurações.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do node</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os nodes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Inspect</b> - Inspecionar detalhes do node</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do node</summary>
	</details>
</details>

<h3>📚 Stacks (Docker Compose)</h3>
📝 Gerenciamento de stacks Docker Compose para deployment e atualização de aplicações multi-container definidas em arquivos YAML.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar stacks</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do stack</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os stacks</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do stack</summary>
	</details>
</details>

<h3>📋 Registries</h3>
📝 Gerenciamento de registries de imagens Docker com suporte a múltiplos tipos incluindo DockerHub, ECR, Azure, GitLab e registries customizados.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos registries</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar registries</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do registry</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os registries</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações do registry</summary>
	</details>
</details>

<h3>👥 Teams</h3>
📝 Gerenciamento de equipes no Portainer para controle de acesso baseado em grupos e permissões colaborativas.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novas equipes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar equipes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas da equipe</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todas as equipes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações da equipe</summary>
	</details>
</details>

<h3>📄 Templates</h3>
📝 Gerenciamento de templates de aplicação do Portainer para deployment rápido de aplicações pré-configuradas.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do template</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os templates</summary>
	</details>
</details>

<h3>⚙️ Settings</h3>
📝 Gerenciamento de configurações do Portainer incluindo autenticação, políticas de segurança e configurações globais da plataforma.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter configurações atuais</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Update</b> - Atualizar configurações</summary>
	</details>
</details>

<h3>🔗 Webhooks</h3>
📝 Gerenciamento de webhooks para automação e integração com sistemas externos através de notificações HTTP.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Create</b> - Criar novos webhooks</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar webhooks</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os webhooks</summary>
	</details>
</details>

<h3>💻 System</h3>
📝 Informações do sistema Portainer incluindo status, versão e informações dos nós para monitoramento da plataforma.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get Status</b> - Obter status do sistema</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Version</b> - Obter versão do Portainer</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Nodes</b> - Obter informações dos nós</summary>
	</details>
</details>

<h3>👤 Users</h3>
📝 Gerenciamento de usuários do Portainer para controle de acesso e administração de contas.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do usuário</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os usuários</summary>
	</details>
</details>

<h3>💾 Volumes</h3>
📝 Gerenciamento de volumes Docker para persistência de dados e compartilhamento entre containers.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar volumes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os volumes</summary>
	</details>
</details>

<h3>🌐 Networks</h3>
📝 Gerenciamento de redes Docker para conectividade e isolamento entre containers.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Delete</b> - Deletar redes</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todas as redes</summary>
	</details>
</details>

<h3>🏢 Environments</h3>
📝 Gerenciamento de ambientes/endpoints do Portainer para conexão com diferentes instâncias Docker.
<br>
<details>
  <summary><b>Lista de operações</b></summary>
	<details>
  	<summary>   ✅ <b>Get</b> - Obter informações específicas do ambiente</summary>
	</details>
	<details>
  	<summary>   ✅ <b>Get Many</b> - Listar todos os ambientes</summary>
	</details>
</details>

<h1></h1>

<h3>🚀 Instalação</h3>

**Via n8n Community Nodes:**
1. Abra sua instância do n8n
2. Vá para **Settings** → **Community Nodes**
3. Instale o pacote: `n8n-nodes-portainer`
4. Reinicie o n8n

**Via NPM:**
```bash
npm install n8n-nodes-portainer
```

<h1></h1>

<h3>🤝 Contribuição</h3>

Contribua para o crescimento deste projeto! Você pode ajudar de diversas formas:  
- **Pull Requests**: Envie melhorias, correções ou novas funcionalidades.  
- **Issues**: Relate problemas ou sugira novas ideias.  
- **Sugestões**: Compartilhe suas opiniões e feedbacks.  
- **Documentação**: Ajude a melhorar ou expandir a documentação existente.  

<h1></h1>

<p align="center">
Desenvolvido com ❤️ por <b>Ramon Matias</b>
</p> 
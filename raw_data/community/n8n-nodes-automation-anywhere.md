# <img src="nodes/AutomationAnywhere/AutomationAnywhere.svg" height="40"> n8n Node for Automation Anywhere

This project is a work in progress. The initial goal is to provide node for integrating n8n workflows with Automation Anywhere.

## Todo
- [x] Authentication credentials
- [x] Bot deploy
	- [x] Basic bot deploy
	- [x] Callback URL
	- [x] Callback Headers
	- [x] Bot Inputs
	- [x] List users with unattended license
	- [x] List device pools
- [x] Manage Executions
	- [x] Start
	- [x] Pause
	- [x] Resume
	- [x] Stop
	- [x] Archive
- [x] Get Executions job
	- [x] Single
	- [x] Many

## Run locally
```sh
docker-compose up --build
```

## Dev environment (optional)
If you don't want to install Node.js locally, you can use the included `dev.sh` script to run your development environment inside a Docker container.
```sh
./dev.sh
```

## Contributing
Contributions are welcome! To contribute to this project, please fork the repository and submit a pull request with your changes. Whether you encounter any issues, have suggestions for improvements, or simply want to participate in enhancing this project, please feel free to [open an issue](https://github.com/Luan7805/n8n-nodes-automation-anywhere/issues) on GitHub.

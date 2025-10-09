![image-banner](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-banner.png)


# n8n-nodes-commander

This is an n8n community node. It lets you use child_process in your n8n workflows so you can execute any command with or without cmd window like silent mode


[Installation](#installation)  
[Compatibility](#compatibility)  
[Usage](#usage)
[Resources](#resources)  
[License](#license)  


## Installation

**For NPM**

To install the node locally, navigate to your n8n installation directory and run the following command:

```
npm install --save n8n-nodes-commander
```

**For Docker**

To install the node using Docker, add the following line to the services block in your docker-compose.yml file:
```

  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    volumes:
      - ./n8n:/root/.n8n
    environment:
      N8N_CUSTOM_NODES: '["n8n-nodes-commander"]'

```
**For n8n UI**

1. Open your n8n instance in a web browser.
2. Click on "Settings" in the left-hand navigation panel.


	![image-0](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-0.png)
3. Click on "Community nodes" in the left-hand navigation panel.

	![image-1](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-1.png)
4. Click on the "Install a community node" button.
	
	![image-2](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-2.png)
5. Fill in the name of the node: "n8n-nodes-commander". and then "Install"
	
	![image-3](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-3.png)


## Credentials

- No credentials required

## Compatibility

- Tested with version 1.94.1

## Usage

1. Open your workflow
2. Open Nodes Panel or press "Tab" then type "Commander" like below

	![image-4](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-4.png)

3. Select or Drag the "Execute Commander" on Canvas area

4. Open Node for Configuration

	- Execution Once : Just Execute Command Once Over All Inputs , otherwise Repeat Execution with Every input item
	- Hidden Window : Just Hide CMD Window for Silent mode (Only Windows OS)

	- Execution Mode : 
  		* Exec : For Simple Output
		* Spawn : For Large Output with continuous Output like logs or monitor stats

	- Command : your command code block like `echo "Welcome To Egypt"`

5. Example

	![image-7](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-7.png)

	![image-5](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-5.png)

	![image-6](https://github.com/MaxBayne/n8n-nodes-commander/blob/master/assets/image-6.png)

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes)
* [n8n-nodes-commander on npmjs](https://www.npmjs.com/package/n8n-nodes-commander)

## License
* This project is licensed under the [MIT License]

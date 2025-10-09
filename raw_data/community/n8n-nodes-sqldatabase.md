# n8n-nodes-sqldatabase 
This is an n8n community node. It lets you use a SQL Database in your n8n workflows.

SQL Database allows you to connect to a database via a JDBC.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  <!-- delete if no auth needed -->  
[Compatibility](#compatibility)  
[Usage](#usage)  <!-- delete if not using this section -->  
[Resources](#resources)  
[Version history](#version-history)  <!-- delete if not using this section -->  

## Installation

### Prerequisites 

The following dependenices must be installed prior to using this node:
* VS Build Tools or VS Community >= v2015 with C++ desktop development workload
* Python3
* Java 8

See [Resources](#resources) for more detail.

### Install
Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

  **_If installing through the n8n GUI fails:_**

  Installing this node through the n8n GUI is throwing an error in my environment currently, node-gyp is unable to find the Visual Studio directory. I will update this section when I find a resolution.

  If you also encounter this issue and would still like to help test or use this node, you may try to install it manually by doing the following:
  #### 1. Stop n8n if it's currently running
  #### 2. Open a new Windows command prompt
  #### 3. Navigate to the .n8n/nodes directory  
    cd [path to .n8n]/.n8n/nodes
  #### 4. Use npm to install n8n-nodes-sqldatabase
    npm i n8n-nodes-sqldatabase
  #### 5. Start n8n

  If successful, you should now see the node available in the editor. If you receive any errors during step 4, review them and confirm that you've properly installed/configured or have encountered an issue that I did not. If the node doesn't appear yet installs properly, check that you've added it to the correct .n8n folder for your desired server.

## Operations

### Statement
#### Execute  
    Execute arbitrary SQL against a specified database. Supports dynamic parameters generated from prior node input.
  

## Credentials

### SQL Database credentials

* Username
* Password
* JDBC connection URL
* Driver Directory


## Compatibility

Tested install and execution with:
* n8n version 1.1.1
* node 18.16.0
* Visual Studio Build Tools 2022
* Python 3.11
* Windows 11 & Windows Server 2022
* JDK & JRE 1.8u381

## Usage

* Configure database credential
* Add node to workflow
* Input SQL
* Execute node

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

### Dependency Information
* [node-java package, requires JDK and built with node-gyp](https://github.com/joeferner/node-java)
* [node-gyp package, requires VS Build Tools/Community and Python](https://github.com/nodejs/node-gyp#on-windows)

### Requirement Downloads
* [VS Build Tools 2022](https://github.com/nodejs/node-gyp#on-windows)
* [VS Community 2022](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community)
* [Oracle Java 8](https://www.oracle.com/java/technologies/downloads/#java8)
* [Python](https://www.python.org/downloads/)


## Version history

_This is another optional section. If your node has multiple versions, include a short description of available versions and what changed, as well as any compatibility impact._



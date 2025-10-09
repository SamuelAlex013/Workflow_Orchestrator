# Table of Contents
- [Table of Contents](#table-of-contents)
- [Overview of Community Short.io n8n Node](#overview-of-community-shortio-n8n-node)
- [If you want a custom node](#if-you-want-a-custom-node)
- [Bugs/Contributing/Feature Request](#bugscontributingfeature-request)
- [Documentation](#documentation)
	- [Installation](#installation)
	- [Credentials](#credentials)
	- [Links](#links)
		- [List Links](#list-links)
		- [Get Link Info](#get-link-info)
		- [Create Link](#create-link)
		- [Update Existing Link](#update-existing-link)
		- [Delete Link](#delete-link)

# Overview of Community Short.io n8n Node
I have no affiliation with short.io beyond being a user.

I created this node for use within my company as well as for our clients. I left out a few features, but I included the options for them so people can see what is possible. Feel free to submit a PR with the updated functionality, or get in touch to discuss us completing it.

# If you want a custom node
Please reach out to me using the info on [my GitHub page](https://github.com/liamdmcgarrigle).  \
Nodes can be built for the community as well as privately just for one organization.

# Bugs/Contributing/Feature Request

If you have a bug to report or a feature request, please [submit a GitHub issue](https://github.com/liamdmcgarrigle/n8n-nodes-shortio/issues/new) with as much detail as you're able to give.

Feel free to submit PRs, but please get in touch with me first to make sure I am willing to add the feature before you spend the time on it.

# Documentation

## Installation

This is now available on cloud as a verified community node. Simply search for shortio in the node panel.

Or follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Credentials

To use this node you will need to set up short.io credentials with a key from short.io. You also will need an account and may need a paid account.

1. Go to https://app.short.io/settings/integrations/api-key and click on "Create API Key"
![Screenshot1](/readme_files/step-1.jpeg)

2. Add a description, pick the domain to use, and press "Create"
![Screenshot2](/readme_files/step-2.jpeg)

3. Copy your new token. It will only be shown once

4. Go to the credential page in n8n, in add credentials add "Short.io API", then paste in your token. Then add the domain you chose in the previous step and press save
![Screenshot3](/readme_files/step-3.png)

## Links

### List Links
Get a list of your short links. These will only be links from the domain in your credential. 

You will need to choose how many results are returned. Anything over 150 is automatically paginationed. 

You can filter the results by adding:
Before date: returns links before the listed date
After date: returns links after the listed date
Date Sort Order: changes the order the links are in based on the date

### Get Link Info
Get link details from the domain in your credential and the path.


### Create Link
Create a link. There are many options. Please see the descriptions I added to n8n's interface.

### Update Existing Link
You can update an existing short link by using the path or the link `idString`. 
You can change anything about the link including the full long URL.

### Delete Link
You can delete an existing short link by using the path or the link `idString`. 

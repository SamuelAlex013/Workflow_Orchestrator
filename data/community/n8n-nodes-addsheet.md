# n8n-nodes-addsheet

This repo contains nodes to add a sheet to a binary file in N8N workflows. The sheets can be added to XLSX based files.

## Using this node

There are 3 basic parameters to add a sheet with data to an existing XLSX Binary file in the workflow.

- **Sheetname** : Name of the sheet you want to add 
- **Data** : A basis JSON List of rows and collumns that is standard to N8N. See below for an example
- **Binary** File : The file you want to add a sheet to.

## Data example
```
   [
   	{
   		"Column 1" : "value 1.1",
   		"Column 2" : "value 1.2",
   		"Column 3" : "value 1.3",
   		"Column 4" : "value 1.4",
   		"Column 5" : "value 1.5",
   		"Column 6" : "value 1.6",
   		"Column 7" : "value 1.7"
   	}
   	{
   		"Column 1" : "value 2.1",
   		"Column 2" : "value 2.2",
   		"Column 3" : "value 2.3",
   		"Column 4" : "value 2.4",
   		"Column 5" : "value 2.5",
   		"Column 6" : "value 2.6",
   		"Column 7" : "value 2.7"
   	}
   ]
```

![Banner image](https://b2sell.com/Admin/Images/Images/netsuite-banner-new.jpg)

# n8n-nodes-nsrestlet

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Credentials](#credentials)  
[Usage](#usage)  
[Compatibility](#compatibility)  
[Resources](#resources)  

## Installation

[Installation instructions for installing/deleting/updating community nodes your n8n instance can be found here.](https://docs.n8n.io/integrations/community-nodes/installation/) Our npm package name is @squaregrove/n8n-nodes-nsrestlet
.

## Credentials

Set up credentials in Netsuite using the following steps

1. [Create an integration record](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1530099787.html)

    * Go to Setup > Integration > Manage Integrations > New.

    * Check the box for Token-Based Authentication.

    IMPORTANT - After you click Save, make sure you take note of the Consumer Key and Consumer Secret. This is the only time you will be able to get those, so if you don't copy them down then a new integration record will need to be created. You will use these later on in n8n.

2. [Create an access token](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/bridgehead_4254081947.html)

    * Go to Setup > Users/Roles > Access Tokens.

    * On the Access Tokens page, click New Access Token.

    * Select the Application Name from the dropdown which will be the same name you chose for your integration record in step 1. Also fill out the User, Role, and adjust the Token Name if you want before clicking Save.

    IMPORTANT - After you click Save, make sure you take note of the Token ID and Token Secret. This is the only time you will be able to get those, so if you don't copy them down then a new access token will need to be generated. You will use these later on in n8n.

3. [Set up a restlet script record](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4618431823.html) 

    * Go to Customization > Scripting > Scripts > New, and then select RESTlet as the script type.
    
    * Enter a name and select the script file. [An example starter script can be found here.](https://github.com/SquareGrove/n8n-nodes-nsrestlet/blob/main/n8n_restlet_sample.js)

    * Copy-paste the script's function names in their respective places depending on the method used to call the function (i.e. - handleGetRequest, handlePostRequest, handlePutRequest, handleDeleteRequest) and click Save.

    * Click Deploy Script. Here you will also need to set the Status to Released, and we recommend setting the Log Level to Debug. Click Save.

    IMPORTANT - Take a note of the External URL that gets generated on the confirmation screen. You will use this later on in n8n.

4. The only other value you will need is your Netsuite Account ID - This will be the number that appears at the beginning of your Netsuite URLs. These are typically 7 digit numbers and can be seen at the beginning of every URL in your environment.

## Usage

1. Create your credentials in n8n by finding the NSRestletCreds credential in the credential manager and inputting the following fields that you noted down from the prerequisites section.

    Consumer Key  
    Consumer Secret  
    Token ID  
    Token Secret  
    NetSuite Account

2. Add the NSRestlet node to your workflow and specify the credentials you set up in the last step, along with the Restlet URL which you should have noted down from step 3 of the prerequisites above.

3. Finally, specify the method that you are using to call your restlet. GET and DELETE will both use Query Parameters to communicate with Netsuite, where the POST and PUT will use the Body. 

Note - Until you build out your restlet more on the Netsuite end, making these calls will just return a success message of "sample response data".

## Compatability

This node has been installed/tested on the most recent production release of n8n at the time of writing n8n@0.228.2. There are no known compatability issues with previous versions.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)

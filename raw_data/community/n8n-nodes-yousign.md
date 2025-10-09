![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-yousign

This is a community node to interact with Yousign API v3.

## Prerequisites

You first need to create an account on [Yousign](https://yousign.app) and create an API Key in the [developer dashboard](https://yousign.app/auth/api/apikeys).

You also need to prepare the document to be signed in PDF with proper anchors to place the signature (or other fields). You can refer to the [documentation](https://developers.yousign.com/docs/signers-fields) for more information or use this [template](https://fields-position.vercel.app/test.pdf).

## Usage

When creating your n8n workflows you need to gather two things before actually using the Yousign node:

- The PDF file in binary format (You can for example use the `Read Binary File` )
- The information about the signer(s) (You can use for instance a form or extract the data from a CSV file)

You can then use the Yousign node.

Parameters:

- Create and/or select credential with your API key
- Select the resource *Signature request*
- Select the operation *Create*
- Enable or disable the *Sandbox* according to your usage

Add one more signers and provider their respective information:

- First name
- Last name
- Email

Finaly select the binary property that contain your PDF to be signed, usually it will be the property `data`.

You can now run the workflow.

## More information

Refer to [ Yousign documentation ](https://developers.yousign.com/)

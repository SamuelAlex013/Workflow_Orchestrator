# n8n-nodes-WritePDFForm

Writes json data into input fields in a PDF Form. Input data should be structured as:  

[  
	  { name: 'FieldName', type: 'text', value: 'Info to display' },  
	  { name: '...', type: 'text', value: '...'},  
		....  
]  

Type can be one of [text, dropdown, radiogroup, checkbox].

PDF Forms can be easily developed with LibreOffice Writer (or your own preferred tool).

There is also a corresponding [readPdfForm](https://github.com/nzidol/n8n-nodes-readpdfform) node that can be to find field names and types of a form.

## License

[MIT](https://github.com/n8n-io/n8n-nodes-starter/blob/master/LICENSE.md)

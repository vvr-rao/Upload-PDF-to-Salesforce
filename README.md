# Upload-PDF-to-Salesforce
Simple code to upload a PDF to Salesforce as an attachment. Can be extended to other file types (tested with .PDF and .txt)
The code creates an Account and attaches a file to it. It  assumes the file is located in the same folder where the code is running.

My initial version used Simple Salesforce but we were leery of downloading it to our server, hence stuck to more 'well known' packages.

Note: The Salesforce REST API requires the body of the attachment to be in Base64. That is the key consideration if you need to modify the code to accept files differently (e.g. read from another application)

Prerquisites:
I created a Connected App in my org.

Tested using Python 3.5.2 on Ubuntu 16

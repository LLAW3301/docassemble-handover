# Handover

This package contains scripts to manage the process of handing over student applications to clients.

At the time I wrote this README, this package does the following:

- It accepts an Excel spreadsheet containing client data, being, first name, last name, email address, name of the application, link to the application as it is installed on the Flinders docassemble server, a flag indicating whether a signed license agreement has been received.
- It prepares a kick-off email to be sent to each client listed in the spreadsheet. The kick-off email will contain a link to another interview in this package which will enable the client to confirm whether they wish to commission the application.
- This second interview is used to record whether a client wishes to commission or not commission, if not commission them whether they wish to continue working with us, if they do wish to commission that instructions for next steps.
- This package contains a word template which will be used as a pro forma application review form, as stated in the formal handover document (which is not part of this package) which is sent to clients
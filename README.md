# Whatsapp-Fixture-Bot

This is a automated Whatsapp Bot made using the Selenium library in python.
The User will recieve a text message of the next 5 fixture of any football team.

The Script access a RESTApi and parses the JSON code to give the information for the teams fixtures

The WhatsBot Scirpt launches an automated Chrome window and logs in with the user credentials by accessing the browser cache(after the first login)
finds the contact in the directory and sends the fixtures as a text message.

The WhatsBot script requires to user to find the Xpath of the given input components in his/her Whatsapp Web interface and input them in the spaces marked 'user inut required'.
Examples of what the Xpath looks like is given in the comments

The chromedriver application is also a nessecity for the running of the bot. 



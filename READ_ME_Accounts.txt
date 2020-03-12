If you run the python file, it needs to be passed the args username (argv[1]) and password (argv[2])
Otherwise, import the python script into new script.
Also, make sure that you have MongoDB running with the Document uploaded and pymongo installed and on $PATH.
"Accounts.json" is the MongoDB document as a JSON.
To import it into your MongoDB:
FROM COMMAND LINE cd'd into the directory that contains the json:
mongoimport --file Accounts.json

TO EXPORT Document:
mongoexport --out NewFileName.json

Currently, the username and pass are both "default" as placeholders.
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

-- UPDATE 3/26/2020:
Added username/password change functionality.

-- UPDATE 4/2/2020:
Added password hashing with SHA256.
MAKE SURE to place hashed value in initial database.
New default username is: default
New default password is: 54036e11410b0c47cb0a62f966c9d879510e8cb29e2628603dd96d67fc6c281d
For database set up and changing.
When using the code, enter unhashed password values.
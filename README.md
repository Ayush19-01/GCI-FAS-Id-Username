# GCI-FASID-USERNAME
_Modules Used: pyhton-fedora connector_
## How it works:
1. The user is asked for his/her Fedora associated username.
2. Using that username a connection is established with the Fedora database.
3. Then the user is asked to enter the username to get the email-id associated with that username.
4. A dictionary is fetched from the fedora database which has a lot of data about the user.
5. A specific key named ['email'] is selected and printed from the user data, which is the required output.
6. User has an option to quit or continue searching usernames.

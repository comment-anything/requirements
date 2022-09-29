
Comment Anywhere has functional requirements for the user.


- Getting Comments

The User must be able to request comments from the Server by clicking the extension icon in their browser. The Server must be able to serve the User comments related to that URL. The Browser Extension must be able to display those comments to the User.

- Registering

The User must be able to register a new account from the user interface in the drop down portion of the browser extension. The Server must be able to validate that the User does not already exist and that their password is of sufficient strength, then either add that User to the Database or tell the User their was a problem with registration.

- Logging In

The User must be able to log into an account from the user interface in the drop down portion of the browser extension. The Server must verify whether the User has supplied the correct credentials. The Server must be able to track whether an HTTP Request is coming from a logged in user.

- Posting Comments

A logged-in User must be able to post a new comment. The Server must be able to add that Comment to the comment data for the URL the User is commenting on, if the user is permitted to comment on that page.

- Reporting

A logged-in User must be able to report a rule-breaking comment. The Server must be able to track which comments require moderation action.

- Moderating

A Domain Moderator or Global Moderator must be able to view all comments that have been flagged by Users as rule breaking. They must be able to remove rule breaking comments or clear flags if no action is required. 

- Banning

....



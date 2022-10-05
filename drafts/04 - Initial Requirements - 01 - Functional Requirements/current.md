
Comment Anywhere has a number of functional requirements necessary to meet our objective.

- Getting Comments

A Viewer must be able to request comments from the Server by clicking the extension icon in their browser. The Server must be able to serve the User comments related to that URL. The Browser Extension must be able to display those comments to the User.

Logged In Users may also receive comments that are hidden by default to non-logged in Viewers. 

- Registering

A Viewer must be able to register a new account from the user interface in the drop down portion of the browser extension. The Server must be able to validate that the User does not already exist and that their password is of sufficient strength, then either add that User to the Database or tell the User their was a problem with registration.

- Logging In

The User must be able to log into an account from the user interface in the drop down portion of the browser extension. The Server must verify whether the User has supplied the correct credentials. The Server must be able to track whether an HTTP Request is coming from a logged in user.

- Settings

The User must be able to change their settings locally to control whether they want to view potentially problematic, hidden, comments. They must be able to reset their password from their settings page. 

- Posting Comments

A logged-in User must be able to post a new comment. The Server must be able to add that Comment to the comment data for the URL the User is commenting on, if the user is permitted to comment on that page.

- Validating Comments and Usernames

The Server must automatically evaluate Comments and Usernames to determine if they may contain words or phrases which violate our policies. They must prevent and remove comments that certainly violate the policies and flag and hide comments that may do so. It must prohibit the registration of usernames that contain prohibited words.

- Reporting

A logged-in User must be able to report a rule-breaking comment. The Server must be able to track which comments require moderation action. A logged-in User must also be able to report buggy pages.

- Moderating

A Domain Moderator or Global Moderator must be able to view comments that have been flagged by Users as rule breaking. They must be able to remove rule breaking comments, take other actions, or clear flags if no action is required. 

- Assigning Moderators

A Global Moderator must be able to elevate a User to the status of Domain Moderator. An Admin must be able to assign Global Moderators. Similarily, an Admin must be able to remove Global Moderator permissions and Admins and Global Moderators must be able to remove Domain Moderator Permissions. The Server must be able to accurately evaluate permissions and allow or disallow actions based on those permissions.

- Banning

Domain Moderators must be able to ban troublesome Users from their domain. The Server must not allow banned Users to post on that domain. Global Moderators must be able to ban Users globally or from a specific domain. Users must be able to appeal Bans and Admins must be able to review banning actions taken by Moderators. 

- Reports

Admins must be able to view reports on User Activity, Moderation Actions, and other metrics. 

- Static Website

There must be a website that provides a description of the project, download links for the Browser Extension, and instructions for installing and using the Browser Extension, which anyone on the internet can view.
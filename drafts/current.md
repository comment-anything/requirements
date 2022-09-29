
# Header


## Title Page

Comment anything requirements Document.
## Instructor Comments and Evaluation


## Table of Contents


## Abstract


We describe the results of Software Requirement Engineering in a Waterfall model as applied to our proposed Software Product, Comment Anywhere. In this document, the requirements of the product are developed. We begin by addressing the background, objective, and team details. We then explore the Application Domain, Operating Requirements, and describe Data Sources and Use Cases. Finally, we explicate the functional and nonfunctional requirements of Comment Anywhere. 
# Introduction


## Background


Internet denizens have long found ways to have vibrant communications about a wide variety of content. In the past, more website supported these conversations through comment sections, but many have closed their comments in recent years. Instead, the avenues of discourse have become social media sites such as Facebook, Reddit, and bulletin board style forums, decoupling the conversation from the content itself.

Tying comments to social media posts rather than the content has the effect of fragmenting the conversation and diluting information available to viewers. Evidence exists that users spend less time on webpages without comments and report a worse user experience.  [2] We infer that there is a market for comments tied to content rather than posts and an application that can bring comments to the content could capture monetizable user engagement.

## Objective


## Team Details & Dynamics

Communication, Organization, and Commitment are the tools we need to complete this project.

Discussions will be conducted in the project's Discord server. Additionally, Discord Webhooks will provide notifications whenever work is done on the source code.

Effective organization will be achieved using prevailing software management tools. Git can track versions and handle changes merged from multiple branches. GitHub provides access to a strong Issue system which we will use to communicate about project needs. 

Each group member has committed to being team leader for a phase of the project. That team leader will create the repository on our GitHub Organization's GitHub page and will communicate with the group to encourage all members to contribute to the project.



# Application Domain

The application domain of Comment Anywhere is internet communication services. More specifically, the domain is internet users commenting and viewing comments about web pages.  [3] 
# Initial Business Model


## Operating Environment

The Front End will run in the browser engines of Chrome, Firefox, and other browsers that may support Chromium or Firefox based extensions. The Back End will be configured to run at least two Virtual Machines to allow for simple deployment on a variety of cloud options. The Database and HTTP Server will run on separate Virtual Machines. 
## Description of Data Sources

We will be getting many parts of our data from many different sources, first we will grab the url that the user is currently on and request the data for that webpages comment section. We will then see that request and grab the comment section from our database and display them to the user. When the user is ready, we will have the user log in to the extention. After the user enters their information into the extention we will verify if the user is actually the user as with all logins. There should be a few options for the user at this point the user can choose to either make a comment or reply to another comment, in the moderator's case they will also be able to report comments. If the user comments or reply's when the commenter posts their message to the database for the website url. If a moderator reports a comment the comment will move from the comments database to a removed comments database that only the moderators are able to see. The administrators as well as being able to do everything users and moderators can do is approve and select both global and regular moderators, they can also request and see who has approved the moderators and when for both global and local moderators. Global moderators are also able to request and see local moderators approval and time. Users can also be banned by moderators, regular moderators cana only ban users to the domain of the site they moderate while global and administrators can issue domain and full bans from all sites. When a user is banned their name is put into the domain bans database as well as where they were banned from who banned them and when.
## Use Case Diagrams


# Initial Requirements


## Functional Requirements


## NonFunctional Requirements


## Documentation


Many types of documentation will be created throughout the project's lifestyle in order to produce a highly maintenable and extensible product that can adapt and scale after release. The target of the documentation is current and future developers. End users will require little documentation to interact with the product. Documentation for the developers will consist documentation generated from code comments and some additional hand written files. 

Some of the documentation files that will be created include: 

- A document entitled Testing.md will describe a standardized way to write and categorize unit tests and provide instructions for running and writing them.

- A document entited Versioning.md will describe the use of `git`.

- A document entitled Documenting.md will describe code-commenting practices. It will describe the procedure for generating project documentation from comments and adding additional non-generated documentation to that.

- A document entitled Glossary.md wil comprise a list of all nonstandard words used. It will be divided into application domain terms and terms specific to this project. It will also have a section describing the contents of each source code folder and a section describing the purpose of each file in root.

- A document entitled Build.md will provide instructions for building and running the project.

- A document entitled Database.md will describe database migrations.

- We will maintain 95% coverage with unit tests of source code we write.

- The writing center will review this project report.



# Testing Revisions


# Appendix


## Technical Glossary



**Administrator**

The highest authority of moderation can do anything a global moderator can do and see their approval to global moderator

**Application Domain**

The specific environment in which the product is to operate.  [3] Can be an organization, a department within an organization, or a single workspace.  [4] 

**Back End **

A Back End is any part of a website or software program the users do not see. It contrasts with the Front End, which refers to a program or website's user interface.

**Cloud**

"The cloud" refers to servers that are accessed over the Internet, and the software and databases that run on those servers. Cloud servers are located in data centers all over the world. By using cloud computing, users and companies do not have to manage physical servers themselves or run software applications on their own machines.  [9] 

**Comment**

A line of text created by any user can be replied to by other comments ,edited for a spacific duration reported and become a removed comment

**Database**

A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and querying data.  [8] 

**Discord**



**Discord Webhooks**



**Front End**

The Front End of a software program is everything with which the user interacts. From a user standpoint, Front End is synonymous with the User Interface. The Front End of Comment Anywhere is the Browser Extension.  [11] 

**Git**



**GitHub**



**GitHub Organization**



**Global Moderator**

Higher authority than a moderator can ban people from any domain or all domains can also see when a regular moderator was premoted and by who

**Nonfunctional Requirement**

Properties of the product such as platform constraints, response times, or reliability.  [12] 

**Requirements Engineering**

The process of defining, documenting, and maintaining requirements in the engineering design process.  [1] 

**Server**

A program which waits for a request then performs some service for the requester and which runs on a computer other than the one on which the requestor/client runs.  [7] The Server used by Comment anywhere is an HTTP server because it processes HTTP requests on the Internet. 

**User**

Anyone that has the browser extention installed on a browser, low level access to the program only able to comment, reply to comments and be premoted to a moderator global moderator or admin or banned by moderators and administrators either entirely or on a spacific domain.

**User Interface**

Also called a "UI" or "interface", a User Interface is the means in which a person controls a software application or hardware device.  [10] 

**Virtual Machine**

Also called a Container, a Virtual Machine is a compute resource that uses software instead of a physical computer to run programs and deploy apps. One or more virtual "guest" machines run on a physical "host" machine. Each virtual machine runs its own operating system and functions separately from the other VMs, even when they are all running on the same host.  [5] 
## Team Details


## Workflow Authentication


## Report from Writing Center


# References



 [1] - https://www.javatpoint.com/software-engineering-requirement-engineering

 [2] - https://www.poynter.org/ethics-trust/2021/dont-read-the-comments-for-news-sites-it-might-be-worth-the-effort/

 [3] - Schach, Stephen R., Object-Oriented and Classical Software Engineering, 8th edition.

 [4] - Züllighoven, Heinz, Object-Oriented Construction Handbook, Chapter 6.3, 2005. https://www.sciencedirect.com/topics/computer-science/application-domain

 [5] - https://www.vmware.com/topics/glossary/content/virtual-machine.html

 [6] - https://techterms.com/definition/backend

 [7] - http://www.catb.org/jargon/html/S/server.html

 [8] - https://www.oracle.com/database/what-is-database/

 [9] - https://www.cloudflare.com/learning/cloud/what-is-the-cloud/

 [10] - https://techterms.com/definition/frontend 

 [11] - https://techterms.com/definition/user_interface

 [12] - Schach, Stephen R., Object-Oriented and Classical Software Engineering, 8th edition.
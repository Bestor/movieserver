# Backend Software Development Exercise
## Objective
Build an API service with a database backend for storing and editing a movie collection. Please
use a technology stack of your choosing to deliver the application, though use of AWS
infrastructure is recommended.

1. Start by briefly documenting the technology stack of your choosing. Let us know what
component you’ve chosen for each layer and why.

2. Setup a source code repository where we can watch your progress. GitHub or Bitbucket
are fine.

3. You’ll need to deploy your application to a hosting service of your choosing (AWS,
DigitalOcean, Azure, etc). Free tiers should be sufficient.

## Requirements

1. The service must be accessible over http using a command line interface (curl, node,
etc.); a GUI is not necessary.

2. Add an authentication method to restrict access to the repository. Only users that need
access to the service should be able to access it.

3. The service must create, read, update, delete, and list movies in the collection.

4. Each movie in the collection needs the following attributes:
	a. Title [text; length between 1 and 50 characters]
	b. Format [text; allowable values “VHS”, “DVD”, “Streaming”]
	c. Length [time; value between 0 and 500 minutes]
	d. Release Year [integer; value between 1800 and 2100]
	e. Rating [integer; value between 1 and 5]

5. On the collection list request, the items in the list must be sortable by movie attributes.

6. Integrate a third-party web service relevant to the project.

## Extra Credit (none, any, or all)
1. Implement a build tool of your choosing (CloudFormation in AWS, etc)
2. Integrate a testing suite of some sort

## Keep In Mind
1. We want to see your progress, not just a finished product. Email us your source code
repository and a link to your application instance as soon as you have them setup.
2. Stay in communication with us (ask questions, give status updates). This is part of the
challenge.

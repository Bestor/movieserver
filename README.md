This repository is going to be used to write an movie server with only an API (no gui) that will be used to maintain a movie collection.

The application will be able to read, write edit, delete, and list movies.

Although it is not necessary for this project I will plan on making an initial commit to master and then after that I will be working on a dev branch and merging code to master via pull requests from my dev branch. This is mostly to demonstrate that I can use a normal team git workflow.

# Results

I did not complete the following things:

- There is no UPDATE or DELETE methods
- There is no sorting functionality
- There is no authentication

All the other requirements were met. I had issues with the docker-compose file for quite some time because I couldn't get the services to link over the internal docker network. I worked around it by just mounting the appropriate ports to the host and going through the host networking. 

In hindsight, I wish I had spent less time on the docker-compose file and more time meeting the requirements and automating deployment to AWS. Overall I am happy with the progress I made though. The django-rest-framework was definitely the right tool and made creating the API itself very easy. The GUI it provided was extremely useful for testing so I didn't have to access everything via GET requests with curl.

Using AWS was a good experience as well. I initially tried to use AWS Fargate but I found that I could get my containers hosted but I was having issues getting them to link so in the interest of time I spun up an EC2 container and deployed the containers into it. This was very easy and smooth.

# Plan of attack

- I will create the application using django. I chose it for three reasons. 
1) One of the stipulations is that the program use a database and django easily integrates with many different DB backends
2) django already has established ways to interact with it via api calls so I won't have to reinvent the wheel
3) familiarity

- I plan to use two containers. One using the django application, one running whatever database I choose (probably postgres because I'm familiar with it). This seeams like a logical seperation of the services here, one to handle the data, and one to handle the API calls and logic.

- Once I have created the two containers above I will attempt to deploy it to AWS. This will take some investigation as I have not used AWS before. If this ends up taking me too long I will probably fall back to deploying it via ansible since that is what I am familiar with.

- If I have time after all this I'll attempt to integrate a test suite and some kind of script that can automatically build/deploy the service.

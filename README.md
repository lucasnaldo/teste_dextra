# PROJETO DEXTRA DIGITAL

## Como Exeutar

Clonar o repositório

docker build --tag dextra_app

docker run --name python-app -p 5000:5000 my-python-app

Besides calcutate the internal rate of investment you want to compare wheter this investment is better than a Selic rate.

# You have to:
Understand the CSV file and how its is relateded with the concepts of internal rate of investiment in irregular cash flow;

# Proposed exercise
Create an Python application that performance the following tasks:

- Read an CSV file with the assets;

- Calculate the IRR(You must create your own algorithm (don't use any python mathematical function for that) we want to test your logical thinking here

- Consume a public web service that return the Selic rate of the day;

- Show the IRR calculated and the Selic rate in console;

- Store the information of the CSV file, the calculated IRR and Selic rate in a in memory database - Feel free to use structure or framework you like.

- Create a Docker image with the application ready to use;

# Unit tests
- Create unit tests with 50% code coverage



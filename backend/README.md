# All My Pets API

This service provides an API to interact with and manage all of my pets 🐱

## Setup

### Prerequisites for local development

- [python3.11](https://www.python.org/downloads/)
- [python virtualenv](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
- [docker CLI](https://docs.docker.com/engine/reference/commandline/cli/)


### Setting up the local development environment

1. Set up python virtual environment

   > cd backend
     python3.11 -m venv env

2. Activate the virtual environment
   > source env/bin/activate

   You will notice that your terminal path includes (env), signifying an activated virtual environment.
   

3. Install dependencies
   > pip install -r requirements.txt


## Run

### Local execution

   > cd backend
     python src/main.py

### With Docker

1. Build the Docker image
   > docker build -t all-my-pets . 

2. Run container
   > docker run -p 8000:8000 all-my-pets



## Working with the API

### OpenApi Spec

You can access the generated openapi file in the browser to test requests against the running API.

Run the app and head to 
`http://localhost:8000/api/docs`



## Follow-up actions

### Further development

- [ ] This current Flask service is only meant for development. Use a production-ready WSGI Server like Gunicorn or uWSGI.
- [ ] Write unit tests
- [ ] Set up database persistence layer
- [ ] Automate creation of openapi spec

### Security 

- [ ] Use HTTPS to encrypt data between client and server
- [ ] Implement authentication & RBAC (JWT)
- [ ] Keep dependencies up to date (github dependabot)

### Deployment

- [ ] Build CI/CD pipeline with Github Actions to: 
      - Build application
      - Run static code analysis (ex: dependency checks)
      - Run unit tests
      - Build and push image to image repo (ex: AWS ECR)
      - Deploy image to AWS (ECS, EKS)
- [ ] Set up logging and monitoring - ex: ELK stack (Elasticsearch, Logstash, Kibana), Prometheus, and Grafana
- [ ] Orchestration with Kubernetes for scalability and management
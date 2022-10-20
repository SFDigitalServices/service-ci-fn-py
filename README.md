# service-ci-fn-py [![CircleCI](https://badgen.net/circleci/github/SFDigitalServices/service-ci-fn-py/main)](https://circleci.com/gh/SFDigitalServices/service-ci-fn-py) [![Coverage Status](https://coveralls.io/repos/github/SFDigitalServices/service-ci-fn-py/badge.svg?branch=main)](https://coveralls.io/github/SFDigitalServices/service-ci-fn-py?branch=main)
Service CI Azure serverless python function microservice  
Lightweight configuration file-based workflow system to enable continuous integration for services interacting various APIs and Webhooks. 

## `api/status/http`
Query http status of the serverless function.

### Query
Example
```
$ curl https://<host>/api/status/http

{"status": "success", "data": {"message": "200 OK"}}
```

## `api/run/jobs`
#### Query Parameters ####
`project`: name of project configuration  
`job`: name of job   
`step`: job step to start  
`limit`: limit the number of steps to run

### Query
Example
```
$ curl https://<host>/api/run/jobs?project=sample_proj_config&job=job1&step=1&limit=1

{"status": "success", "data": {...}}
```

## MODS
This microservice run of concept of leveraging individual modules ([`mods`](./mods)) to interact with various external systems. A mod to used in a `step` within a `job`. A simple one step job that uses version 1 of the email mod to send email looks like this:
```
jobs:
  job1:
    steps:
        - uses: email/send@v1
```
### List of MODs available
* `airtable@v1`: Connects to [Airtable](https://airtable.com/)
    * `get`: gets an Airtable record
    * `insert`: insert an record into Airtable base
* `email@v1`: Connects to [Email microservice](https://github.com/SFDigitalServices/email-microservice-py)
    * `send`: send an email
* `formio@v1`: Connects to [Form.io](https://www.form.io/)
    * `submission-get`: get a form submission
* `jsonata@v1`: Connects to [JSONata microservice](https://github.com/SFDigitalServices/jsonata-fn-js)
    * `eval`: evaluates JSONata query [[try](http://try.jsonata.org/)]
* `pts@v1`: Connects to [Permit Tracking System (PTS) microservice](https://github.com/SFDigitalServices/pts-microservice-fn-py)
    * `permit-create`: creates a building permit application

## Deployment notes
#### :warning: [Linux Consumption] Successful slot swaps automatically reverted after a few minutes :warning:
DO NOT USE "SWAP" option until [issue](https://github.com/Azure/azure-functions-host/issues/7336) is resolved.   
see more at: https://github.com/Azure/azure-functions-host/issues/7336


## Development

### Get started

Install Pipenv (if needed)
> $ pip install --user pipenv

Install included packages
> $ pipenv install

Output virtualenv information
> $ pipenv --venv






### Quickstart Reference Guide
[Create a function in Azure with Python using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python)  
[Create a Python function in Azure from the command line](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python)

### Environment variables
[Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#environment-variables)
In Functions, `application settings`, such as service connection strings, are exposed as environment variables during execution. You can access these settings by declaring `import os` and then using, `setting = os.environ["setting-name"]`. See example of `local.settings.json` file at `local.settings.example.json`.

### Generating requirements.txt
Currently Azure Python Functions [does not support pipenv](https://github.com/Azure/azure-functions-python-worker/issues/417). However we can run `pipenv lock --requirements` to produce a requirements file for the non-dev requirements and `pipenv lock --requirements --dev` to produce one for just the dev requirements.
sample usage:  
production
```
$ pipenv lock --requirements > requirements.txt
```
development
```
pipenv lock --requirements --dev > requirements-dev.txt
```

#### azure-functions-worker
DO NOT include azure-functions-worker in requirements.txt
The Python Worker is managed by Azure Functions platform
Manually managing azure-functions-worker may cause unexpected issues

### Testing and Code Coverage
Code coverage command with missing statement line numbers  
> $ pipenv run python -m pytest --cov --cov-report term-missing

### Prec-commit
Set up git hook scripts with pre-commit
> $ pipenv run pre-commit install

### Continuous integration
* Setup `.env`
    1. Setup environmental variables from `local.settings.json`
* Setup coveralls.
    1. Log into coveralls.io to obtain the coverall token for your repo.
    2. Create an environment variable in CircleCI with the name `COVERALLS_REPO_TOKEN` and the coverall token value.

## How to fork in own repo (SFDigitalServices use only)
reference: [How to fork your own repo in Github](http://kroltech.com/2014/01/01/quick-tip-how-to-fork-your-own-repo-in-github/)

### Create a new blank repo
First, create a new blank repo that you want to ultimately be a fork of your existing repo. We will call this new repo "my-awesome-microservice-py".

### Clone that new repo on your local machine
Next, make a clone of that new blank repo on your machine:
> $ git clone https://github.com/SFDigitalServices/my-awesome-microservice-fn-py.git

### Add an upstream remote to your original repo
While this technically isn’t forking, its basically the same thing. What you want to do is add a remote upstream to this new empty repo that points to your original repo you want to fork:
> $ git remote add upstream https://github.com/SFDigitalServices/microservice-fn-py.git

### Pull down a copy of the original repo to your new repo
The last step is to pull down a complete copy of the original repo:
> $ git fetch upstream

> $ git merge upstream/main

Or, an easier way:
> $ git pull upstream main

Now, you can work on your new repo to your hearts content. If any changes are made to the original repo, simply execute a `git pull upstream main` and your new repo will receive the updates that were made to the original!

Psst: Don't forget to upload the fresh copy of your new repo back up to git:

> $ git push origin main



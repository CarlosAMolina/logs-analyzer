## Table of contents

- [Introduction](#introduction)
- [Configuration](#configuration)
  - [VirusTotal credentials](#virustotal-credentials)
  - [External libraries](#external-libraries)
    - [Bash requirements](#bash-requirements)
    - [Python requirements](#python-requirements)
    - [Angular requirements](#angular-requirements)
  - [Database](#database)
    - [Create the database](#create-the-database)
- [How it works](#how-it-works)
  - [Work with Bash scripts](#work-with-bash-scripts)
    - [Analyze an IP with VT](#analyze-an-ip-with-vt)
  - [Work with the user interface](#work-with-the-user-interface)
    - [Run the API](#run-the-api)
    - [Run the Frontend](#run-the-frontend)
- [Tests](#tests)
  - [Test Python code](#test-python-code)

## Introduction

Project that facilitates logs analysis with an user interface.

The main program runs on Python. There are some Bash scripts but they are not required, you can use them to analyze a log file manually.

## Configuration

### VirusTotal credentials

Configure the [Virus Total credentials](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key):

```bash
vi ~/.bashrc
# Example. Add to the end of the file:
# export VT_KEY="foo"
source ~/.bashrc
```

### External libraries

External software must be installed.

The Python code does not need the Bash scripts, you can work with Python without installing the Bash requirements.

#### Bash requirements

Some Bash scripts require `jq`:

```bash
sudo apt-get install jq
```

#### Python requirements

Create a virtual environment, activate it and install the `requirements.txt` file.

#### Angular requirements

Install the Angular requirements:

```bash
cd src/frontend/
npm install
```

### Database

### Database credentials

Configure the database credentials:

```bash
vi ~/.bashrc
# Example. Add to the end of the file:
# export DB_USERNAME="foo"
# export DB_PASSWORD="bar"
source ~/.bashrc
```

#### Create the database

##### Create the database manually

You can find the database DDL at:

```bash
less configuration/database/logs_analyzer.ddl
```

##### Create the database with SQLAlchemy

The Python requirements must be installed.

Change working directory:

```bash
cd src/api
```

Initialize the database:

```bash
flask db init
```

Create database and tables:

```bash
flask db migrate
flask db upgrade
```

## How it works

There are some Bash scripts to analyze a log file, the main project that provides the user interface runs on Python and does not need the Bash scripts.

To work with the user interface, you must run:

- API
- Frontend

### Work with Bash scripts

See the scripts in the `src/bash_scripts` folder.

Run each script with the required arguments.

#### Analyze an IP with VT

Example:

```bash
./src/bash_scripts/get-analysis-of-ip 8.8.8.8
```

### Work with the user interface

#### Run the API

```bash
python src/api/app.py
```

#### Run the Frontend

```bash
cd src/frontend/
ng serve --port 4200 --open
```

Open the following link:

<http://127.0.0.1:4200>

## Tests

### Test Python code

With the virtualenv activated, run the following command:

```bash
tox
```

## Table of contents

- [Introduction](#introduction)
- [Configuration](#configuration)
  - [VirusTotal credentials](#virustotal-credentials)
  - [External libraries](#external-libraries)
    - [Bash requirements](#bash-requirements)
    - [Python requirements](#python-requirements)
- [How it works](#how-it-works)
  - [Work with Bash scripts](#work-with-bash-scripts)
    - [Analyze an IP with VT](#analyze-an-ip-with-vt)
  - [Work with Python](#work-with-python)
- [Tests](#tests)
  - [Test Python code](#test-python-code)

## Introduction

Project to facilitate the analysis of logs.

The main program works with Python but you have some Bash scripts too.

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

## How it works

### Work with Bash scripts

See the scripts in the `src/bash_scripts` folder.

Run each script with the required arguments.

#### Analyze an IP with VT

Example:

```bash
./src/bash_scripts/get-analysis-of-ip 8.8.8.8
```

### Work with Python

Run the app:

```bash
python -m src
```

Open the following link:

<http://127.0.0.1:5000/logs>

## Tests

### Test Python code

```bash
tox
```

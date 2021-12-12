## Table of contents

- [Introduction](#introduction)
- [Configuration](#configuration)
  - [VirusTotal credentials](#virustotal-credentials)
- [How this works](#how-this-works)
  - [Bash](#bash)
  - [Python](#python)

## Introduction

Project to facilitate the analysis of logs.

## Configuration

### VirusTotal credentials

Configure the [Virus Total credentials](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key):

```bash
vi ~/.bashrc
# Example. Add to the end of the file:
# export VT_KEY="foo"
source ~/.bashrc
```

## How this works

The main program works with Python but you have some bash scripts too.

### Bash

See the scripts in the `src_bash` folder.

Run each script with the required arguments.

#### Analyze an IP with VT

Install `jq`:

```bash
sudo apt-get install jq
```

Example:

```bash
./src_bash/get-analysis-of-ip 8.8.8.8
```

### Python

Create a virtual environment and install the `requirements.txt` file.

Run the app:

```bash
python -m src_python
```

Open the following link:

<http://127.0.0.1:5000/logs>


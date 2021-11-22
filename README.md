## Table of contents

- [Introduction](#introduction)
- [Configuracion](#configuracion)
  - [Analyze an IP](#analyze-an-ip)
- [Run](#run)

## Introduction

Project to facilitate the analysis of logs.

## Configuracion

### Analyze an IP

Configure the [Virus Total credentials](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key):

```bash
vi ~/.bashrc
# Example. Add to the end of the file:
# export VT_KEY="foo"
source ~/.bashrc
```

Install `jq`:

```bash
sudo apt-get install jq
```

## Run

Run each script with the required arguments. Example:

```bash
./get-analysis-of-ip 8.8.8.8
```

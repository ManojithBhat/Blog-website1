# Blog-website1
## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Cloning the Repository](#cloning-the-repository)
  - [Setting up the Virtual Environment](#setting-up-the-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
  - [Configuring Environment Variables](#configuring-environment-variables)
  - [Initializing the Database](#initializing-the-database)
- [Running the Application](#running-the-application)

## Overview

Brief description of your project.

## Getting Started

### Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ManojithBhat/Blog-website1.git
cd Blog-website1
```
## Setting up the Virtual Environment

### Create a virtual environment:

```bash
python -m venv venv
```

## Activate the Virtual Environment:

### On Windows:
```bash
source venv\Scripts\activate
```

### On Unix or MacOS:
```bash
source venv/bin/activate
```

## Install Required Modules:

```bash
pip install -r requirements.txt
```

## To add any dependencies for future development just do this:

```bash
pip install <MODULE_NAME>
pip freeze > requirements.txt
```

## Configure Environment Variables:

### Open the .env file and set the values for:

-SQLALCHEMY_DATABASE_URI
-SECRET_KEY

## Initialize the Database in CLI:
### make required changes in the app.py file for app.config\['SQLALCHEMY_DATABASE_URI'] for mysql,sqlite or Postgres sql.

```bash
python3
```
```bash
from app import app
app.app_context().push()
db.create_all()
```

## Run the Flask App Locally:

```bash
flask --run
```

### you can also use app in the debug mode 

- for linux

```bash
set FLASK_ENV=development
set FLASK_APP=app.py
flask run --debug
```

- for windows
```bash
set FLASK_ENV=development
export FLASK_APP=app.py
flask run --debug
```


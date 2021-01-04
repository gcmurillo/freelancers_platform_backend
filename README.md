# WorkClick Freelancer Platform

## Description
The propose of this project is to manage platform data thought API REST services. 

## How to setup
1. Create Python3 venv
``` bash
$ python3 -m venv .venv
```

2. Activate Venv
``` bash
$ source .venv/bin/activate
```

3. Install requeriments
``` bash
$ pip install -r requeriments.txt
```

4. Migrate models
``` bash
$ python manage.py makemigration
$ python manage.py migrate
```
## IMPORTANT!
- Use [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) to manage branches.
- All the PRs should have a review to be completed.

![GitHub last commit](https://img.shields.io/github/last-commit/matracks/webpersonal?color=blue)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/matracks/webpersonal?color=purple)

# Personal Web

## Requirements
Python and pipenv as Virtual environment

## Getting started
If you don't have pipenv, install with this, else go to step 1.
```bash
pip install pipenv
```
1. Clone the repository
```bash
git clone https://github.com/matracks/webpersonal.git
```
2. Open the root of the project in your terminal
```bash
cd webpersonal
```
3. Created a Virtual environment with packages
```bash
pipenv install -r requirements.txt
```
```bash
pipenv shell
```
3. Need [generate a new one](https://djecrety.ir/) SECRET KEY and copy in 'secret_key.txt'

4. Then make the migrations for DB
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
5. Create Admin user
```bash
python manage.py createsuperuser
```
6. Runserver
```bash
python manage.py runserver
```
7. Now [open your browser](http://127.0.0.1:8000/)
5. Easy and enjoy 🍻

## Architecture
- Server - Client

## Runs on
- Linux
- MacOS
- Windows

## Useful Links
[Django](https://docs.djangoproject.com/en/4.1/)

[Pipenv](https://pipenv.pypa.io/en/latest/)

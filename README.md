# vue-catalogue
> Demo of a product catalogue built with Vue 3 and Django
---

## *Backend*

### Required

- Python 3
- PIP
- venv

### Installation & Usage

``` bash
# create virtual environment
python -m venv env

# activate virtual environment
source env/bin/activate # (Linux)
source env/Scripts/activate # (Windows)

# install dependencies
pip install -r requirements.txt

# migrate database
python manage.py migrate

# run server at http://127.0.0.1:8000
python manage.py runserver
```
---

## *Frontend*

### Required
- Node.js >=12.0.0

### Installation & Usage

``` bash
# change to frontend directory 
cd frontend

# install dependencies
npm install

# serve with hot reload at http://localhost:3000
npm run dev
```
---

## *Note*

### Login
- Admin
```
username: admin
password: admin
```

- Normal user
```
username: user
password: catalogue123
```

<sup>* Credentials can be modified at migrations or using [django-admin](https://docs.djangoproject.com/en/1.8/intro/tutorial02/).</sup>
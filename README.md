# vue-catalogue
---

## *Backend*

### Required

- Python 3
- PIP
- venv

### Installation

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

### Installation

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
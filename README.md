# task_manager

## Things You Need Before Starting a Django Project

1. You will need the latest Python version.
2. Must have pip installed.
3. Virtual Environment.
4. Django.
5. PyMySQL.
6. XAMPP.
7. Git must be installed.
8. A GitHub account.

## Steps on Setting Up

### Step 1: Create a folder where you want to start your project.
### Step 2: Open the folder in VS Code.
### Step 3: Open Terminal and install Django:
```sh
pipenv install django
```
### Step 4: Install PyMySQL:
```sh
pipenv install pymysql
```
### Step 5: Activate the virtual environment:
```sh
pipenv shell
```
### Step 6: Start a new Django project:
```sh
django-admin startproject task_manager
```
### Step 7: Start a new Django app:
```sh
python manage.py startapp tasks
```

## Next Steps in Creating the Project

### Step 1: Create templates in the project-level folder.
### Step 2: Create URLs.

## Setting Up from GitHub

### Step 1: Clone the Repository
```sh
git clone <repository_url>
cd task_manager
```
### Step 2: Create and Activate a Virtual Environment
```sh
pipenv shell
```
### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```
### Step 4: Apply Migrations
```sh
python manage.py migrate
```
### Step 5: Run the Development Server
```sh
python manage.py runserver
```

## Note

- When creating models, you must first go to `settings.py`, locate the `INSTALLED_APPS` section, and add the name of your app. For example:
  ```python
  INSTALLED_APPS = [
      ...
      'tasks',
  ]
  ```
- SANTOS EMMANUELLE D. BSCS 2C

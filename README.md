# Qatros Backend Internship Challenge
### Made in Django, Included inside is :
### Project 1 (Master Item)
An API to manage an master item
### Project 2 (Bus Scheduling System)
An API to manage and monitoring Bus Schedule

### Link for the Project
To access the project visit this [link](http://qatros-challenge.herokuapp.com/).\

## How to use
### 1.Ensure Python 3 is included in your system and PATH:
Python instalation can be seen on this [Python](https://realpython.com/installing-python/).\
Git instalation can be seen on this [Git-CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).\

### 2.Make a virtual enviroment for the project:
Make a folder for the project, lets name it "Example Folder", on your run terminal run the following commands
```
python -m virtualenv venvname
```
Make sure you has virtualenv on your package, install using `pip install virtualenv`<br/>

After installing your virtual enviroment, activate it by using
```
venvname\Scripts\activate
```
Further explanation about virtual enviroment can be seen on this [link](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/).\


### 2.Clone the repository to your folder project:
After activating your virtual enviroment, using your Terminal or Git-CLI, run the following code to clone the project

```
git clone https://github.com/nicorenaldo/qatros-challenge.git
```

### 3.Install the requirements package for the project
Open the Django folder using your terminal and run this line of code on your terminal

```
pip install -r requirements.txt
```

### 4.Sync the database of the project
Sync the database of the project by running

```
python manage.py migrate
```

### 5.Run the project
You can run the server by running
```
python manage.py runserver 0.0.0.0:8000
```
You can see the project on your browser by the URL address written on the terminal after running the code

### DONE

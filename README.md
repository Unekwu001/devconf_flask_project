# devconf_flask_project
This project helps developers register online to attend developer conferences. The application is powered by python flask on the server-side.
Collaborated with cohort22 of moat academy on this project.

Steps TAKEN IN SETTING UP THE PROJECT

1. CREATED A FOLDER CALLLED DEVCONF
2. CD INTO DEVCONF
3. CREATED A VIRTUAL ENVIRONMENT USING THE COMMAND "python3 -m venv vdevconf".note that the name of the virtual environment could be anything.
4. ACTIVATED THE VIRTUAL ENVIRONMENT USING THE COMMAND "source vdevconf/bin/activate"
5. INSTALLED flask using "pip3 install flask"
6. INSTALLED mysql.connector class using "pip3 install mysql-connector"
7. INSTALLED SQLALCHEMY using "pip3 install sql_alchemy"
8. CREATED AN INSTANCE FOLDER WITH A config.py file within, CREATED A starter.py file inside devconf,CREATED pkg folder with contents as follows: 1. a myroutes folder, 2. an __init__.py file, 3. a static folder for static files, 4. a templates folder for html files, 5. a mymodels.py file.
9. nEXT ON THE PYTHON COMMAND WE RAN  COMMANDS BELOW TO CREATE A TABLE WITH ITS PROPERTIES.:
	>>>from pkg import db
	>>>from pkg import app
	>>>app.app_context().push()
	>>>db.create_all()
10. READ MORE DETAILS WITHIN THE FILES

# Django CRUD API Project by Tahir Bin Bashir

This project, developed by Tahir Bin Bashir, demonstrates the creation of CRUD APIs using Django and Django REST framework. It includes two models: `Section` and `Student`, with a foreign key relationship.


# Setup Instructions

**Create a virtual environment:**
   ```bash
   python -m venv venv
Activate the virtual environment:

On Windows:
bash
.\venv\Scripts\activate


On macOS/Linux:
bash
source venv/bin/activate
Install dependencies:

bash
Apply migrations:

python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
python manage.py runserver
Access the APIs:

List all sections: http://127.0.0.1:8000/api/sections/
Create a section: http://127.0.0.1:8000/api/sections/
View, update, and delete a section: http://127.0.0.1:8000/api/sections/{section_id}/
List all students within a section: http://127.0.0.1:8000/api/students/
Create a student within a section: http://127.0.0.1:8000/api/students/
View, update, and delete a student: http://127.0.0.1:8000/api/students/{student_id}/
Access the default API home view:

http://127.0.0.1:8000/api/


Developed by Tahir Bin Bashir
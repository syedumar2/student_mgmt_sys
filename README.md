Steps to run Django miniproject
1. Set Up Your Environment
  Ensure you have Python and Django installed. If not, install them:
    pip install django
2. Navigate to Your Project Directory
  Move to your Django project’s root folder:
    cd path/to/your/project
3. Create a Virtual Environment (Optional but Recommended)
    python -m venv venv
   Activate the virtual environment:
    venv\Scripts\activate
4. Apply Migrations
  Run the migrations to set up the database schema:
   python manage.py migrate
5. Create a Superuser (For Admin Access, Optional)
    python manage.py createsuperuser
    Follow the prompts to enter the username, email, and password.
6. Run the Development Server
  python manage.py runserver
  The Django project should now be running at http://127.0.0.1:8000/.
7. Access the Application
  Open a browser and go to http://127.0.0.1:8000/students/.
  If you set up Django Admin, access it at http://127.0.0.1:8000/admin/ and log in with the superuser credential

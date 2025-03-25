# User_Listing
User Listing Application

# Description
 The User Listing Application is a web application built using React for the frontend and Django for the backend. It fetches user data from the Random User API, stores it in a database, and provides a user-friendly interface to view and manage user information.

# Features
  Fetches user data from the https://randomuser.me/api/?results=10.
  Displays a list of users with pagination.
  Allows users to view detailed information about each user.

# Technologies Used
  Frontend: React
  Backend: Django, Django REST Framework
  Database: SQLite 
  API: Random User API

# Installation

  # Prerequisites
   [Node.js](https://nodejs.org/) (v12 or higher)
   [Python](https://www.python.org/downloads/) (v3.6 or higher)
   [pip](https://pip.pypa.io/en/stable/) (Python package manager)

  # Backend (django) Setup
  Create Directory
      cd user_listing
   Install packages 
      pip install django djangorestframework requests   
    Run the migration in order to run the sql and django in sync 
        python manage.py migrate
     Fetch users from random user api 
        python manage.py fetch_users
     Start django server
        python manage.py runserver
    
  Frontend Setup (React)
        Create Directory
            cd user-listing-frontend
        Install packages
            npm install
        Start React developement server
            npm start

# Usage
  Open your browser and navigate to http://localhost:3000 to access the User Listing Application.
  Click on a user to view their detailed information.
  Use the "Back to User List" button to return to the user list.

# Acknowledgments
  Randomuser.me for providing user data


        

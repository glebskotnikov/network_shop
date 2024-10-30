# Electronics Trading Network

This backend part is intended for an online electronics trading platform. 
The aim of the project is to provide functionality for managing the multi-level
hierarchy of the trading network and interacting with users.

## Main Functionality 

1. User authorization and authentication.
2. Role distribution among users (user and admin).
3. User identification features like email, country, city, street and house number.
4. The trading network presents a hierarchical structure with three main levels: Factory, Retail Chain and Individual Entrepreneur.
5. Each level of the network refers to a single equipment supplier (not necessarily the previous hierarchical level).
6. CRUD for objects of network model in administrative panel (admin can delete or edit all objects).
7. Ability to filter objects based on the city name in the site header.
8. A feature to clear the debt to the supplier for selected objects via an admin action.
9. Views set creation using Django Rest Framework (DRF), including CRUD for supplier model (updating of "Debt to the supplier" field via API is forbidden).
10. Objects Filtering based on a specific country.
11. API access rights configuration to ensure only active employees have access.

## Setup
Follow the steps below to setup and run the project locally:

1. Clone the Repository.
2. Setup a Virtual Environment.
Navigate to your project directory and create a virtual environment using the command:
python3 -m venv venv
3. Activate the Virtual Environment.
Activate the virtual environment using the following command:
source venv/bin/activate
4. Install Dependencies.
Install all the required dependencies from the 'requirements.txt' file using the command:
pip install -r requirements.txt
5. Setup Environment Variables.
Create an .env file in the root directory of your project and define the variables 
that are in the .env.sample file
6. Initialize the Database.
python manage.py migrate
7. Start the Server
Run the command below to start Django's development server:
python manage.py runserver
The server should now be accessible on http://localhost:8000/

## Installation

As Postman is used for result visualization, the project setup will include its usage. 

1. Install Postman if you don't have it yet. It can be downloaded [here](https://www.postman.com/downloads/).
2. Clone the repository: git@github.com:glebskotnikov/bulletin_board.git
3. Install project dependencies (this command assumes that you are in the root directory of the project): pip install -r requirements.txt 
4. Run the server: python3 manage.py runserver

## Usage 

Use Postman to test the web application.

1. When your server is running, open Postman.
2. Create a new request (e.g., GET, POST, etc.).
3. Insert the server URL, for example, `http://localhost:8000/`.
4. If required, add the request body in JSON format or enter necessary parameters.
5. Press the "Send" button to send the request.
6. The server's response will be displayed at the bottom of the window.

This project provides several API endpoints for interacting with the application:

USERS
- `POST /users/login`: Log in an existing user.
- `GET /users/users/`: Getting a list of all products.
- `POST /users/users/`: Registering a new user.
- `GET /users/users/<int:pk>/`: Retrieving detailed information about a user.
- `PUT /users/users/<int:pk>/`: Modifying an existing user.
- `PATCH /users/users/<int:pk>/`: Making partial changes to a user.
- `DELETE /users/users/<int:pk>/`: Deleting a user.

PRODUCTS
- `GET /users/products/`: Getting a list of all products.
- `POST /users/products/`: Registering a new product.
- `GET /users/products/<int:pk>/`: Retrieving detailed information about a product.
- `PUT /users/products/<int:pk>/`: Modifying an existing product.
- `PATCH /users/products/<int:pk>/`: Making partial changes to a product.
- `DELETE /users/products/<int:pk>/`: Deleting a product.



## Docker-compose

1. Install Docker if you don't already have it. You can download it [here](https://docs.docker.com/).
2. Type the command in the terminal: docker-compose up -d --build

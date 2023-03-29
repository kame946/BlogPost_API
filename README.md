Blog Post API
This is a Django RESTful API that allows users to create and update blog posts. Users can create a new blog post, update an existing post by its ID, and view all the blog posts. The blog post consists of a title and content fields.

Setup

1. Clone this repository to your local machine
2. Create a virtual environment using virtualenv or venv and activate it
3. Install the required packages using pip install -r requirements.txt
4. Run the server using python manage.py runserver


Endpoints

I. Create a Blog Post

Endpoint: /create

HTTP Method: POST

Request Body:

json
Copy code
{
  "title": "New Blog Post",
  "content": "This is the content of the new blog post."
}
Response Body:

json
Copy code
{
  "id": 1,
  "title": "New Blog Post",
  "content": "This is the content of the new blog post."
}

II. Update a Blog Post

Endpoint: /create/<id>

HTTP Method: PUT

Request Body:

json
Copy code
{
  "title": "Updated Blog Post",
  "content": "This is the updated content of the blog post."
}
Response Body:

json
Copy code
{
  "id": 1,
  "title": "Updated Blog Post",
  "content": "This is the updated content of the blog post."
}


III. View All Blog Posts

Endpoint: /all

HTTP Method: GET

Response Body:

json
Copy code
[
  {
    "id": 1,
    "title": "New Blog Post",
    "content": "This is the content of the new blog post."
  },
  {
    "id": 2,
    "title": "Another Blog Post",
    "content": "This is the content of another blog post."
  }
]



Dependencies
This project uses the following packages:

1. Django
2. djangorestframework
You can install them using pip by running pip install -r requirements.txt.

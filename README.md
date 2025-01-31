# Social Media API

This is a simple social media API built with **FastAPI** and **Python**. The application allows users to register, verify their email, log in, create posts, comment on posts, like posts, and fetch all posts for a user. The API is backed by **SQLite** using **SQLAlchemy** ORM for database management.

The project includes Docker support for easy deployment.

## Table of Contents

- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Endpoints](#endpoints)
- [Docker Setup](#docker-setup)

## Technologies

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite**: Lightweight database used for data persistence.
- **Pydantic**: Data validation and settings management.
- **JWT**: JSON Web Token for user authentication.
- **Docker**: Containerization for easy deployment.
- **Terraform**: Deploy API on AWS ECS.

## Setup and Installation

### Clone the repository:

```bash
git clone https://github.com/nimishmadan98/social_media_api.git
cd social-media-api
```

### Install dependencies:
It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```
Run the API
1. Without Docker (Local Development):
You can run the FastAPI server using Uvicorn.

```bash
uvicorn app.main:app --reload
```
This will start the server at http://localhost:8000.

2. With Docker (Containerized):
If you prefer to run the app with Docker, you can build and run the Docker container.

```bash
docker build -t social-media-api .
docker run -d -p 8000:8000 social-media-api
```
This will start the app on http://localhost:8000.

To deploy the application to AWS ECS, use the following terraform commands.
```bash
cd terraform/  # move inside terraform folder
terraform init
terraform plan
terraform apply
```

### Environment Variables
The app uses several environment variables that should be set in a .env file at the root of the project for local development:

```bash
# For SMTP (Email verification)
SMTP_SERVER=<smtp-server>
SMTP_PORT=<smtp-port>
SMTP_USER=<smtp-username>
SMTP_PASSWORD=<smtp-password>
SENDER_EMAIL=<sender-email>
```
Make sure to replace the values with appropriate settings for your environment.

### Endpoints

![948B9204-F519-4F61-A848-CFA732B48E58](https://github.com/user-attachments/assets/42fec9b3-33d7-4b3f-b4a1-2578332860b9)

#### 1. Register User
POST /users

Request Body:

```json
{
  "name": "user_name",
  "email": "user_email",
  "password": "user_password"
}
```

Response:

```json
{
  "message": "User registered successfully",
  "username": "user_name"
}
```

#### 2. Verify Email
GET /users/verify/{token}

Description: Verifies the user's email using a token sent during registration.

URL parameter: token (JWT token)

Response:

```json

{
  "message": "Email verified successfully!"
}
```

#### 3. Login
POST /auth/login

Request Body:

```json
{
  "email": "email",
  "password": "user_password"
}
```

Response:

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

#### 4. Create Post
POST /posts/

Request Body:

```json
{
  "content": "Your post content here"
}
```

Response:

```json
{
  "id": 1,
  "content": "Your post content here",
  "likes_count": 0,
  "comments_count": 0
}
```

#### 5. Comment on a Post
POST /posts/{post_id}/comments

Request Body:

```json
{
  "content": "Your comment content",
}
```

Response:

```json
{
  "content": "string",
  "id": 0,
  "user_id": 0,
  "post_id": 0
}
```

#### 6. Like a Post
POST /posts/{post_id}/likes/

Response:

```json
{
  "id": 0,
  "user_id": 0,
  "post_id": 0
}
```

#### 7. Get All Posts for a User
GET /posts

Description: Get all posts created by a user.

Response:

```json
[
  {
    "content": "string",
    "id": 0,
    "likes_count": 0,
    "comments_count": 0
  }
]
```

## Docker Setup
The project comes with a Dockerfile for easy deployment. To build and run the application in Docker:

Build the Docker image:

```bash
docker build -t social-media-api .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 social-media-api
```
This will expose the FastAPI app on http://localhost:8000.


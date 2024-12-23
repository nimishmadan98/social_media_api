# Social Media API

This is a simple social media API built with **FastAPI** and **Python**. The application allows users to register, verify their email, log in, create posts, comment on posts, like posts, and fetch all posts for a user. The API is backed by **SQLite** using **SQLAlchemy** ORM for database management.

The project includes Docker support for easy deployment.

## Table of Contents

- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Endpoints](#endpoints)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Technologies

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: ORM for database interaction.
- **SQLite**: Lightweight database used for data persistence.
- **Pydantic**: Data validation and settings management.
- **JWT**: JSON Web Token for user authentication.
- **Docker**: Containerization for easy deployment.

## Setup and Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/social-media-api.git
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
1. Register User
POST /register

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

2. Verify Email
GET /verify/{token}

Description: Verifies the user's email using a token sent during registration.

URL parameter: token (JWT token)

Response:

```json

{
  "message": "Email verified successfully!"
}
```

3. Login
POST /login

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

4. Create Post
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

5. Comment on a Post
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

6. Like a Post
POST /posts/{post_id}/likes/

Response:

```json
{
  "id": 0,
  "user_id": 0,
  "post_id": 0
}
```

7. Get All Posts for a User
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

## Contributing
If you'd like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request.

### Steps to contribute:
Fork the repo.
Clone your fork.
Create a new branch (git checkout -b feature-xyz).
Make your changes.
Commit your changes (git commit -am 'Add feature xyz').
Push to the branch (git push origin feature-xyz).
Open a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

```css
This `README.md` provides a comprehensive guide to set up, run, and interact with your social media API, including all the endpoints, Docker setup details, and environment configuration. You can simply copy and paste this content into your `README.md` file.
```

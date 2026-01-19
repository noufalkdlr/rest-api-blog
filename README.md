# 📝 RESTful Blog API - Django & DRF

A robust, production-ready RESTful API for content management built with Django 6 and Django REST Framework (DRF). This project is designed with a modular architecture focusing on security, scalability, and optimized database performance.

## 🚀 Key Features

* **JWT Authentication**: Secure user registration, login, and token refresh mechanisms using `SimpleJWT`.
* **Full CRUD Functionality**: Complete implementation for managing blog posts and hierarchical comments.
* **Automatic Slug Generation**: SEO-friendly URL slugs generated automatically from post titles with collision handling.
* **Advanced Data Handling**: Integrated filtering by author, full-text search across titles/content, and dynamic ordering.
* **Performance & Security**: Implemented rate limiting (throttling), efficient pagination (PageNumberPagination), and strict permission classes (IsOwnerOrReadOnly).
* **API Documentation**: Integrated Swagger and Redoc UI via `drf-spectacular` for interactive API testing.
* **Containerization**: Fully dockerized environment using the high-performance `uv` package manager for faster builds.

## 🛠 Tech Stack

* **Framework**: Django 6.0.1, Django REST Framework 3.16.1.
* **Database**: PostgreSQL (psycopg2-binary).
* **Authentication**: JSON Web Token (JWT).
* **Ops & Deployment**: Docker, Gunicorn, WhiteNoise, `uv` package manager.

## 🔗 API Endpoints

### User Management
- `POST /api/register/` - Create a new user account.
- `POST /api/login/` - Obtain Access & Refresh JWT tokens.
- `POST /api/token/refresh/` - Refresh expired access tokens.

### Blog Posts & Comments
- `GET /api/posts/` - List all posts with pagination, search, and filters.
- `POST /api/posts/` - Create a new post (Authenticated).
- `GET/PUT/DELETE /api/post/<slug>/` - Retrieve, Update, or Delete a specific post.
- `GET/POST /api/posts/<slug>/comments/` - Manage comments for a specific post.

## ⚙️ Setup & Installation

### Using Docker (Recommended)
```bash
# Build and run the container
docker build -t rest-api-blog .
docker run -p 8080:8080 rest-api-blog

# Blog API

The **Blog API** is a RESTful API designed for managing blog posts in a blogging platform. Built using **FastAPI**, **SQLAlchemy**, and **MySQL**, this API allows you to handle blog post data with robust features such as CRUD operations, search, and pagination.

## Features

- **Create Blog Posts**: Easily create blog posts with a title, content, author, tags, and publication status.
- **Update Blog Posts**: Modify existing blog posts, including updating the title, content, or tags.
- **Delete Blog Posts**: Remove posts from the system securely.
- **Post Management**: Organize and manage posts with fields like `created_at`, `updated_at`, `published`, and `tags`.
- **Search Functionality**: Search posts by title, content, or tags for better organization.
- **Pagination**: Retrieve large datasets efficiently by using pagination for fetching posts.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: An ORM for database interactions with MySQL.
- **MySQL**: Database for persistent storage of blog post data.
- **Alembic**: A tool for handling database migrations and schema changes.
- **Pydantic**: Provides data validation and settings management.
- **Uvicorn**: ASGI server to run the FastAPI app.

## Database Model

The **Blog Post Model** is the core of this API, with the following fields:
- **Title**: The title of the blog post.
- **Content**: The content of the blog post.
- **Author**: The author of the post (can be optional).
- **Tags**: A list of tags associated with the blog post (optional).
- **Created At**: The timestamp of when the post was created.
- **Updated At**: The timestamp of the last update to the post.
- **Published**: A boolean to mark whether the post is published or still a draft.

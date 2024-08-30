# Django Blog & Rating System

This is a Django-based web application that allows users to create blog posts and rate them. Users can submit ratings for individual posts and retrieve a list of all blog posts along with their average ratings.

## Features

- **Blog Posts**: Users can create, view, update, and delete blog posts.
- **Rating System**: Users can rate blog posts. Each post displays its average rating and the total number of ratings.
- **Asynchronous Task Processing**: Ratings are processed asynchronously using Celery and Redis to ensure smooth and scalable operations.
- **REST API**: Fetch all blog posts and their average ratings through a simple API.

## Requirements

- Docker
- Docker Compose
- Make (Optional, for simplified commands)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-django-blog.git
cd your-django-blog
```
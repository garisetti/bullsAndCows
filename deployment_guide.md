# Deployment Guide for Bulls and Cows Web App

This guide explains how to deploy your Django application to a hosting platform. We have prepared the project for platforms like **Render**, **Heroku**, or **Railway**.

## Prerequisites

- You have a GitHub account and the project is pushed to a repository.
- You have an account on the hosting platform (e.g., [Render](https://render.com/), [Heroku](https://www.heroku.com/)).

## Files Created for Deployment

- **`requirements.txt`**: Lists all Python dependencies.
- **`Procfile`**: Tells the hosting platform how to run the app (`gunicorn`).
- **`runtime.txt`**: Specifies the Python version.
- **`settings.py`**: Updated to read configuration from environment variables.

## Deploying to Render (Recommended)

1.  **Create a New Web Service**:
    - Go to your Render dashboard and click "New +".
    - Select "Web Service".
    - Connect your GitHub repository.

2.  **Configure the Service**:
    - **Name**: Choose a name for your app.
    - **Region**: Select a region close to you.
    - **Branch**: `main` (or your working branch).
    - **Runtime**: `Python 3`.
    - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
    - **Start Command**: `gunicorn bulls_and_cows.wsgi`

3.  **Environment Variables**:
    - Scroll down to "Environment Variables" and add the following:
        - `PYTHON_VERSION`: `3.12.1` (matches runtime.txt)
        - `SECRET_KEY`: Generate a strong random string (e.g., use an online generator).
        - `DEBUG`: `False`
        - `WEB_CONCURRENCY`: `4` (optional, for gunicorn workers)

4.  **Deploy**:
    - Click "Create Web Service". Render will build and deploy your app.

## Deploying to Heroku

1.  **Install Heroku CLI**: Download and install the Heroku CLI.
2.  **Login**: Run `heroku login`.
3.  **Create App**: Run `heroku create your-app-name`.
4.  **Add Buildpacks**:
    - `heroku buildpacks:set heroku/python`
5.  **Set Environment Variables**:
    - `heroku config:set SECRET_KEY='your-secret-key'`
    - `heroku config:set DEBUG=False`
6.  **Deploy**:
    - `git push heroku main`

## Important Notes

- **Database**: The current setup uses SQLite, which is a file-based database. **On platforms like Render/Heroku, the filesystem is ephemeral, meaning your database will be reset every time you redeploy.**
    - For a real production game with persistent user accounts or history, you should use a PostgreSQL database.
    - To use PostgreSQL:
        1.  Create a PostgreSQL database on your hosting provider.
        2.  Add the `DATABASE_URL` environment variable with the connection string.
        3.  The app is already configured to use `dj-database-url` to read this variable.

- **Static Files**: We configured `whitenoise` to serve static files efficiently. The `collectstatic` command in the build step prepares these files.

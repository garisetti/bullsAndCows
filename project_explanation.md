# Bulls and Cows Web Application - Project Explanation

This document provides a detailed explanation of the file structure and the purpose of each file in the `bullsAndCowsWebApp` project.

## Project Root

### `manage.py`
This is Django's command-line utility for administrative tasks. It allows you to interact with this Django project in various ways, such as running the development server, creating migrations, and running tests. It sets the `DJANGO_SETTINGS_MODULE` environment variable to point to `bulls_and_cows.settings`.

### `test_logic.py`
This is a standalone Python script used to verify the core game logic independently of the Django web framework. It imports `calculate_bulls_and_cows` from `game.utils` and runs several test cases (exact match, no match, partial match, mixed match) to ensure the logic is correct.

### `db.sqlite3`
This is the default SQLite database file created by Django. Since this project primarily uses session storage for the game state, this file might not be heavily used for game data but is required for Django's internal operations (like session management if using database-backed sessions).

## Project Configuration Directory: `bulls_and_cows/`

This directory contains the configuration files for the entire Django project.

### `settings.py`
This file contains all the configuration settings for the Django project. Key settings include:
- **`INSTALLED_APPS`**: Lists all applications that are enabled in this Django installation. It includes `game` (our custom app) and standard Django apps.
- **`MIDDLEWARE`**: A list of middleware components that process requests and responses. `SessionMiddleware` is crucial here for maintaining game state.
- **`TEMPLATES`**: Configuration for the template engine.
- **`DATABASES`**: Database configuration (SQLite by default).
- **`SECRET_KEY`**: A secret key used for cryptographic signing.

### `urls.py`
This file contains the project-level URL declarations. It defines the root URL mapping.
- It includes `path('admin/', admin.site.urls)` for the Django admin interface.
- It includes `path('', include('game.urls'))`, which delegates the handling of the root URL (`/`) and sub-paths to the `game` application's URL configuration.

### `wsgi.py`
WSGI (Web Server Gateway Interface) configuration for the project. It exposes the WSGI callable as a module-level variable named `application`. This is the entry point for WSGI-compatible web servers to serve your project.

### `asgi.py`
ASGI (Asynchronous Server Gateway Interface) configuration for the project. It exposes the ASGI callable as a module-level variable named `application`. This is the entry point for ASGI-compatible web servers.

## Game Application Directory: `game/`

This directory contains the source code for the "Bulls and Cows" game application.

### `views.py`
This file contains the view functions that handle HTTP requests and return responses.
- **`index(request)`**: The main view that renders the game interface. It initializes the game state in the session (secret word, attempts, history) if it doesn't exist.
- **`guess(request)`**: Handles the form submission for a user's guess. It validates the input, calculates bulls and cows using `calculate_bulls_and_cows`, updates the session history, and checks for a win condition.
- **`reset(request)`**: Clears the session data to restart the game and redirects to the index page.

### `utils.py`
This file contains utility functions that encapsulate the core game logic.
- **`get_secret_word()`**: Returns a random 4-letter isogram word from a predefined list.
- **`calculate_bulls_and_cows(secret, guess)`**: Compares the secret word and the user's guess to calculate the number of Bulls (correct letter, correct position) and Cows (correct letter, wrong position).

### `urls.py`
This file defines the URL patterns specific to the `game` application.
- **`path('', views.index, name='index')`**: Maps the root URL of the app to the `index` view.
- **`path('guess/', views.guess, name='guess')`**: Maps `/guess/` to the `guess` view.
- **`path('reset/', views.reset, name='reset')`**: Maps `/reset/` to the `reset` view.

### `models.py`
This file is used to define database models. Currently, it is empty because the game state is managed entirely within the user's session, and no persistent database storage is required for the game logic itself.

### `apps.py`
This file contains the configuration for the `game` application. It defines the `GameConfig` class.

### `tests.py`
This file is for writing tests for the application. It is currently empty or contains a default placeholder.

### `admin.py`
This file is used to register models with the Django admin site. It is currently empty as there are no models to register.

### `migrations/`
This directory stores database migration files, which track changes to your models. Since there are no models, this directory likely contains only `__init__.py`.

### `static/`
This directory is used to store static files like CSS, JavaScript, and images.
- **`game/style.css`**: Contains the CSS styles for the game interface.

### `templates/`
This directory stores the HTML templates.
- **`game/index.html`**: The main HTML template for the game interface. It displays the game status, input form, and guess history.

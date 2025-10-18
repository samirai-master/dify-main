"""Application entry point for Flask and Celery setup."""

import sys


def is_db_command() -> bool:
    """Check if the current command is related to database migrations."""
    if len(sys.argv) > 1 and sys.argv[0].endswith("flask") and sys.argv[1] == "db":
        return True
    return False


# Create app
if is_db_command():
    from api.app_factory import create_migrations_app

    app = create_migrations_app()
else:
    from api.app_factory import create_app

    app = create_app()
    celery = app.extensions.get("celery")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)



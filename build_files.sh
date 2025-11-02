if ! command -v pipenv &> /dev/null
then
    echo "pipenv is not installed. Installing pipenv..."
    # Install pipenv
    python -m pip install pipenv
fi

# Install dependencies from Pipfile.lock
pipenv install --deploy --ignore-pipfile

# Run collectstatic command
pipenv run python manage.py collectstatic --noinput
# Social Media Web Application

This is a Social Media Web Application built on Django. It allows users to connect, share posts, and interact with each other.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- Post creation, editing, and deletion
- User profiles and connections

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SanzEev17/Social-Media-in-Django.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Social-Media-in-Django
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Set up your environment variables:

   Create a `.env` file in the root directory and add the following variables:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   EMAIL_BACKEND=your_email_backend
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_host_user
   EMAIL_HOST_PASSWORD=your_email_host_password
   ```

   Replace `your_secret_key`, `your_email_backend`, `your_email_host`, `your_email_port`, `your_email_host_user`, and `your_email_host_password` with your own values.

2. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

3. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at http://localhost:8000/.

## Configuration

You can customize the application by modifying the settings in the `settings.py` file.

For more information on Django settings, refer to the [Django documentation](https://docs.djangoproject.com/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

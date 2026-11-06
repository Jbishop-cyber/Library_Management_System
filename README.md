# Bishop's Library Management System

A web-based Library Management System built with Python and Flask. The application allows users to browse a library's book collection and view individual book details.

## Project Overview

This project is an extension of my function-based Python Library Management System. It is being developed into a web application using Flask, HTML, CSS, and eventually JavaScript.

The goal is to build a functional library website with book management, member registration, and borrowing functionality.

## Technologies Used

- **Python** – Backend programming
- **Flask** – Web framework
- **HTML** – Webpage structure
- **CSS** – Webpage styling
- **Jinja2** – Dynamic HTML templating
- **SQLite** – Planned database integration

## Current Features

- Homepage
- Browse book collection
- View individual book details
- Dynamic book pages using Flask routes
- Reusable HTML layouts using Jinja template inheritance
- Basic CSS styling

## Project Structure

```text
web_app/
├── app.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── books.html
    └── book_details.html
```

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/Jbishop-cyber/Library_Management_System.git
```

2. Navigate into the project directory:

```bash
cd Library_Management_System/web_app
```

3. Create a virtual environment:

```bash
python3 -m venv .venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

5. Install Flask:

```bash
pip install flask
```

6. Run the application:

```bash
python app.py
```

7. Open your browser:

```text
http://127.0.0.1:5000
```

## Development Roadmap

- [x] Flask fundamentals
- [x] HTML templates and Jinja
- [ ] CSS, JavaScript and static files
- [ ] GET and POST requests
- [ ] Forms and input validation
- [ ] SQLite database integration
- [ ] User authentication
- [ ] Book CRUD operations
- [ ] Borrowing and returning functionality
- [ ] Testing and deployment

## Project Status

**Currently in development.**

This project is being built incrementally as part of my Python and backend web development learning journey.
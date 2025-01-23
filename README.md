# QA_DOCS - AI-powered Document Q&A Application

QA_DOCS is a web-based application that allows users to upload documents and interact with them through AI-powered Q&A functionality. The application is built using Django and integrates cutting-edge machine learning models for answering questions based on the content of the uploaded documents.

## Features

- **Document Upload**: Users can upload various types of documents (e.g., PDFs, Excel files).
- **AI-Powered Q&A**: Users can ask questions about the document's content, and the AI will respond with contextually relevant answers.
- **Easy-to-use Interface**: Simple and intuitive web interface for seamless interaction.
- **Fast Document Processing**: Optimized document parsing and AI model inference for quick results.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: OpenAI API, Hugging Face Transformers, Custom ML Models
- **Database**: SQLite (for local development), PostgreSQL (production)
- **Version Control**: Git, GitHub

## Installation

### 1. Clone the Repository

To get started with the project, clone the repository to your local machine:

```bash
git clone https://github.com/surajsk2003/QA_DOCS.git
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (for macOS/Linux)
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the following commands to set up the database:

```bash
# Run migrations to set up the database
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## Usage

- Upload a document (e.g., a PDF or Excel file).
- Once the document is uploaded, type any question related to its content in the input field.
- The AI model will generate and display an answer based on the document’s text.

## Deployment

To deploy the application to production, you can use services like **Heroku**, **AWS**, or **DigitalOcean**. The following steps outline how to deploy on **Heroku**:

1. Install the Heroku CLI and log in.
2. Create a `Procfile` in the root of the project:

```
web: gunicorn qa_docs.wsgi
```

3. Push the project to Heroku:

```bash
git push heroku main
```

## Contributing

We welcome contributions to this project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Create a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) for the backend framework.
- [Hugging Face](https://huggingface.co/) for providing pre-trained transformer models for Q&A functionality.
- [OpenAI](https://openai.com/) for their powerful language models.
- [Heroku](https://www.heroku.com/) for easy deployment options.

---

This template covers the key sections that should be included in a `README.md`. Make sure to adjust the specifics to match your project details.
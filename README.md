# QA_DOCS - AI-powered Document Q&A Application

**QA_DOCS** is a web-based application that allows users to upload documents and interact with them through AI-powered Q&A functionality. This application utilizes advanced machine learning models to analyze document content and respond to user queries with contextually relevant answers.

## Features

- **Document Upload**: Users can upload various types of documents such as PDFs, Word documents, and Excel files for analysis.
- **AI-Powered Q&A**: Users can input questions related to the content of the uploaded document, and the AI will respond with answers based on the document's information.
- **Easy-to-use Interface**: A simple and intuitive web interface for seamless interaction between users and the AI model.
- **Fast Document Processing**: Optimized document parsing and machine learning model inference for quick and accurate results.
- **Admin Panel**: Admin users can manage uploaded documents, users, and settings via the Django admin interface.

## Technologies Used

- **Backend**: Django for the web framework, handling the application logic and routing.
- **Frontend**: HTML, CSS, and JavaScript for the user interface and document interaction.
- **Machine Learning**: OpenAI API, Hugging Face Transformers, and custom models for question answering.
- **Database**: SQLite for local development; PostgreSQL for production.
- **Version Control**: Git and GitHub for version control and collaboration.
- **Hosting & API**: Microsoft **Azure** for both hosting the application and using the Azure-hosted OpenAI models.

## Installation

To set up and run QA_DOCS on your local machine, follow the steps below:

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/surajsk2003/QA_DOCS.git
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment to manage dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

### 3. Install Dependencies

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the database migrations to set up the required tables:

```bash
# Run migrations
python manage.py migrate

# Create a superuser for the Django admin panel
python manage.py createsuperuser
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory and add your Azure-specific environment variables:

```bash
# .env file
AZURE_API_KEY=your_azure_api_key
AZURE_ENDPOINT=your_azure_endpoint_url
AZURE_DEPLOYMENT_NAME=your_deployment_name
```

**Note**: These values can be obtained from your Azure portal, where you set up the OpenAI API and your deployment.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can access the application at `http://127.0.0.1:8000/`.

## Usage

1. **Upload a Document**: Select and upload a document such as a PDF, Word, or Excel file.
2. **Ask Questions**: Once the document is uploaded, type any question related to its content in the input field.
3. **AI-Generated Answers**: The AI model will analyze the document and generate an answer based on the document’s text, displaying it on the page.

## Deployment on Azure

To deploy the QA_DOCS application on **Microsoft Azure** for both hosting the app and using the OpenAI API, follow these steps:

### 1. Set Up Azure App Service

1. Log in to your **Azure portal** and create an **App Service** resource.
2. Configure the App Service to use **Python** (make sure you choose the appropriate Python version).
3. In the **Configuration** section, add environment variables for Azure API keys and endpoint URLs:
   - `AZURE_API_KEY`: Your Azure API key.
   - `AZURE_ENDPOINT`: The base URL for your Azure OpenAI service.
   - `AZURE_DEPLOYMENT_NAME`: The deployment name of your model.

### 2. Set Up Azure Database

1. Set up an **Azure Database for PostgreSQL** or any database of your choice.
2. Update the `DATABASES` setting in `settings.py` to use Azure's PostgreSQL database.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_azure_database_host',
        'PORT': '5432',
    }
}
```

### 3. Configure the Azure Pipeline for Deployment

1. Create a **GitHub Actions** workflow to automate deployments to Azure. 
2. In your repository, create a `.github/workflows/azure-deploy.yml` file with the following content:

```yaml
name: Azure Deploy

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy to Azure App Service
        uses: Azure/webapps-deploy@v2
        with:
          app-name: 'your-app-name'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          package: .
```

### 4. Push the Application to Azure

Once the repository is set up, push your code to the Azure App Service using the GitHub Actions pipeline, or manually through **Azure CLI**.

```bash
git push azure main
```

### 5. Open the Application

Once deployed, you can access the application by going to the Azure **App Service URL**.

## Contributing

We welcome contributions to this project! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to your forked repository (`git push origin feature-branch`).
5. Create a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **[Django](https://www.djangoproject.com/)**: Web framework for backend development.
- **[OpenAI](https://openai.com/)**: For providing the GPT models for natural language processing.
- **[Hugging Face](https://huggingface.co/)**: For pre-trained transformer models used in the Q&A functionality.
- **[Microsoft Azure](https://azure.microsoft.com/)**: For hosting the application and providing the API for the OpenAI models.
- **[Heroku](https://www.heroku.com/)**: For deployment (if using as an alternative to Azure).

from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import Document, QuestionAnswer
import pandas as pd
import json
from .ai_logic import get_answer  # Assuming this is your AI model


# Home view to render the upload and question interface
def home(request):
    return render(request, "base.html")


# File upload handler
def upload(request):
    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']

        # Save the file to the server
        fs = FileSystemStorage(location="media/documents/")
        try:
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)  # Full path of the saved file

            # Create a Document entry in the database
            document = Document.objects.create(
                uploaded_file=filename,
                file_name=uploaded_file.name
            )

            # Parse and save the Excel file content as JSON
            try:
                df = pd.read_excel(file_path)  # Assuming an Excel file
                json_file_path = f"{file_path}.json"
                df.to_json(json_file_path, orient='records')  # Save DataFrame as JSON file

                # Store the JSON file path in the session for later use
                request.session['document_file_path'] = json_file_path
                request.session['document_id'] = document.id  # Store document ID for linking to Q&A

                return JsonResponse({'success': True, 'message': 'File uploaded and processed successfully!'})
            except Exception as e:
                return JsonResponse({'error': f'Error parsing document: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error saving file: {str(e)}'}, status=500)

    return JsonResponse({'error': 'No document uploaded.'}, status=400)


# Question-answer handler
def ask_question(request):
    if request.method == 'GET':
        # Parse the query parameter to extract the question
        question = request.GET.get('question', '').strip()
        if not question:
            return JsonResponse({'error': 'Question is required.'}, status=400)

        # Process the question for simple greetings
        greeting_response = process_question(question)
        if greeting_response:
            return JsonResponse({'answer': greeting_response}, status=200)

        # Check if document exists in the session
        document_id = request.session.get('document_id', None)
        if not document_id:
            return JsonResponse({'error': 'No document found to process the question.'}, status=400)

            # Fetch the document from the database
        document = Document.objects.get(id=document_id)

        # Access the uploaded JSON file
        file_path = f"media/documents/{document.uploaded_file}"
        json_file_path = f"{file_path}.json"  # Assuming you saved it as JSON earlier

        # Load the JSON data
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        # Use the JSON data to answer the question
        answer = get_answer(question, json_data)  # Assuming `get_answer` processes the question with the document

        # Save the question-answer pair to the database
        QuestionAnswer.objects.create(
            question=question,
            answer=answer,
            document=document
        )

        return JsonResponse({'answer': answer}, status=200)
        # except Exception as e:
        #     return JsonResponse({'error': f'Error processing question: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


# Helper to process simple greetings in the question
def process_question(question):
    # List of keywords to check in the question
    keywords = ["hello", "hi", "yo", "hello world"]

    # Convert question to lowercase for case-insensitive comparison
    question_lower = question.lower()

    # Check if any keyword is present in the question
    for word in keywords:
        if word in question_lower:
            return "Hello! How can I help you?"

    # Default response if no keywords are found
    return None  # Return None so it can continue processing for AI answers
from django.db import models

# Document model to store uploaded files
class Document(models.Model):
    uploaded_file = models.FileField(upload_to='documents/', verbose_name="Uploaded File")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")
    file_name = models.CharField(max_length=255, blank=True, verbose_name="File Name")
    
    def _str_(self):
        return self.file_name if self.file_name else "Document " + str(self.id)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


# QA Model to store questions and their answers
class QuestionAnswer(models.Model):
    question = models.CharField(max_length=512, verbose_name="Question")
    answer = models.TextField(verbose_name="Answer")
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="qa_pairs", verbose_name="Document")
    asked_at = models.DateTimeField(auto_now_add=True, verbose_name="Asked At")
    
    def _str_(self):
        return f"Q: {self.question} | A: {self.answer}"

    class Meta:
        verbose_name = "Question Answer"
        verbose_name_plural = "Question Answers"
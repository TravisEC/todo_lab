from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title.strip():
            raise forms.ValidationError("Title cannot be empty or only spaces.")
        return title.strip()
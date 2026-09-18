from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication

        fields = [
            "name",
            "email",
            "phone",
            "resume",
            "cover_letter",
        ]

        labels = {
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "resume": "Resume",
            "cover_letter": "Cover Letter",
        }

        help_texts = {
            "resume": "Upload your resume in PDF, DOC, or DOCX format.",
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 outline-none transition focus:border-yellow-400 focus:bg-white focus:ring-4 focus:ring-yellow-100",
                "placeholder": "Enter your full name",
            }),

            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 outline-none transition focus:border-yellow-400 focus:bg-white focus:ring-4 focus:ring-yellow-100",
                "placeholder": "you@example.com",
            }),

            "phone": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 outline-none transition focus:border-yellow-400 focus:bg-white focus:ring-4 focus:ring-yellow-100",
                "placeholder": "Enter your phone number",
            }),

            "resume": forms.ClearableFileInput(attrs={
                "class": "block w-full cursor-pointer rounded-xl border border-gray-200 bg-gray-50 text-sm text-gray-600 file:mr-4 file:border-0 file:bg-yellow-400 file:px-5 file:py-3 file:font-semibold file:text-gray-900 hover:file:bg-yellow-500",
            }),

            "cover_letter": forms.Textarea(attrs={
                "class": "w-full rounded-xl border border-gray-200 bg-gray-50 px-4 py-3 text-sm text-gray-900 outline-none transition focus:border-yellow-400 focus:bg-white focus:ring-4 focus:ring-yellow-100",
                "rows": 6,
                "placeholder": "Tell us briefly why you are a good fit for this role...",
            }),
        }

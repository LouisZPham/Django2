from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label='Email')
    
class EnrollmentForm(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=14)
    meets_requirements = forms.BooleanField(label='Meets requirements',required=False)
    notice = forms.BooleanField(label='Course available',required=True)
    
class AddCourseForm(forms.Form):
    pass
class EditCourseForm(forms.Form):
    pass
    
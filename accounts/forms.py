from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import ProjectDetail, Skill
from django.forms import ModelForm


from django import forms


class ProfileForm(ModelForm):
    pass


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectDetail
        fields = (
            'project_name',
            'mentor_name',
            'branch',
            'start_date',
            'paid',
            'description',
        )
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'start_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }

    def save(self, commit=True):
        project = super(ProjectForm, self).save(commit=False)
        project.project_name = self.cleaned_data['project_name']
        project.mentor_name = self.cleaned_data['mentor_name']
        project.branch = self.cleaned_data['branch']
        project.start_date = self.cleaned_data['start_date']
        project.paid = self.cleaned_data['paid']
        project.description = self.cleaned_data['description']

        if commit:
            project.save()

        return project


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
        # we can use exclude(....fields....) if we want to exclude attributes

"""
class SignUpForm(UserCreationForm):
    branch = forms.CharField(help_text="Your Branch")
    phone = forms.CharField(help_text="Your Phone Number")
    year = forms.CharField(help_text="Your Year OF Study")

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','branch', 'phone', 'year', 'password1', 'password2')
"""

class RegistrationForm(UserCreationForm):   # extending from superclass
    email = forms.EmailField(required=True)

    # define meta data

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False) # i might have left a loophole here
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('skill_name',)

    def save(self, commit=True):
        skills = super(SkillForm, self).save(commit=False)
        skills.project_name = self.cleaned_data['skill_name']

        if commit:
            skills.save()

        return skills

from django import forms
from stories.models import Story


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'story_text',
                  'nickname', 'anonymous', 'image')



from django.forms import ModelForm, inlineformset_factory

from .models import Profile, FamilyMember


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ()


class FamilyMemberForm(ModelForm):
    class Meta:
        model = FamilyMember
        exclude = ()


FamilyMemberFormSet = inlineformset_factory(Profile, FamilyMember,
                                            form=FamilyMemberForm, extra=1)

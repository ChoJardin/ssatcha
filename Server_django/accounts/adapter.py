from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


# many to many field 저장
def save_genres(user, genres):
    user = get_object_or_404(User, pk=user.pk)
    for genre in genres:
        user.like_genres.add(genre['id'])


# 회원가입 정보 저장
class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.nickname = data.get('nickname')
        user.save()
        # 회원 가입 단계에서 좋아요 누른 장르 연결
        save_genres(user, data.get('selected_genres', []))
        return user


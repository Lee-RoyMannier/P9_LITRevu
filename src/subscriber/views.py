from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from subscriber.forms import FollowingForm
from subscriber.models import UserFollows
from authentication.models import User


# Create your views here.
def follow_page(request):
    followers = UserFollows.objects.filter(user=request.user)
    followings = UserFollows.objects.filter(followed_by=request.user)
    msg = ""
    follow_form = FollowingForm()
    if request.method == 'POST':
        follow_form = FollowingForm(request.POST)
        if follow_form.is_valid():
            user = follow_form.cleaned_data.get('following')

            if user == request.user.username:
                msg = "Vous ne pouvez vous follow vous même"
            elif not User.objects.filter(username=user).exists():
                msg = "Username non trouvé"
            elif UserFollows.objects.filter(user=request.user, followed_by=User.objects.get(username=user)).exists():
                msg = "Vous suivez déjà cette personne"
            else:
                user_to_follow = User.objects.get(username=user)
                UserFollows.objects.create(user=request.user, followed_by=user_to_follow)

    context = {
        'follow_form': follow_form,
        'msg': msg,
        "followers": followers,
        "followings": followings
    }
    return render(request, 'subscriber/following_page.html', context=context)


class UnfollowUserView(LoginRequiredMixin, View):
    """
    Vue pour gérer le désabonnement d'un utilisateur suivi.
    """
    def post(self, request, user_id):
        followed_user = get_object_or_404(User, id=user_id)  # Récupère l'utilisateur suivi

        # Vérifie si la relation de suivi existe
        follow_relation = UserFollows.objects.filter(user=request.user, followed_by=followed_user).first()

        if follow_relation:
            follow_relation.delete()  # Supprime la relation de suivi

        return redirect("follow:follow")
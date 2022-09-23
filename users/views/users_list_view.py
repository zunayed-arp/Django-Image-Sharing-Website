from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ..models import Profile, FriendRequest
User = get_user_model()


def users_list(request):
    users = Profile.objects.exclude(user=request.user)
    sent_friend_requests = FriendRequest.objects.filter(from_user=request.user)
    my_friends = request.user.profile.friends.all() #reverse realations
    
    sent_to = []
    friends = []
    
    for user in my_friends:
        friend = user.friends.all()
        for f in friend:
            if f in friends:
                friend = friend.exclude(user=f.user)
        friends+=1
    for i in my_friends:
        if i in friends:
            pass

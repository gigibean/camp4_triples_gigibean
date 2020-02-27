from datetime import datetime
from django import forms
from django.forms.utils import ErrorList
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import *

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View


# Create your views here.
def profile(request, user_id):
        try:
            user = Users.objects.get(user_id=user_id)
            posts = Posts.objects.filter(users_idx=user.idx)
            # posts = qs.order_by('-id')
            track_posts = []
            for post in posts:
                track_post = TrackPost(track=post.track_idx, post=post, user=post.users_idx)
                track_posts.append(track_post)

            trackposts = enumerate(track_posts)
            return render(request, 'profile.html',
                          {'trackposts': trackposts, 'user':user})
        except ObjectDoesNotExist:
            print("Either the entry or track doesn't exist.")

    # posts = get_object_or_404(Posts, user_id=user_id)
    # user = get_object_or_404(Users, user_id=user_id)
    # Users = Users.objects.all()
    # user = Users.objects.get(user_id=user_id)
    # posts = Posts.objects.filter(users_idx=user.idx)
    # tracks = list(Tracks.objects.filter(users_idx=user.idx))
    # artist_names = Users.objects.filter(idx=user.idx).values_list('nickname', flat=True)
    # key = enumerate(tracks)
    # print(artist_names)
    # hashtags = []  # initiate
    # for post in posts:
    #     a = []
    #     if (post.tags):
    #         taglist = post.tags.split(' ')
    #         for tag in taglist:
    #             a.append("#" + tag)
    #
    #     hashtags.append(a)
    # print("여기보세요" , hashtags[0], hashtags[1])
    #
    # hashtags = enumerate(hashtags)
    #
    #
    # return render(request, 'profile.html', {'posts':posts, 'tracks':tracks, 'user':user, 'key':key, 'hashtags':hashtags,},)


def mr(request, user_id):
    # user = Users.objects.get(user_id=user_id)
    # posts = Posts.objects.filter(users_idx=user.idx)
    # tracks = list(Tracks.objects.filter(users_idx=user.idx))
    # artist_names = Users.objects.filter(idx=user.idx).values_list('nickname', flat=True)
    # key = enumerate(tracks)
    #
    # return render(request, 'profile.html',
    #               {'posts': posts, 'tracks': tracks, 'user': user, 'key': key, }, )
    try:
        user = Users.objects.get(user_id=user_id)
        posts = Posts.objects.filter(users_idx=user.idx)
        # posts = qs.order_by('-id')
        track_posts = []
        tps = []
        for post in posts:
            track_post = TrackPost(track=post.track_idx, post=post, user=post.users_idx)
            track_posts.append(track_post)
        for tp in track_posts:
            if tp.track.type_idx.name == 'MR':
                tps.append(tp)
        trackposts = enumerate(tps)

        return render(request, 'mr.html',
                      {'trackposts': trackposts, 'user':user})
    except ObjectDoesNotExist:
        print("Either the entry or track doesn't exist.")
    # return render(request, 'mr.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def songs(request, user_id):
    try:
        user = Users.objects.get(user_id=user_id)
        posts = Posts.objects.filter(users_idx=user.idx)
        # posts = qs.order_by('-id')
        track_posts = []
        tps = []
        for post in posts:
            track_post = TrackPost(track=post.track_idx, post=post, user=post.users_idx)
            track_posts.append(track_post)
        for tp in track_posts:
            if tp.track.type_idx.name == 'song':
                tps.append(tp)
        trackposts = enumerate(tps)

        return render(request, 'songs.html',
                      {'trackposts': trackposts, 'user':user})
    except ObjectDoesNotExist:
        print("Either the entry or track doesn't exist.")
    # return render(request, 'songs.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def likes(request, user_id):
    try:
        user = Users.objects.get(user_id=user_id)
        # posts = Posts.objects.filter(users_idx=user.idx)
        # posts = qs.order_by('-id')
        track_posts = []
        likes = Likes.objects.get_liked_posts(user.idx)
        # posts = Posts.objects.filter(idx__in=likes.posts_idx)
        for like in likes:
            post = like.posts_idx
            track_post = TrackPost(track=post.track_idx, post=post, user=post.users_idx)
            track_posts.append(track_post)


        trackposts = enumerate(track_posts)

        return render(request, 'likes.html',
                      {'trackposts': trackposts, 'user':user})
    except ObjectDoesNotExist:
        print("Either the entry or track doesn't exist.")
    # return render(request, 'likes.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def followings(request, user_id):
    try:
        user = Users.objects.get(user_id=user_id)
        # posts = Posts.objects.filter(users_idx=user.idx)
        # posts = qs.order_by('-id')
        users = []
        friends = Friends.objects.get_following_users(user.idx)
        # posts = Posts.objects.filter(idx__in=likes.posts_idx)
        for friend in friends:
            following_user = UserDisplaySmall(user=friend.receiver_idx)
            print("profile_pic is", following_user.profile_pic)
            users.append(following_user)
        users = enumerate(users)

        return render(request, 'followings.html',
                      {'users': users, 'user':user})
    except ObjectDoesNotExist:
        print("Either the entry or track doesn't exist.")
    # return render(request, 'followings.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def followers(request, user_id):
    try:
        user = Users.objects.get(user_id=user_id)
        # posts = Posts.objects.filter(users_idx=user.idx)
        # posts = qs.order_by('-id')
        users = []
        friends = Friends.objects.get_followers(user.idx)
        # posts = Posts.objects.filter(idx__in=likes.posts_idx)
        for friend in friends:
            following_user = UserDisplaySmall(user=friend.sender_idx)
            print("profile_pic is", following_user.profile_pic)
            users.append(following_user)
        users = enumerate(users)

        return render(request, 'followers.html',
                      {'users': users, 'user':user})
    except ObjectDoesNotExist:
        print("Either the entry or track doesn't exist.")
    # return render(request, 'followers.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def comments(request, user_id):
    return  render(request, 'comments.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def track_detail(request, user_id, post_id):
    return  render(request, 'track_detail.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})

def edit_post(request, user_id, post_id):
    return render(request, 'postupload.html')

def delete_post(request, user_id, post_id):
    return redirect('profile')

def post_comment(request, user_id, post_id):
    return redirect('track_detail')

def delete_comment(request, user_id, post_id, comment_id):
    return redirect('track_detail')
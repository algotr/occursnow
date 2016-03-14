__author__ = 'ali'

from django.core.cache import cache
from home.models import Post
from . import constants
from taggit.models import Tag
from django.contrib.auth.models import User


def get_user_posts(req_user):
    """
    :param req_user: The user that require his posts
    :return: posts list for the required user
    """
    user_posts_count = Post.objects.filter(user=req_user).count()
    user_posts_dict = cache.get('posts_user'+str(req_user.id))
    if user_posts_dict and user_posts_dict['user_posts_count'] == user_posts_count:
        return user_posts_dict['user_posts']
    else:
        posts_list = Post.objects.select_related().filter(user=req_user)
        user_posts_dict = {'user_posts': posts_list,
                           'user_posts_count': user_posts_count}
        cache.set('posts_user'+str(req_user.id), user_posts_dict, constants.CACHE_DURATION)
        return posts_list


def get_posts_buddies(user):
    """
    :param user: The user that require hist buddies posts
    :return: List of posts for the required user buddies that he follows
    """
    posts_buddies_count = Post.objects.filter(user__userprofile__in=user.userprofile.follows.all).count()
    posts_buddies_dict = cache.get('posts_buddies_user'+str(user.id))
    if posts_buddies_dict and posts_buddies_dict['posts_buddies_count'] == posts_buddies_count:
        return posts_buddies_dict['posts_buddies']
    else:
        posts_buddies = Post.objects.select_related().filter(user__userprofile__in=user.userprofile.follows.all)
        posts_buddies_dict = {'posts_buddies': posts_buddies,
                              'posts_buddies_count': posts_buddies_count}
        cache.set('posts_buddies_user'+str(user.id), posts_buddies_dict, constants.CACHE_DURATION)
        return posts_buddies


def get_public_posts():
    """
    :return: All posts for public page or guests
    """
    posts_count = Post.objects.count()
    posts_dict = cache.get('posts_dict')
    if posts_dict and posts_dict['posts_count'] == posts_count:
        return posts_dict['posts_list']
    else:
        posts_list = Post.objects.prefetch_related().all()
        posts_dict = {'posts_list': posts_list, 'posts_count': posts_count}
        cache.set('posts_dict', posts_dict, constants.CACHE_DURATION)
        return posts_list


def get_follows(user):
    """
    :param user: The user that we want to get his follows
    :return: A list of profiles that the user follows
    """
    follows_count = user.userprofile.follows.count()
    follows_dict = cache.get('follows_user'+str(user.id))
    if follows_dict and follows_dict['follows_count'] == follows_count:
        return follows_dict['follows_list']
    else:
        followings_list = user.userprofile.follows.select_related().all()
        follows_dict = {'follows_list': followings_list,
                        'follows_count': follows_count}
        cache.set('follows_user'+str(user.id), follows_dict, constants.CACHE_DURATION)
        return followings_list


def get_followed(user):
    """
    :param user: The user that we want to get who is followed him
    :return: A list of profiles for users followed this user
    """
    followed_count = user.userprofile.followed_by.count()
    followed_dict = cache.get('followed_user'+str(user.id))
    if followed_dict and followed_dict['followed_count'] == followed_count:
        return followed_dict['followed_list']
    else:
        followed_list = user.userprofile.followed_by.select_related().all()
        followed_dict = {'followed_list': followed_list,
                         'followed_count': followed_count}
        cache.set('followed_user'+str(user.id), followed_dict, constants.CACHE_DURATION)
        return followed_list


def get_posts_by_tag(tag_name):
    """
    :param tag_name: The tag name which we need to get posts in it
    :return: A list of posts under this tag_name
    """
    posts_count = Post.objects.filter(tags__name__in=[tag_name]).count()
    tag = Tag.objects.get(name=tag_name)
    tag_posts_dict = cache.get('posts_tag'+str(tag.id))
    if tag_posts_dict and tag_posts_dict['posts_count'] == posts_count:
        return tag_posts_dict['posts_list']
    else:
        posts_list = Post.objects.select_related().filter(tags__name__in=[tag_name])
        tag_posts_dict = {'posts_list': posts_list, 'posts_count': posts_count, 'tag_name': tag_name}
        cache.set('posts_tag'+str(tag.id), tag_posts_dict, constants.CACHE_DURATION)
        return posts_list


def authors_for(user):
    """
    :param user: The user that we need to get a list of authors he can follow
    :return: A list of users that this user can follow
    """
    authors_count = User.objects.exclude(username=user.username).count()

    cache_key = 'authors_except_user' + str(user.id)
    authors_dict = cache.get(cache_key)

    if authors_dict and authors_dict['authors_count'] == authors_count:
        return authors_dict['authors_list']
    else:
        authors_list = User.objects.select_related().exclude(username=user.username).order_by('username')
        authors_dict = {'authors_list': authors_list, 'authors_count': authors_count}
        cache.set(cache_key, authors_dict, constants.CACHE_DURATION)
        return authors_list

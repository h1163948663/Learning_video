from django import template
register = template.Library()
from apps.videos.models import Courese,ALLCoureslist

@register.filter()
@register.simple_tag()
def user_collect_style(courses_id, user):
    video = Courese.objects.get(pk=courses_id)
    collected = video.user_collected(user)
    if collected == 1:
        return "color: #ff5c5d"
    else:
        return "color: #777"

@register.filter()
@register.simple_tag()
def get_courses_tag_count(tag):
    print(tag)
    print(type(tag))
    video_count = Courese.objects.filter(tag=tag).all()
    return len(video_count)


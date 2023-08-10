from django import template

register = template.Library()
num = 0


@register.simple_tag()
def count_track_duration(albumtracks):
    counted_duration = 0
    for i in albumtracks:
        counted_duration += i.duration
    return counted_duration


@register.simple_tag()
def autonum():
    global num
    if num < 10:
        num += 1
        return f"0{num}"
    else:
        return num

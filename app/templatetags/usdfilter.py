from django import template

register=template.Library()

@register.filter()
def swap(value):
    return value.swapcase()

@register.filter()
def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg)]:
            c+=1
    return c

def remove(value,arg):
    return value.replace(arg,'')
register.filter('remove',remove)



 
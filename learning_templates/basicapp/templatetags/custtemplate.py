from django import template

newregister = template.Library()

@newregister.filter(name='cut')

def cuts(value,arg):
    return value.replace(arg,'')

# newregister.filter('cut',cuts)

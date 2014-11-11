from django.template import Template, Context
from django.conf import settings
settings.configure()

t = Template("My name is {{ person.first_name }}.")
class PersonClass3(object):
    """docstring for PersonClass3"""
    def first_name(self):
        raise AssertionError, "foo"

class SilentAssertionError(AssertionError):
    silent_variable_failure = True

class PersonClass4(object):
    """docstring for PersonClass4"""
    def first_name(self):
        raise SilentAssertionError

p = PersonClass4()
c = Context({'person': p})

#for name in ('John', 'Pat'):
print t.render(c)

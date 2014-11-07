# from django.template.loader import get_template
# from django.template import Template, Context
# from django.http import HttpResponse
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = get_template('current_datetime.html')
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)

from django.shortcuts import render_to_response
import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     return render_to_response('current_datetime.html', {'current_date': now})

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

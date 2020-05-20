from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from Pizza_site.celery import app
from blog.models import News
from blog.utils import func
from blog.models import Rate


@app.task
def change_cours():
    rates = func()
    for rate in rates:
        if Rate.objects.filter(name=rate['name']).exists():
            r = Rate.objects.filter(name=rate['name'])
            r.update(cours=rate['NBU'])
        else:
            r = Rate(name=rate['name'], cours=rate['NBU'])
            r.save()


REPORT_TEMPLATE = """
Number of total users  = {{ posts.count }}
Thank You for staying with us.
Sincierly,
"""


@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = News.objects.filter(author=user)
        if not posts:
            continue

        template = Template(home.html)

        send_mail(
            'Your Activity',
            template.render(context=Context({'posts': posts})),
            'Nurijusha@gmail.com',
            [user.email],
            fail_silently=False,
        )

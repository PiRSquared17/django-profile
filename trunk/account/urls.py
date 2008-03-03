from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template
from account.views import *
from django.contrib.auth import views

urlpatterns = patterns('',
    (r'^password/reset/$', reset_password, {'template' : 'account/password_reset.html'}),
    (r'^password/reset/done/$', direct_to_template, {'template': 'account/password_reset_done.html'}),
    (r'^password/change/(?P<key>.{70})/$', change_password_with_key, {'template': 'account/password_change.html'}),
    (r'^password/change/$', change_password_authenticated, {'template': 'account/password_change.html'}),
    (r'^password/change/done/$', direct_to_template, {'template': 'account/password_change_done.html'}),
    (r'^email/change/$', email_change, {'template': 'account/email_change.html'}),
    (r'^email/change/processed/$', direct_to_template, {'template': 'account/email_change_processed.html'}),
    (r'^email/change/(?P<key>.{70})/$', change_email_with_key, {'template': 'account/email_change_done.html'}),
    (r'^login/$', views.login, {'template_name': 'account/login.html'}),
    (r'^logout/$', logout, {'template': 'account/logout.html'}),
    (r'^check_user/(?P<user>.*)/$', check_user),
    (r'^check_email/(?P<email>.*)/$', check_email),
    (r'^check_email_unused/(?P<email>.*)/$', check_email_unused),

    # Profile
    ('^profile/$', redirect_to, {'url': '/profile/'}),

    # Registration
    (r'^register/$', register, {'template_name' : 'account/registration.html'}),
    (r'^register/complete/$', direct_to_template, {'template': 'account/registration_done.html'}),
)
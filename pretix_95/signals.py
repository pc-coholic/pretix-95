import pytz
from distutils.util import strtobool
from django.dispatch import receiver
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from pretix import settings
from pretix.control.signals import nav_topbar


@receiver(nav_topbar, dispatch_uid="pretix_95_nav_topbar")
def nav_topbar(sender, request=None, **kwargs):
    # This is duplicated in the nav_topbar signal as well as the context_processor
    # If this wasn't the case, the button would display the wrong text if we just
    # switched layout.
    if not settings.DEBUG and not 'staging.pretix.eu' in settings.SITE_URL and now().astimezone(
            pytz.timezone('Europe/Berlin')).date().isoformat() != '2021-04-01':
        return ''

    if request.GET.get('pretix95', None):
        try:
            request.session['pretix95'] = strtobool(request.GET.get('pretix95'))
        except ValueError:
            pass

    if request.session.get('pretix95', True):
        return [{
            'label': _('What is this?!'),
            'url': 'https://www.pretix.eu/about/{}/social/doodles/'.format(
                'de' if 'de' in request.LANGUAGE_CODE else 'en'
            ),
        }, {
            'label': _('Switch back to classic pretix'),
            'url': '?pretix95=off',
        }]
    else:
        return [{
            'label': _('Switch back to pretix95'),
            'url': '?pretix95=on',
        }]

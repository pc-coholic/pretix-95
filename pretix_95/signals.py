from distutils.util import strtobool
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from pretix.control.signals import nav_topbar


@receiver(nav_topbar, dispatch_uid="pretix_95_nav_topbar")
def nav_topbar(sender, request=None, **kwargs):
    # This is duplicated in the nav_topbar signal as well as the context_processor
    # If this wasn't the case, the button would display the wrong text if we just
    # switched layout.
    if request.GET.get('pretix95', None):
        try:
            request.session['pretix95'] = strtobool(request.GET.get('pretix95'))
        except ValueError:
            pass

    if request.session.get('pretix95', True):
        return [{
            'label': _('Switch back to classic pretix'),
            'url': '?pretix95=off',
        }]
    else:
        return [{
            'label': _('Switch back to pretix95'),
            'url': '?pretix95=on',
        }]

import pytz
from distutils.util import strtobool
from django.conf import settings
from django.template.loader import get_template
from django.utils.timezone import now
from pretix.control.signals import html_head


def contextprocessor(request):
    ctx = {}
    if not settings.DEBUG and not 'staging.pretix.eu' in settings.SITE_URL and now().astimezone(pytz.timezone('Europe/Berlin')).date().isoformat() != '2021-04-01':
        return ctx

    if request.path.startswith('/control/'):
        _html_head = []
        template = get_template('pretix_95/control_head.html')
        if request.GET.get('pretix95', None):
            try:
                request.session['pretix95'] = strtobool(request.GET.get('pretix95'))
            except ValueError:
                pass

        if request.session.get('pretix95', True):
            if hasattr(request, 'event') and request.user.is_authenticated:
                for receiver, response in html_head.send(request.event, request=request):
                    _html_head.append(response)

            _html_head.append(template.render({}))

            ctx['html_head'] = "".join(_html_head)

    return ctx

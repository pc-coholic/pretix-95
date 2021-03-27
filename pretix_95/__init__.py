import os
import pytz
from django.utils.timezone import now
from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = '1.0.0'


class PluginApp(PluginConfig):
    name = 'pretix_95'
    verbose_name = 'pretix95'

    class PretixPluginMeta:
        name = gettext_lazy('pretix95')
        author = 'Martin Gross'
        description = gettext_lazy('Bring the glory of Windows 95 to your pretix installation!')
        visible = False
        version = __version__
        category = 'CUSTOMIZATION'
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from django.conf import settings

        from . import signals  # NOQA
        if not settings.DEBUG and not 'staging.pretix.eu' in settings.SITE_URL and now().astimezone(
                pytz.timezone('Europe/Berlin')).date().isoformat() != '2019-04-01':
            return

        # Yes. Seriously. Sorry, not sorry.
        settings.TEMPLATES[0]['OPTIONS']['context_processors'].append('pretix_95.context.contextprocessor')
        settings.TEMPLATES[0]['DIRS'].insert(0, os.path.join(os.path.dirname(__file__), 'templates'))
        settings.STATICFILES_DIRS.insert(0, os.path.join(os.path.dirname(__file__), 'static'))


default_app_config = 'pretix_95.PluginApp'

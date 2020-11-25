pretix95
==========================

This is a plugin for `pretix`_. 

Bring the glory of Windows 95 to your pretix installation!

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/pretix-95``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.

Acknowledgements
----------------
- `litheory's Bootstrap Theme：Win95`_
- `Leo Leontev's Windows 95 Sans Serif TTF`_

License
-------


Copyright 2020 Martin Gross

Released under the terms of the Apache License 2.0



.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
.. _litheory's Bootstrap Theme：Win95: https://litheory.github.io/bootstrap-theme-Win95/demo.html
.. _Leo Leontev's Windows 95 Sans Serif TTF: https://stackoverflow.com/a/54023769

This is a CKAN extension that aims to remove all traces of CKAN's groups
feature from CKAN's web interface. It's useful for sites that don't use groups
and so don't want this feature showing up on their pages.

So far not all signs of the groups feature are hidden, only some of the most
obvious ones (eg. the groups link in the main navigation header, and the groups
facet box on the search page).

To install, activate your CKAN virtualenv then run:

    pip install -e 'git+https://github.com/whiskyechobravo/ckanext-hidegroups.git#egg=ckanext-hidegroups'

Then add the plugin to your CKAN config file (e.g. `development.ini` or
`production.ini`), for example:

  ckan.plugins = stats text_preview recline_preview hidegroups

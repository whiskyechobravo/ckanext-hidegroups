from setuptools import setup, find_packages

setup(
    name='ckanext-hidegroups',
    version='0.2',
    description="A CKAN 2 plugin that hides the groups feature from the web interface",
    long_description="""""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='''CKAN''',
    author='Sean Hammond, Bart Saelen, David Lesieur',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        hidegroups=ckanext.hidegroups.plugin:HideGroupsPlugin
    ''',
)

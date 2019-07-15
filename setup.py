from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-hidegroups',
    version=version,
    description="A CKAN 2 plugin that hides the groups feature from the web interface",
    long_description="""""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Sean Hammond, Bart Saelen',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.hidegroups'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points= \
    """
        [ckan.plugins]
        # Add plugins here, eg
        hidegroups=ckanext.hidegroups.plugin:HideGroupsPlugin
    """,
)

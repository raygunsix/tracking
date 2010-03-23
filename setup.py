try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='tracking',
    description='web spider tracking application',
    author='',
    author_email='administrator@suite101.com',
    url='',
    install_requires=[
        "Pylons<=0.9.7",
        "SQLAlchemy<=0.5.8",
        "Fixture<=1.3.1",
        "Boto",
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'tracking': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'tracking': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = tracking.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)

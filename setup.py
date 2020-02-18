from distutils.core import setup
import wordpress

long_description = open('README.rst').read()

setup(
    name='the-real-django-wordpress-py3',
    version=wordpress.__version__,
    description='Django models and views for a WordPress database (Django 1.11 or later).',
    long_description=long_description,
    author='Alexej Starschenko',
    author_email='alexej@2e2a.de',
    url='http://github.com/2e2a/django-wordpress/',
    packages=['wordpress'],
    package_data={'wordpress': ['templates/wordpress/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
    license='BSD License',
    platforms=["any"],
)

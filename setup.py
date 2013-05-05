from setuptools import setup, find_packages

setup(name="django-post-syncdb-hooks",
      version='0.1.0',
      url='https://github.com/podshumok/django-post-syncdb-hooks',
      description='Lets you to run SQL after django syncdb',
      packages=find_packages(),
      zip_safe=True,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: SQL',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Public Domain',
        ],
)

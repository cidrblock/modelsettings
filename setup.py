from setuptools import setup

setup(name='modelsettings',
      version='1.6.3',
      description='Model your application settings.',
      url='http://github.com/cidrblock/modelsettings',
      author='Bradley A. Thornton',
      author_email='brad@thethorntons.net',
      license='MIT',
      packages=[
        'modelsettings'
      ],
      install_requires=[
          'envparse',
          'pyyaml'
      ],
      zip_safe=False)

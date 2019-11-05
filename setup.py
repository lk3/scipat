from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='scipat',
      version='1.0.0',
      description='Generates dataset from USPTO patent records',
      url='https://github.com/lk3/scipat',
      author='Luciano Kay',
      author_email='luciano@kay.com.ar',
      license='GNU GPLv3',
      classifiers=[''],
      keywords=[''],
      packages=['scipat'],
      install_requires=['bs4', 'requests', 'pandas', 'selenium'],
      python_requires='>=3',
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown')
from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.31'

setup(name='snowpark_extensions',
      version=VERSION,
      description='A set of helpers to extend snowpark functionality',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/MobilizeNet/snowpark-extensions-py',
      author='mauricio.rojas',
      install_requires=['snowflake-snowpark-python[pandas]==1.5.1', 
                        'nest_asyncio', 'jinja2', 'rich'],
      author_email='mauricio.rojas@mobilize.net',
      packages=['snowpark_extensions'],
      zip_safe=False)

import os
from setuptools import setup


setup(
    name = "DateRangeParser",
    packages = ['daterangeparser'],
    install_requires = ['pyparsing'],
    version = "1.3.2",
    author = "Robin Wilson",
    author_email = "robin@rtwilson.com",
    description = ("""Module to parse human-style date ranges (eg. 15th-19th March 2011) to datetimes"""),
    license = "LGPL",
    test_suite = "nose.collector",
    tests_require=['nose'],
    url = "https://github.com/robintw/daterangeparser",
    long_description="""DateRangeParser is a Python module which makes it easy to parse date ranges specified in
    a human-style string. For example, it can parse strings like:
      - 27th-29th June 2010
      - 30 May to 9th Aug
      - 3rd Jan 1980 -- 2nd Jan 2013
      - Wed 23 Jan -> Sat 16 February 2013
      - Tuesday 29 May - Sat 2 June 2012
      - From 1 to 9 Jul
      - 14th July 1988 *(it works with single dates too!)*
      - 07:00 Tue 7th June - 17th July 3:30pm *(it ignores times, currently)*
      - Jan 2011 - Mar 2014
    DateRangeParser can be installed by running ``pip install daterangeparser``.
    Full documentation is provided at http://daterangeparser.readthedocs.org/ and the code (and development information)
    is available at https://github.com/robintw/daterangeparser.""",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2"],
)
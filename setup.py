import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.handover',
      version='0.1',
      description=('Scripts to manage process of handing over apps to clients for production use'),
      long_description='# Handover\r\n\r\nThis package contains scripts to manage the process of handing over student applications to clients.\r\n\r\nAt the time I wrote this README, this package does the following:\r\n\r\n- It accepts an Excel spreadsheet containing client data, being, first name, last name, email address, name of the application, link to the application as it is installed on the Flinders docassemble server, a flag indicating whether a signed license agreement has been received.\r\n- It prepares a kick-off email to be sent to each client listed in the spreadsheet. The kick-off email will contain a link to another interview in this package which will enable the client to confirm whether they wish to commission the application.\r\n- This second interview is used to record whether a client wishes to commission or not commission, if not commission them whether they wish to continue working with us, if they do wish to commission that instructions for next steps.\r\n- This package contains a word template which will be used as a pro forma application review form, as stated in the formal handover document (which is not part of this package) which is sent to clients',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://flinders.edu.au',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['pandas'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/handover/', package='docassemble.handover'),
     )


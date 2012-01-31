from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import os
import cython_gsl

gsl_include = os.popen('gsl-config --cflags').read()[2:-1]

if gsl_include == '':
    print "Couldn't find gsl-config. Make sure it's installed and in the path."
    import sys
    sys.exit(-1)

setup(
    name="integrate",
    version="0.1",
    author="Thomas V. Wiecki",
    author_email="thomas_wiecki@brown.edu",
    url="http://github.com/twiecki/CythonGSL",
    description="CythonGSL example integrate.",
    install_requires=['NumPy >=1.3.0'],
    setup_requires=['NumPy >=1.3.0'],
    include_dirs = [np.get_include(), gsl_include],
    cmdclass = {'build_ext': build_ext},
    classifiers=[
                'Development Status :: 3 - Alpha',
                'Environment :: Console',
                'Operating System :: OS Independent',
                'Intended Audience :: Science/Research',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering',
                 ],
    ext_modules = [Extension("integrate", ["integrate.pyx"], libraries=['gsl','gslcblas'], cython_include_dirs=cython_gsl.__path__)]
)

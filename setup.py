from distutils.core import setup

setup(
    name='swapy',
    version='0.1',
    description='Web micro framework built for APIs',
    author='Daniel Däschle',
    author_email='daniel.daeschle@gmail.com',
    url='https://github.com/danieldaeschle/swapy',
    packages=['swapy'],
    install_requires=['werkzeug']
)
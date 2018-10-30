from setuptools import setup

setup(
    name='gnip',
    version='0.1',
    py_modules=['gnip'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gnip=gnip.cli.train:cli
    ''',
)
from setuptools import setup

setup(
    name='nergal',
    version='0.1.0',
    py_modules=['__main__'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            '__main__ = nergal.__main__:single',
        ],
    },
)
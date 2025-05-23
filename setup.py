from setuptools import setup

setup(
    name='file-organizer',
    version='1.0.0',
    py_modules=['organize'],
    install_requires=["python-dotenv==1.1.0"],
    entry_points={
        'console_scripts': [
            'organize-folder=organize:main',
        ],
    },
)

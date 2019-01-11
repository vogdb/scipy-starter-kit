from setuptools import setup

setup(
    name='scipy-starter-kit',
    version='0.0.1',
    description='Python Scipy Starter Kit for a quick start of your project',
    url='https://github.com/vogdb/scipy-starter-kit/',
    license='MIT',
    install_requires=['scipy'],
    python_requires='>3.5',
    packages=['your_project_name'],
    package_dir={'your_project_name': 'your_project_name'},
    package_data={'your_project_name': ['data']},
)

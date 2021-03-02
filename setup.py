from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name=locker_project,
    version='0.0.1',
    description='Implementation locker to Azure DevOps.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    url='',
    author='Daniel Simanjuntak',
    author_email='daniel.smnjuntak@gmail.com',
    keywords='Configuration on Azure DevOps',
    license='MIT',
    packages=['locker_project'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
from setuptools import setup, find_packages

setup(
    name='jdxonv',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
    entry_points={
        'console_scripts': [
            # list any console scripts provided by your package here
        ]
    },
    author='Your Name',
    author_email='youremail@example.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jdgod/jdxonv',
    license='GPL',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.9',
    ],
)

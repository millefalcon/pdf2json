from setuptools import setup

setup(
    name='pdf2json',
    version='0.1.0-dev',
    author='Hanish K H',
    author_email='hanish0019@gmail.com',
    py_modules=['pdf2json'],
    data_files=[('test_data', ['data/Interview_sample_data.pdf'])],
    install_requires=['pdfminer.six==20200726'],
    entry_points={
        'console_scripts': [
            'pdf2json = pdf2json:main'
            ],
    }
)


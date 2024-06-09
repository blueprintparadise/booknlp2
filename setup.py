from setuptools import setup, find_packages

setup(name='booknlp2', 
	version='1.0', 
	packages=find_packages(),
	py_modules=['booknlp2'],
	url="https://github.com/blueprintparadise/booknlp2",
	author="Rushikesh Hiray",
	author_email="rhiray03@gmail.com",
	include_package_data=True, 
	license="MIT",
	install_requires=['torch>=1.7.1',
					  'tensorflow>=1.15',
					  'spacy>=3',
                      'transformers==4.11.3'
                      ],

	)

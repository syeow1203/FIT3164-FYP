from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
        package_data={
        'mypackage': ['data/model.pkl'],
    },
    include_package_data=True,
    description='A simple prediction package',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "joblib"
    ],
    
    python_requires='>=3.6',
    author='Yeow Shiau Yen',
    author_email='syeo0021@student.monash.edu'
)

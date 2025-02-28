from setuptools import setup, find_packages
from typing import List

e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [i.replace('\n','') for i in requirements]
        if e_dot in requirements:
            requirements.remove(e_dot)

    return requirements


setup(
name='my_first_ml_project',
version='0.1',
author='arjun',
author_email= 'arjun569@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),




)
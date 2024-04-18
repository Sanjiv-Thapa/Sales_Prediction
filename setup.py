from setuptools import find_packages,setup
from typing import List

hyphen_e = '-e .'
def get_requirement(file_path:str)->list[str]:
    '''
    return the list of requirement
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements


setup(
    name ='sales_prediction',
    version='0.0.1',
    author='sanjiv',
    author_email='sanjivthapa40@gmail.com',
    packages= find_packages(),
    install_requires = get_requirement('requirements.txt')

)
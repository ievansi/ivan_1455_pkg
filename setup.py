from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ivan_1455_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch','*.py*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='igsp-01',
    maintainer_email='ilamajorov365@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'even_number_publisher = ivan_1455_pkg.even_number_publisher:main',
            'overflow_listener = ivan_1455_pkg.overflow_listener:main',
        ],
    },
)

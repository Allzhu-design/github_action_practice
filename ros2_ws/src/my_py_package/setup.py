from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_py_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 包含所有 launch 文件
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # 包含所有 config 文件
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A simple ROS2 Python package with config files',
    license='Apache-2.0',
    extras_require={
    'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'talker = my_py_package.talker:main',
            'listener = my_py_package.listener:main',
        ],
    },
)
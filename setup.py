from setuptools import find_packages, setup

package_name = 'service_calculatrice'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lagab-maria',
    maintainer_email='marialagab2174@gmail.com',
    description='Challenge 2 ROS 2 - Service Calculatrice',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'calculette = service_calculatrice.calculette_node:main'
        ],
    },
)

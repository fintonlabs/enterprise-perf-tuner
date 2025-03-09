from setuptools import setup, find_packages

setup(
    name='PerformanceMonitor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask==1.1.2',
        'psutil==5.8.0',
        'jsonify==0.5',
    ],
    entry_points={
        'console_scripts': [
            'performancemonitor=performancemonitor:main',
        ],
    },
)
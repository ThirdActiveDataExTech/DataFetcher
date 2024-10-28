from setuptools import setup, find_packages

setup(
    name='DataFetcher',
    version='0.1.0',
    author='EunmiGo',
    author_email='@example.com',
    description='Airflow test',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
    ],
    python_requires='>=3.9',  # 최소 Python 버전
)
from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'matplotlib',
        # 다른 필요한 패키지들을 여기에 추가합니다
    ],
)
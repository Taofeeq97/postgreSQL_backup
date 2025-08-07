from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-db-s3-backup",
    version="2.0.8",
    author="Otu Taofeeq",
    author_email="otutaofeeq@gmail.com",
    description="Django database backup with S3 storage and scheduling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-db-s3-backup",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Django>=3.2",
        "boto3>=1.26.0",
        "django-apscheduler>=0.6.2",
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-django>=4.5.0',
            'coverage>=6.0',
        ],
    },
    keywords="django database backup s3_access",
)
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
        name="highchartexport",
        version="0.0.3",
        url="https://github.com/jitendra29mishra/highchartexport",
        description="Python package that convert highchart configuration into image file",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Jitendra Mishra",
        author_email="jitendra29mishra@gmail.com",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Utilities",
            ],
        keywords="Highchart Visualization Chart Map",
        packages=find_packages(),
        install_requires=["requests>=2"],
        entry_points={
            'console_scripts': [
                'highchartexport=highchartexport.__main__:main'
                ]
            },
        python_requires=">=3.6",
        zip_safe=False
        )

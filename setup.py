from setuptools import setup, find_packages

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
        name="highchartexport",
        version="1.0.0",
        description="Python package that convert highchart configuration into image file",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Jitendra Mishra",
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Apprived :: MIT License"],
        keywords="Highchart Visualization Chart Map",
        packages=find_packages("highchartexport"),
        install_requires=["requests>=2"],
        entry_points={
            'console_scripts': [
                'highchartexport=highchartexport.__main__:main'
                ]
            },
        python_requires=">=3.6"
        )

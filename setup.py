from setuptools import setup, find_packages

setup(
    name="quant-trading",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'scipy',
        'statsmodels',
        'yfinance',
        'quantlib',
        'ta-lib',
        'requests',
    ],
    author="KRISH RM",
    author_email="krish-rm@example.com",
    description="Quantitative Trading Tools for Equity, Derivatives, and Commodities Markets",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/quant-trading",  # Replace with your actual GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

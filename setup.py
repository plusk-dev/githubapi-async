from setuptools import setup

setup(
    name="githubapi-async",
    version="0.0.1",
    description="An (unofficial) asynchronous API Wrapper for interactions with the GitHub API v3",
    url="https://github.com/YuvrajGeek/githubapi-async",
    author="Yuvraj M.",
    author_email="yuvrajmotiramani5115@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
    ],
    install_requires=["aiohttp"],
    python_requires='>=3.5',
)

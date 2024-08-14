from setuptools import find_packages, setup

setup(
    name="langchain-altero",
    version="0.0.1",
    description="LangChain Helper Library",
    author="Dicky Umardhani",
    author_email="dicky@alterolab.com",
    url="https://github.com/cakeplabs/langchain-altero",
    install_requires=[
        "langchain",
        "kiwipiepy",
        "konlpy",
        "rank_bm25",
        "pinecone-client[grpc]",
        "pinecone-text",
        "olefile",
        "pdf2image",
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        "langchain",
        "altero",
    ],
    python_requires=">=3.10",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

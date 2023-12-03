from setuptools import setup, find_packages

setup(
    name="mdx23",
    py_modules=["mdx23"],
    version="0.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    # 其他相关信息，如作者，授权，描述等
)

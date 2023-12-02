from setuptools import setup, find_packages

setup(
    name="mvsep_mdx23_colab_v2",
    version="0.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    # 其他相关信息，如作者，授权，描述等
)

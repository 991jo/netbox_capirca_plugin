from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='netbox_capirca_plugin',
    version="2.0.0",
    packages=find_packages(),
    url='https://github.com/991jo/netbox_capirca_plugin',
    author='Johannes Erwerle',
    author_email='jo@swagsapce.org',
    description='A netbox plugin to manage ACLs with capirca',
    include_package_data=True,
    zip_safe=False,
    long_description=readme,
    install_requires=[
        "capirca",
        "jinja2",
        "netbox-plugin-extensions>=1.1.0",
        "importlib",
        ],
    long_description_content_type="text/markdown",
)

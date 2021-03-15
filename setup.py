from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='netbox_acl_plugin',
    version="0.1.2",
    packages=find_packages(),
    url='https://git.belwue.de/ip/belwue_services',
    author='Johannes Erwerle',
    author_email='erwerle@belwue.de',
    description='A netbox Plugin to add simple ACL management',
    include_package_data=True,
    zip_safe=False,
    long_description=readme,
    install_requires=[]
)

import pkg_resources

# Get a list of installed packages and their versions
installed_packages = [(package.key, package.version) for package in pkg_resources.working_set]

# Print the list of installed packages
print(installed_packages)

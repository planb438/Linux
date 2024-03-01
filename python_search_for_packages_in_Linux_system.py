import apt

def search_packages(keyword):
    # Initialize the apt cache
    cache = apt.Cache()

    # Update package lists
    cache.update()

    # Search for packages containing the keyword
    packages = []
    for package in cache:
        if keyword.lower() in package.name.lower():
            packages.append(package)

    return packages

def main():
    keyword = input("Enter the keyword to search for packages: ")
    print("Searching for packages containing '{}'...".format(keyword))
    found_packages = search_packages(keyword)

    if found_packages:
        print("Found packages:")
        for package in found_packages:
            print("- {} ({})".format(package.name, package.installed.version if package.is_installed else "Not installed"))
    else:
        print("No packages found containing '{}'".format(keyword))

if __name__ == "__main__":
    main()

from os import system, remove as rm
import json

class AtomPackageManager(object):
    def __init__(self):
        self.installed_files = None

    @property
    def installed(self):
        if self.installed_files is None:
            self.installed_files = self.get_installed()

        return self.installed_files

    def get_installed(self):
        installed_files_path = "installed.txt"
        system("apm list --bare > {f}".format(installed_files_path))

        with open(f) as f:
            installed = f.read().split()
        return [p.split("@@")[0] for p in installed]

    def install(self, package):
        try:
            package, extra_cmd = package
        except:
            package, extra_cmd = package, None

        system("apm install {pkg}".format(pkg=package))

        if extra_cmd is not None:
            system(extra_cmd)

if __name__ == "__main__":
    with open("atom-packages.json", "r") as f:
        packages = json.loads(f.read())['packages']

    manager = AtomPackageManager()

    for p in packages:
        manager.install(p)

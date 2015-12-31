def uninstall(distro, purge=False):
    packages = [
        'ceph',
        ]
    extra_remove_flags = []
    distro.packager.remove(
        packages,
        extra_remove_flags=extra_remove_flags
    )

import mon  # noqa
from install import install, mirror_install, repo_install  # noqa
from uninstall import uninstall  # noqa
from ceph_deploy.util import pkg_managers

# Allow to set some information about this distro
#

distro = None
release = None
codename = None


def choose_init(module):
    """
    Select a init system

    Returns the name of a init system (upstart, sysvinit ...).
    """
    return 'systemd'


def get_packager(module):
    return pkg_managers.Pacman(module)

from urlparse import urlparse

from ceph_deploy.hosts.common import map_components


NON_SPLIT_COMPONENTS = ['ceph']


def install(distro, version_kind, version, adjust_repos, **kw):
    packages = map_components(
        NON_SPLIT_COMPONENTS,
        kw.pop('components', [])
    )
    codename = distro.codename
    machine = distro.machine_type

    if packages:
        distro.packager.install(packages)


def mirror_install(distro, repo_url, gpg_url, adjust_repos, **kw):
    install(distro, "", "", "", )


def repo_install(distro, repo_name, baseurl, gpgkey, **kw):
    install(distro, "", "", "", )

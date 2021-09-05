# RPM files for Storj

[![Copr build status](https://copr.fedorainfracloud.org/coprs/jonny/Storj/package/storj/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jonny/Storj/package/storj/)

Built on Fedora Copr at https://copr.fedorainfracloud.org/coprs/jonny/Storj/

## How to build the RPM locally

Make srpm:
```
$ make -f .copr/Makefile srpm outdir=. spec=/home/jonny/projects/storj-rpms/storj.spec
```

Make rpm:
```
$ mock --rebuild --enable-network ./storj-${VERSION}.src.rpm
```

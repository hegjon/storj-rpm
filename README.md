# RPM files for Storj

[![Copr build status](https://copr.fedorainfracloud.org/coprs/jonny/Storj/package/storj-storagenode/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jonny/Storj/package/storj-storagenode/)

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

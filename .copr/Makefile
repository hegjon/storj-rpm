srpm:
		mkdir SOURCES
		cp storagenode/* SOURCES

		dnf install -y rpmdevtools rpm-build
		spectool -g -C SOURCES storj-storagenode.spec

		rpmbuild -bs storj-storagenode.spec --define "_sourcedir SOURCES" --define "_srcrpmdir $(outdir)"

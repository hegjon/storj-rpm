srpm:
		mkdir SOURCES
		cp -v storagenode/* SOURCES

		dnf install -y rpmdevtools rpm-build
		spectool -g -C SOURCES storj-storagenode.spec

		rpmbuild -bs $(spec) --define "_sourcedir SOURCES" --define "_srcrpmdir $(outdir)"

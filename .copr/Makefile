NAME = storagenode

srpm: /usr/bin/spectool
	mkdir -p SOURCES

	NAME=storagenode
	cp -v ${NAME}/* SOURCES
	spectool -g -C SOURCES ${spec}

	rpmbuild -bs ${spec} --define "_sourcedir SOURCES" --define "_srcrpmdir $(outdir)"

/usr/bin/spectool:
	dnf install -y rpmdevtools

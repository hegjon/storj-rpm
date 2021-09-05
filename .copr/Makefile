srpm: /usr/bin/spectool
	spectool -g -C sources ${spec}

	rpmbuild -bs ${spec} --define "_sourcedir sources" --define "_srcrpmdir $(outdir)"

/usr/bin/spectool:
	dnf install -y rpmdevtools

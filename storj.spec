%global debug_package %{nil}
%global _build_id_links none

Name:    storj
Version: 1.67.3
Release: 1%{?dist}
Summary: Storj is building a decentralized cloud storage network

License: AGPLv3
URL:     https://storj.io/

Source0:  https://github.com/storj/storj/archive/refs/tags/v%{version}.tar.gz

Source2: storj-storagenode.conf

Source11: storj-storagenode@.service
Source12: storj-storagenode-setup@.service

Source21: storj-identity-create@.service

BuildRequires: go
BuildRequires: git

BuildRequires: npm
BuildRequires: unzip

%if 0%{?mageia} > 0
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%{?systemd_requires}

%global _description %{expand:
Storj is an S3-compatible platform and suite of decentralized applications that
allows you to store data in a secure and decentralized manner. Your files are
encrypted, broken into little pieces and stored in a global decentralized
network of computers. Luckily, we also support allowing you (and only you) to
retrieve those files!
}

%description %_description


%package storagenode
Summary: Storj Storage Node
Requires: storj-identity

%description storagenode %_description

%package identity
Summary: Storj Identity

%description identity %_description

%package uplink
Summary: Storj Uplink

%description uplink %_description


%prep
%setup -n storj-%{version}
cp %{SOURCE2} .


%build
export GOPATH="$(pwd)/.godeps"
go install -v ./cmd/{storagenode,identity,uplink}

#web console
cd web/storagenode
npm ci
npm run build

%install
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 .godeps/bin/storagenode %{buildroot}%{_bindir}/storagenode
install -m 755 .godeps/bin/identity %{buildroot}%{_bindir}/identity
install -m 755 .godeps/bin/uplink  %{buildroot}%{_bindir}/uplink


install -dD -m 755 %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/
install -p -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/

install -dD -m 0750 %{buildroot}%{_sharedstatedir}/storj-storagenode


install -dD -m 0750 %{buildroot}%{_sysconfdir}/storj-storagenode

#web console
install -dD -m755 %{buildroot}%{_datadir}/storj-storagenode
cp -a web/storagenode/dist %{buildroot}%{_datadir}/storj-storagenode/

%pre storagenode
getent group storj-storagenode >/dev/null || groupadd -r storj-storagenode
getent passwd storj-storagenode >/dev/null || \
  useradd -r -g storj-storagenode -s /sbin/nologin \
    -d %{_sharedstatedir}/storj-storagenode \
    -c 'Storj Storage Node' storj-storagenode
exit 0


%post storagenode
%systemd_post storj-storagenode@.service

%preun storagenode
%systemd_preun storj-storagenode@.service

%postun storagenode
%systemd_postun_with_restart storj-storagenode@\*.service

%files storagenode
%doc storj-storagenode.conf
%config %dir %attr(-,-,storj-storagenode) %{_sysconfdir}/storj-storagenode
%{_bindir}/storagenode
%{_unitdir}/storj-storagenode@.service
%{_unitdir}/storj-storagenode-setup@.service
%{_unitdir}/storj-identity-create@.service
%attr(0770,storj-storagenode,storj-storagenode) %{_sharedstatedir}/storj-storagenode
%{_datadir}/storj-storagenode

%files identity
%{_bindir}/identity

%files uplink
%{_bindir}/uplink

%changelog
* Sun Nov 27 2022 Jonny Heggheim <hegjon@gmail.com> - 1.67.3-1
- Updated to version 1.67.3

* Sun Nov 13 2022 Jonny Heggheim <hegjon@gmail.com> - 1.66.1-1
- Updated to version 1.66.1

* Fri Oct 14 2022 Jonny Heggheim <hegjon@gmail.com>
- Updated to version 1.65.1

* Fri Oct 07 2022 Jonny Heggheim <hegjon@gmail.com> - 1.64.1-2
- Added uplink sub-package

* Sun Oct 02 2022 Jonny Heggheim <hegjon@gmail.com> - 1.64.1-1
- Updated to version 1.64.1

* Sun Sep 11 2022 Jonny Heggheim <hegjon@gmail.com> - 1.63.1-1
- Updated to version 1.63.1

* Sun Sep 04 2022 Jonny Heggheim <hegjon@gmail.com> - 1.62.3-1
- Updated to version 1.62.3

* Sat Aug 27 2022 Jonny Heggheim <hegjon@gmail.com> - 1.61.3-1
- Updated to version 1.61.3

* Wed Aug 10 2022 Jonny Heggheim <hegjon@gmail.com> - 1.61.1-1
- Updated to version 1.61.1

* Sun Jul 10 2022 Jonny Heggheim <hegjon@gmail.com> - 1.58.2-1
- Updated to version 1.58.2

* Wed Jun 22 2022 Jonny Heggheim <hegjon@gmail.com> - 1.56.4-1
- Updated to version 1.56.4

* Thu Jun 02 2022 Jonny Heggheim <hegjon@gmail.com> - 1.56.3-1
- Updated to version 1.56.3

* Thu May 19 2022 Jonny Heggheim <hegjon@gmail.com> - 1.55.1-1
- Updated to version 1.55.1

* Sun Apr 24 2022 Jonny Heggheim <hegjon@gmail.com> - 1.53.1-1
- Updated to version 1.53.1

* Sun Apr 10 2022 Jonny Heggheim <hegjon@gmail.com> - 1.52.2-1
- Updated to version 1.52.2

* Sat Mar 19 2022 Jonny Heggheim <hegjon@gmail.com> - 1.50.4-1
- Updated to version 1.50.4

* Thu Mar 10 2022 Jonny Heggheim <hegjon@gmail.com> - 1.49.5-1
- Updated to version 1.49.5

* Fri Feb 25 2022 Jonny Heggheim <hegjon@gmail.com> - 1.49.3-1
- Updated to version 1.49.3

* Thu Jan 13 2022 Jonny Heggheim <hegjon@gmail.com> - 1.46.3-1
- Updated to version 1.46.3

* Tue Dec 14 2021 Jonny Heggheim <hegjon@gmail.com> - 1.45.3-1
- Updated to version 1.45.3

* Wed Dec 01 2021 Jonny Heggheim <hegjon@gmail.com> - 1.44.1-1
- Updated to version 1.44.1

* Tue Nov 23 2021 Jonny Heggheim <hegjon@gmail.com> - 1.43.1-1
- Updated to version 1.43.1

* Thu Oct 14 2021 Jonny Heggheim <hegjon@gmail.com> - 1.40.4-1
- Updated to version 1.40.4

* Mon Oct 04 2021 Jonny Heggheim <hegjon@gmail.com> - 1.39.5-1
- Updated to version 1.39.5

* Sun Sep 19 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-7
- storj-storagenode-setup requires storj-identity-create

* Sun Sep 05 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-6
- storj-storagenode requires storj-identity

* Sun Sep 05 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-5
- Added storj-identity

* Fri Sep 03 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-4
- Build storagenode from source

* Fri Sep 03 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-3
- Fixed wrong placement of web consile files

* Thu Sep 02 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-2
- Include web console files

* Thu Sep 02 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-1
- Updated to version 1.37.2

* Sun Aug 08 2021 Jonny Heggheim <hegjon@gmail.com> - 1.35.3-1
- Initial package from pre-built binary

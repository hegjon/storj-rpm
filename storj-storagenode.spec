%global debug_package %{nil}

Name:    storj-storagenode
Version: 1.35.3
Release: 1%{?dist}
Summary: Storj is building a decentralized cloud storage network

License: AGPLv3
URL:     https://storj.io/

Source0:  https://github.com/storj/storj/releases/download/v%{version}/storagenode_linux_amd64.zip

Source2: storj-storagenode.conf

Source11: storj-storagenode@.service
Source12: storj-storagenode-setup@.service

BuildArch: x86_64

BuildRequires: systemd-rpm-macros
%{?systemd_requires}

%description
Storj is an S3-compatible platform and suite of decentralized applications that
allows you to store data in a secure and decentralized manner. Your files are
encrypted, broken into little pieces and stored in a global decentralized
network of computers. Luckily, we also support allowing you (and only you) to
retrieve those files!

%prep
%setup -c
cp %{SOURCE2} .


%build
#no build, the zip contains the binary

%install
install -D -m755 -p storagenode %{buildroot}%{_bindir}/storagenode

install -D -p -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/storj-storagenode@.service
install -D -p -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/storj-storagenode-setup@.service

install -dD -m 0750 %{buildroot}%{_sharedstatedir}/storj-storagenode


install -dD -m 0750 %{buildroot}%{_sysconfdir}/storj-storagenode


%pre
getent group storj-storagenode >/dev/null || groupadd -r storj-storagenode
getent passwd storj-storagenode >/dev/null || \
  useradd -r -g storj-storagenode -s /sbin/nologin \
    -d %{_sharedstatedir}/storj-storagenode \
    -c 'Storj Storage Node' storj-storagenode
exit 0


%post
%systemd_post storj-storagenode@.service

%preun
%systemd_preun storj-storagenode@.service

%postun
%systemd_postun_with_restart storj-storagenode@\*.service

%files
%doc storj-storagenode.conf
%config %dir %attr(-,-,storj-storagenode) %{_sysconfdir}/storj-storagenode
%{_bindir}/storagenode
%{_unitdir}/storj-storagenode@.service
%{_unitdir}/storj-storagenode-setup@.service
%attr(0770,storj-storagenode,storj-storagenode) %{_sharedstatedir}/storj-storagenode

%changelog
* Sun Aug 08 2021 Jonny Heggheim <hegjon@gmail.com> - 1.35.3-1
- Initial package from pre-built binary

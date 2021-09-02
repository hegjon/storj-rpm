%global debug_package %{nil}

Name:    storj-identity
Version: 1.37.2
Release: 1%{?dist}
Summary: Storj is building a decentralized cloud storage network

License: AGPLv3
URL:     https://storj.io/

Source0:  https://github.com/storj/storj/releases/download/v%{version}/identity_linux_amd64.zip

Source11: storj-identity-create@.service

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


%build
#no build, the zip contains the binary

%install
install -D -m755 -p identity %{buildroot}%{_bindir}/identity

install -D -p -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/storj-identity-create@.service


%post
%systemd_post storj-identity-create@.service

%preun
%systemd_preun storj-identity-create@.service

%postun
%systemd_postun storj-identity-create@\*.service

%files
%{_bindir}/identity
%{_unitdir}/storj-identity-create@.service

%changelog
* Thu Sep 02 2021 Jonny Heggheim <hegjon@gmail.com> - 1.37.2-1
- Updated to version 1.37.2

* Sun Aug 15 2021 Jonny Heggheim <hegjon@gmail.com> - 1.35.3-1
- Initial package from pre-built binary

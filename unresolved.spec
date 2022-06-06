Name:           unresolved
Version:        0.1
Release:        1%{?dist}
Summary:        Remove systemd-resolved and have working network

License:        GPLv3
URL:            TODO
Source0:        unresolved

Requires:       systemd
BuildArch:      noarch

%description
Simple tool fixing DNS resolution on system, when systemd-resolved
is no longer welcome. Disable or unistall the service, but also fix
network resolution to working state.

%prep
%autopatch -p1


%build
:

%install
install -m 755 %{SOURCE0} -D %{buildroot}%{_sbindir}/unresolved

%files
%license LICENSE
%doc README.md
%{_sbindir}/unresolved



%changelog
* Sat Jun 04 2022 Petr Menšík <pemensik@redhat.com>
- 
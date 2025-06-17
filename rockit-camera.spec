Name:      rockit-camera
Version:   %{_version}
Release:   1%{dist}
Summary:   Generic camera control client for the *_camd daemons
Url:       https://github.com/rockit-astro/camd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d

%{__install} %{_sourcedir}/cam %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/cam %{buildroot}/etc/bash_completion.d

%package client
Summary:  Generic camera client
Group:    Unspecified
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/cam
/etc/bash_completion.d/cam

%changelog

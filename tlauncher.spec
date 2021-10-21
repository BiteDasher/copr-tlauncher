%define secname TLauncher

Name:		tlauncher
Version:	2.82
Release:	2
Summary:	Unofficial Minecraft launcher
License:	Custom
Source0:	https://tlauncher.org/download/14724
Source1:	https://tlauncher.org/fav-icon-512.png
Source2:	https://raw.githubusercontent.com/BiteDasher/copr-tlauncher/master/%{name}.desktop
Source3:	https://raw.githubusercontent.com/BiteDasher/copr-tlauncher/master/%{name}

Requires:	libjawt.so
Requires:	atk
Requires:	libdrm
Requires:	fontconfig
Requires:	xrandr
Requires:	cairo
Requires:	pango
Requires:	xdg-utils
Requires:	bash

BuildRequires:	unzip

BuildArch:	noarch

%description
Unofficial Minecraft: Java Edition launcher

%prep
mkdir -p %{_builddir}/tmp
unzip "%{SOURCE0}" -d %{_builddir}/tmp

%install
install -D -m 755 %{_builddir}/tmp/%{secname}-%{version}.jar %{buildroot}/opt/%{name}/%{name}.jar
install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -D -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
/opt/%{name}
/opt/%{name}/%{name}.jar

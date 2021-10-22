%define secname TLauncher

Name:		tlauncher
Version:	2.82
Release:	3
Summary:	Unofficial Minecraft launcher
License:	Custom
Source0:	https://tlauncher.org/download/14724
Source1:	https://tlauncher.org/fav-icon-512.png
Source2:	%{name}.desktop
Source3:	%{name}

Requires:	jre-openjdk
Requires:	jre-headless
Requires:	libdrm
Requires:	fontconfig
Requires:	xrandr
Requires:	cairo
Requires:	pango
Requires:	xdg-utils
Requires:	bash

BuildRequires:	unzip
BuildRequires:	ImageMagick

BuildArch:	noarch

%description
Unofficial Minecraft: Java Edition launcher

%prep
mkdir -p %{_builddir}/tmp
cp %{SOURCE1} %{_builddir}/tmp/512x512.png
unzip "%{SOURCE0}" -d %{_builddir}/tmp

%build
for size in 256x256 192x192 128x128 96x96 48x48; do
  convert -verbose -resize ${size} -quality 100 %{_builddir}/tmp/512x512.png \
                                                %{_builddir}/tmp/${size}.png
done

%install
install -D -m 755 %{_builddir}/tmp/%{secname}-%{version}.jar %{buildroot}/opt/%{name}/%{name}.jar
for size in 512x512 256x256 192x192 128x128 96x96 48x48; do
  install -D -m 644 %{_builddir}/tmp/${size}.png \
                    %{buildroot}/%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
#install -D -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
install -D -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
/opt/%{name}
/opt/%{name}/%{name}.jar

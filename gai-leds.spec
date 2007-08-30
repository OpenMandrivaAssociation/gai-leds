%define name gai-leds
%define version 0.6
%define release %mkrel 5

Name: %name
Summary: GAI applet displaying the status of the keyboard leds.
Version: %{version}
Release: %{release}
License: GPL
Url: http://gai.sf.net
Group: Monitoring
Source: http://prdownloads.sourceforge.net/gai/%{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
Patch: gai-album-0.6-rox-install.patch
BuildRoot: %{_tmppath}/build-root-%{name}
BuildRequires: libgai-devel >= 0.5.3

%description
Displays the status of the keyboard leds. Useful for people with
wireless keyboards.

This applet can be used in the GNOME and ROX Panels and as a
WindowMaker dockapp. Other panels and Window Managers will be
supported soon.

%prep
%setup -q 
%patch -p1

%build
%configure2_5x
%make 

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std
%if %_lib != lib
mv %buildroot%_prefix/lib/* %buildroot%_libdir/
%endif
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > %{buildroot}/%{_menudir}/%{name} 
?package(%name): command="%{_bindir}/%name" icon="%name.png" \
                needs="X11" section="Applications/Monitoring" \
 title="Gai-leds" longtitle="Displays the status of the keyboard leds" \
 xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gai-leds
Comment=Displays the status of the keyboard leds
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-System-Monitoring;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING README README.gai
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_%{name}Applet.server
%{_menudir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/*
%_libdir/apps/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png



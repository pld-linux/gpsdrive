Summary:	gpsdrive - a GPS based navigation tool
Summary(pl):	gpsdrive - narzêdzie do nawigacji oparte o GPS
Name:		gpsdrive
Version:	1.32
Release:	1
License:	GPL
Vendor:		Fritz Ganter <ganter@ganter.at>
Group:		Applications/Communications
Source0:	http://gpsdrive.kraftvoll.at/%{name}-%{version}.tar.gz
# Source0-md5:	24b8e3c9d94de184f1a7daaede226fa5
Patch0:		%{name}-assert.patch
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gpsdrive is a map-based navigation system. It displays your position
on a zoomable map provided from a NMEA-capable GPS receiver. The maps
are autoselected for the best resolution, depending of your position,
and the displayed image can be zoomed. Maps can be downloaded from the
Internet with one mouse click. The program provides information about
speed, direction, bearing, arrival time, actual position, and target
position. Speech output is also available. MySQL is supported. See
http://gpsdrive.kraftvoll.at for new releases.

%description -l pl
Gpsdrive jest bazuj±cym na mapie systemem nawigacyjnym. Wy¶wietla
pozycje podawan± przez odbiornik GPS z obs³ug± NMEA na skalowalnej
mapie. Mapy s± automatycznie dobierane dla uzyskania najlepszej
rozdzielczo¶ci w zale¿no¶ci od pozycji, a wy¶wietlany obraz mo¿na
zbli¿aæ. Pobieranie map z Internetu odbywa siê jednym klikniêciem
myszy. Program informuje o prêdko¶ci, kierunku, azymucie, czasie
przybycia, aktualnej pozycji i pozycji punktu docelowego. Dostêpna
jest tak¿e informacja g³osowa. Obs³ugiwany jest MySQL.
Sprawd¼ na http://gpsdrive.kraftvoll.at czy jest nowsza wersja.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc GPS-receivers AUTHORS TODO README README.gpspoint2gspdrive FAQ.gpsdrive README.SQL create.sql NMEA.txt wp2sql README.kismet
%lang(es) %doc LEEME
%lang(fr) %doc LISEZMOI LISEZMOI.kismet LISEZMOI.SQL FAQ.gpsdrive.fr

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/gpsdrive
%{_datadir}/gpsdrive/gpsdrivesplash.png
%{_datadir}/gpsdrive/friendsicon.png

%{_mandir}/man1/gpsdrive.1*
%lang(de) %{_mandir}/de/man1/gpsdrive.1*
%lang(es) %{_mandir}/es/man1/gpsdrive.1*

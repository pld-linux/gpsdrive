#
#
#
Summary:	gpsdrive is a GPS based navigation tool
Name:		gpsdrive
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gpsdrive.kraftvoll.at/%{name}-%{version}.tar.gz
Vendor:		Fritz Ganter <ganter@ganter.at>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gdk-pixbuf-devel

%define _prefix /usr
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
Gpsdrive jest bazujacym na mapie systemem nawigacyjnym. Wy¶wietla Twoj±
pozycje podawan± przez odbiornik GPS z obs³ug± NMEA na skalowalnej mapie.
Mapy s± automatycznie dobierane dla uzyskania najlepszej rozdzielczo¶ci w
zale¿no¶ci od Twojej pozycji a wy¶wietlany obraz mo¿na zbli¿aæ. Pobieraie
map z Internetu odbywa siê jednym klikniêciem myszy.
Program informuje o prêdko¶ci, kierunku, azymucie, czasie przybycia,
aktualnej pozycji i pozycji punmktu docelowego. Dostepna jest tak¿e
informacja g³osowa, wsparcie dla MySQL.
Sprawd¼ na http://gpsdrive.kraftvoll.at czy jest nowsza wersja.


%prep
%setup -q
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir}


%build
%{__make}
%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install-strip

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}/%{name}-%{version}
%files
%defattr(644,root,root,755)
%doc GPS-receivers INSTALL AUTHORS COPYING  TODO README LEEME LISEZMOI README.FreeBSD README.gpspoint2gspdrive FAQ.gpsdrive FAQ.gpsdrive.fr  README.SQL create.sql  NMEA.txt wp2sql README.kismet  LISEZMOI.kismet LISEZMOI.SQL
%doc %{_mandir}/de/man1/gpsdrive.1.gz
%doc %{_mandir}/es/man1/gpsdrive.1.gz
%doc %{_mandir}/man1/gpsdrive.1.gz

%{_libdir}/*
%attr(755,root,root) %{_bindir}/*

%dir %{_datadir}/gpsdrive
%{_datadir}/gpsdrive/gpsdrivesplash.png
%{_datadir}/gpsdrive/friendsicon.png
%{_datadir}/locale/*/LC_MESSAGES/*

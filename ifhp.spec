Summary:	Print filter for hp postscript, text, and other printers
Summary(pl):	Filtr wydruku HP postscriptu, tekstu i innych drukarek
Name:		ifhp
Version:	3.4.4
Release:	2
License:	GPL and Artistic License
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
Group:		Applications/System
Source0:	ftp://ftp.astart.com/pub/LPRng/FILTERS/%{name}-%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-trim_cmdline.patch
URL:		http://www.astart.com/LPRng/LPRng.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
Requires:	lpr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	rhs-printfilters
Obsoletes:	apsfilter

%define	        lpfiltersdir lpfilters

%description
ifhp is a highly versatile print filter for BSD based print spoolers.
It can be configured to handle text, PostScript, PJL, PCL, and raster
printers, supports conversion from one format to another, and can be
used as a stand-alone print utility.

It is the primary supported print filter for the LPRng print spooler.

%description -l pl
ifhp jest wszechstronnym filtrem wydruków do menad¿erów wydruku
bazuj±cych na BSD. Mo¿e byæ skonfigurowany do obs³ugi tekstu,
PostScriptu, PJL, PCL i drukarek rasterowych, obs³uguje konwersjê
miêdzy formatami, mo¿e byæ u¿ywany jako samodzielne narzêdzie do
drukowania.

Jest to podstawowy filtr dla menad¿era LPRng.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
%{__autoconf}
gettextize --copy --force
%configure \
	--with-filterdir=%{_libdir}/%{lpfiltersdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf

gzip -9nf README ifhp.conf.sample

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz HOWTO/*.html
%attr(755,root,root) %{_libdir}/%{lpfiltersdir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*

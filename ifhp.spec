Summary:	Print filter for hp postscript, text, and other printers
Summary(pl):	Filtr wydruku HP postscriptu, tekstu i innych drukarek
Name:		ifhp
Version:	3.5.10
Release:	2
License:	GPL and Artistic
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
Group:		Applications/System
Source0:	ftp://ftp.lprng.com/pub/LPRng/ifhp/%{name}-%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-trim_cmdline.patch
URL:		http://www.lprng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
Requires:	/usr/bin/lpr
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
%{__gettextize}
aclocal
%{__autoconf}
%configure \
	--with-filterdir=%{_libdir}/%{lpfiltersdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README ifhp.conf.sample HOWTO/*.html
%attr(755,root,root) %{_libdir}/%{lpfiltersdir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*

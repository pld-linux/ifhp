%include	/usr/lib/rpm/macros.perl
Summary:	Print filter for hp postscript, text, and other printers
Summary(pl):	Filtr wydruku HP postscriptu, tekstu i innych drukarek
Name:		ifhp
Version:	3.5.13
Release:	1
License:	GPL/Artistic
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com/
Group:		Applications/System
Source0:	ftp://ftp.lprng.com/pub/LPRng/ifhp/%{name}-%{version}.tgz
# Source0-md5:	b79d51b3abbc02772dae900eae3f93c1
Source1:	%{name}.conf
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-trim_cmdline.patch
URL:		http://www.lprng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov
Requires:	/usr/bin/lpr
Obsoletes:	apsfilter
Obsoletes:	rhs-printfilters
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	        lpfiltersdir lpfilters
# only few scripts need it
%define		_noautoreq	'perl(Net::SNMP)'

%description
ifhp is a highly versatile print filter for BSD based print spoolers.
It can be configured to handle text, PostScript, PJL, PCL, and raster
printers, supports conversion from one format to another, and can be
used as a stand-alone print utility.

It is the primary supported print filter for the LPRng print spooler.

%description -l pl
ifhp jest wszechstronnym filtrem wydruków dla opartych na BSD
zarz±dców wydruku. Mo¿e byæ skonfigurowany do obs³ugi tekstu,
PostScriptu, PJL, PCL i drukarek rastrowych, obs³uguje konwersjê
miêdzy formatami, mo¿e byæ u¿ywany jako samodzielne narzêdzie do
drukowania.

Jest to podstawowy filtr dla zarz±dcy drukowania LPRng.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-filterdir=%{_libdir}/%{lpfiltersdir} \
	--with-foomatic-rip=/usr/bin/foomatic-rip
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf

for f in $RPM_BUILD_ROOT%{_datadir}/locale/fr/LC_MESSAGES/ifhp.mo ; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README ifhp.conf.sample DOCS/*.{html,jpg}
# HOWTO/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{lpfiltersdir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*

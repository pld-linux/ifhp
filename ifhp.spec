%include	/usr/lib/rpm/macros.perl
Summary:	Print filter for HP postscript, text, and other printers
Summary(pl.UTF-8):	Filtr wydruku HP postscriptu, tekstu i innych drukarek
Name:		ifhp
Version:	3.5.20
Release:	3
License:	GPL or Artistic
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com/
Group:		Applications/System
Source0:	ftp://ftp.lprng.com/pub/LPRng/ifhp/%{name}-%{version}.tgz
# Source0-md5:	25b151b3adb953b571e6b0a7cc9937f3
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-trim_cmdline.patch
Patch2:		%{name}-no-Werror.patch
URL:		http://www.lprng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	perl-Net-SNMP
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

%description -l pl.UTF-8
ifhp jest wszechstronnym filtrem wydruków dla opartych na BSD
zarządców wydruku. Może być skonfigurowany do obsługi tekstu,
PostScriptu, PJL, PCL i drukarek rastrowych, obsługuje konwersję
między formatami, może być używany jako samodzielne narzędzie do
drukowania.

Jest to podstawowy filtr dla zarządcy drukowania LPRng.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf autom4te.cache

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-filterdir=%{_libdir}/%{lpfiltersdir} \
	--with-foomatic-rip=/usr/bin/foomatic-rip \
	--with-pagesize=a4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man8/*

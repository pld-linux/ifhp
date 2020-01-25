#
# WARNING;
#	DO NOT update this to 3.5.22, that release is broken.
#
Summary:	Print filter for HP postscript, text, and other printers
Summary(pl.UTF-8):	Filtr wydruku HP postscriptu, tekstu i innych drukarek
Name:		ifhp
Version:	3.5.20
Release:	6
License:	GPL v2 or Artistic
Group:		Applications/System
Source0:	http://www.lprng.com/DISTRIB/ifhp/%{name}-%{version}.tgz
# Source0-md5:	25b151b3adb953b571e6b0a7cc9937f3
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-trim_cmdline.patch
Patch2:		%{name}-no-Werror.patch
Patch3:		%{name}-a4.patch
URL:		http://www.lprng.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	ghostscript
BuildRequires:	perl-Net-SNMP
BuildRequires:	perl-modules
BuildRequires:	rpm-perlprov
Requires:	/usr/bin/lpr
Suggests:	a2ps
Suggests:	ghostscript
Obsoletes:	apsfilter
Obsoletes:	rhs-printfilters
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	        lpfiltersdir	%{_libexecdir}/lpfilters
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

%build
%{__autoconf}
%configure \
	A2PS=/usr/bin/a2ps \
	GS=/usr/bin/gs \
	--disable-gscheck \
	--with-filterdir=%{lpfiltersdir} \
	--with-fontdir=%{lpfiltersdir}/fonts \
	--with-foomatic-rip=/usr/bin/foomatic-rip \
	--with-pagesize=a4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .

# some random junk and docs
%{__rm} $RPM_BUILD_ROOT%{lpfiltersdir}/UTILS/{400095.ppd,HP2500CJ.PPD,Watermarks,accounting.sh.in,extract_pjl,fixupdate.in,install-sh,mkinstalldirs,sendhp.sh.in,stopstr.c,supported.in,test1,use_snmp_for_status}

# not installed
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README ifhp.conf.sample DOCS/*.{html,jpg}
# HOWTO/*.html
%attr(755,root,root) %{_bindir}/extract_pjl
%attr(755,root,root) %{_bindir}/snmp_printer_status
%attr(755,root,root) %{lpfiltersdir}/extract_pjl
%attr(755,root,root) %{lpfiltersdir}/ifhp
%attr(755,root,root) %{lpfiltersdir}/snmp_printer_status
%attr(755,root,root) %{lpfiltersdir}/textps
%attr(755,root,root) %{lpfiltersdir}/wrapper
%{lpfiltersdir}/snmp_printer_status.conf
%dir %{lpfiltersdir}/UTILS
%attr(755,root,root) %{lpfiltersdir}/UTILS/accounting.sh
%attr(755,root,root) %{lpfiltersdir}/UTILS/fixupdate
%attr(755,root,root) %{lpfiltersdir}/UTILS/phaser5400_snmp_mib_query
%attr(755,root,root) %{lpfiltersdir}/UTILS/sendhp.sh
%attr(755,root,root) %{lpfiltersdir}/UTILS/supported
%{lpfiltersdir}/UTILS/ellipse.ps
%{lpfiltersdir}/UTILS/one.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man8/ifhp.8*
%{_mandir}/man8/textps.8*

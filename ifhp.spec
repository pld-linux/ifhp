Summary:	print filter for hp postscript, text, and other printers
Name:		ifhp
Version:	3.4.4
Release:	1
License:	GPL and Artistic License
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.astart.com/pub/LPRng/FILTERS/%{name}-%{version}.tgz
Source1:	%{name}.conf
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.astart.com/LPRng/LPRng.html
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

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
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

Summary:	print filter for hp postscript, text, and other printers
Name:		ifhp
Version:	3.4.2
Release:	1
License:	GPL and Artistic License
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.astart.com/pub/LPRng/FILTERS/%{name}-%{version}.tgz
Source1:	%{name}.conf
URL:		http://www.astart.com/LPRng/LPRng.html
Requires:	lpr
Obsoletes:	rhs-printfilters
Obsoletes:	apsfilter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	        lpfiltersdir lpfilters

%description
ifhp is a highly versatile print filter for BSD based print spoolers.
It can be configured to handle text, PostScript, PJL, PCL, and raster
printers, supports conversion from one format to another, and can be
used as a stand-alone print utility.

It is the primary supported print filter for the LPRng print spooler.

%prep
%setup -q

%build
%configure \
	--with-filterdir=%{_libdir}/%{lpfiltersdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_mandir}/man8}

%{__make} INSTALL_PREFIX=$RPM_BUILD_ROOT install
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf.sample .
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/ifhp.conf

gzip -9nf HOWTO/*.html README ifhp.conf.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc HOWTO/*.gz
%attr(755,root,root) %{_libdir}/%{lpfiltersdir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*

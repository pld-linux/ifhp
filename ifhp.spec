Summary:	print filter for hp postscript, text, and other printers
Name:		ifhp
Version:	3.3.18
Release:	1
Copyright:	OpenSource
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/LPRng/FILTERS/%{name}-%{version}.tgz
URL:		http://www.astart.com/LPRng.html
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ifhp is a highly versatile print filter for BSD based print spoolers.
It can be configured to handle text, PostScript, PJL, PCL, and raster
printers, supports conversion from one format to another, and can be
used as a stand-alone print utility.

It is the primary supported print filter for the LPRng print spooler.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libexecdir},%{_mandir}/man8}
%{__make} INSTALL_PREFIX=$RPM_BUILD_ROOT install
mv -f $RPM_BUILD_ROOT/%{_sysconfdir}/ifhp.conf.sample .
gzip -9nf HOWTO/*.html README ifhp.conf.sample \
	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc HOWTO/*.gz
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/ifhp.conf
%attr(755,root,root)  %{_libexecdir}/filters/*
%{_mandir}/*/*.gz

Summary:	print filter for hp postscript, text, and other printers
Name:		ifhp
Version:	3.3.19
Release:	2
License:	OpenSource
Vendor:		Astart Technologies, San Diego, CA 92123 http://www.astart.com
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.astart.com/pub/LPRng/FILTERS/%{name}-%{version}.tgz
Requires:       lpr
URL:		http://www.astart.com/LPRng.html
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
LDFLAGS="-s"; export LDFLAGS
%configure --with-filterdir=%{_libdir}/%{lpfiltersdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir},%{_mandir}/man8}

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
%attr(755,root,root)  %{_libdir}/%{lpfiltersdir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/*/*

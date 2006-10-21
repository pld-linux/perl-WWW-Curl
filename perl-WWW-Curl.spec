#
# Conditional build:
%bcond_with	tests	# perform "make test" (fetches URL passed interactively)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Curl
Summary:	WWW::Curl::easy - Perl extension interface for libcurl
Summary(pl):	WWW::Curl::easy - interfejs perlowy do biblioteki libcurl
Name:		perl-WWW-Curl
Version:	3.02
Release:	1
License:	MPL or MIT/X
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0619d1a39fc92e9a5363f2269b7b1d59
URL:		http://curl.haxx.se/libcurl/perl/
BuildRequires:	curl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-Curl-easy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Curl::easy provides an interface to the libcurl C library
(http://curl.haxx.se/).

Before v2.0, this module was called 'Curl::easy'. The name has changed
to better suit CPAN naming guidelines.

%description -l pl
WWW::Curl::easy dostarcza interfejs do biblioteki C libcurl
(http://curl.haxx.se/).

Przed wersj± 2.0 ten modu³ nazywa³ siê Curl::easy. Nazwa zosta³a
zmieniona, aby lepiej pasowa³a do wytycznych CPAN dotycz±cych
nazewnictwa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/WWW/Curl.pm
%{perl_vendorarch}/WWW/Curl
%dir %{perl_vendorarch}/auto/WWW/Curl
%{perl_vendorarch}/auto/WWW/Curl/Curl.bs
%attr(755,root,root) %{perl_vendorarch}/auto/WWW/Curl/Curl.so
%{_mandir}/man3/*

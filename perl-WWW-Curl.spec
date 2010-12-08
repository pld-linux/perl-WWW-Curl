#
# Conditional build:
%bcond_with	tests	# perform "make test" (fetches URL passed interactively)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Curl
Summary:	WWW::Curl::easy - Perl extension interface for libcurl
Summary(pl.UTF-8):	WWW::Curl::easy - interfejs perlowy do biblioteki libcurl
Name:		perl-WWW-Curl
Version:	4.15
Release:	1
License:	MPL or MIT/X
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SZ/SZBALINT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31c0b8c7e5e2d26bcc8213d702186d5f
URL:		http://curl.haxx.se/libcurl/perl/
BuildRequires:	curl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-Curl-easy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Curl::easy provides an interface to the libcurl C library
<http://curl.haxx.se/>.

Before v2.0, this module was called 'Curl::easy'. The name has changed
to better suit CPAN naming guidelines.

%description -l pl.UTF-8
WWW::Curl::easy dostarcza interfejs do biblioteki C libcurl
<http://curl.haxx.se/>.

Przed wersją 2.0 ten moduł nazywał się Curl::easy. Nazwa została
zmieniona, aby lepiej pasowała do wytycznych CPAN dotyczących
nazewnictwa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	OPTIMIZE="%{rpmcflags}" \
	OTHERLDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/WWW/Curl/.packlist

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
%{_mandir}/man3/WWW::Curl.3pm*

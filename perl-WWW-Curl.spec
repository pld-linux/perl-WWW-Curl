#
# Conditional build:
%bcond_with	tests	# perform "make test" (fetches URL passed interactively)
#
%define		pdir	WWW
%define		pnam	Curl
Summary:	WWW::Curl::easy - Perl extension interface for libcurl
Summary(pl.UTF-8):	WWW::Curl::easy - interfejs perlowy do biblioteki libcurl
Name:		perl-WWW-Curl
Version:	4.17
Release:	8
License:	MPL or MIT/X
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SZ/SZBALINT/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	997ac81cd6b03b30b36f7cd930474845
Patch0:		WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
Patch1:		curl-7.66.0.patch
Patch2:		curl-7.69.0.patch
Patch3:		WWW-Curl-Adapt-to-curl-7.87.0.patch
Patch4:		WWW-Curl-Work-around-a-macro-bug-in-curl-7.87.0.patch
URL:		http://curl.haxx.se/libcurl/perl/
BuildRequires:	curl-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Module-Install
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Obsoletes:	perl-Curl-easy < 2
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
%attr(755,root,root) %{perl_vendorarch}/auto/WWW/Curl/Curl.so
%{_mandir}/man3/WWW::Curl.3pm*

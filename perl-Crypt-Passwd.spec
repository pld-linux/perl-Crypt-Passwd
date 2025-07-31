#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	Passwd
Summary:	Crypt::Passwd - interface to the UFC-Crypt library
Summary(pl.UTF-8):	Crypt::Passwd - interfejs do biblioteki UFC-Crypt
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	30
# same as perl and/or UFC-Crypt library
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66d9794442e27f33ad05685035082aa9
Patch0:		crypt.patch
URL:		http://search.cpan.org/dist/Crypt-Passwd/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Passwd Perl module provides an interface layer between Perl 5
and Michael Glad's UFC Crypt library.

%description -l pl.UTF-8
Moduł Perla Crypt::Passwd udostępnia warstwę interfejsu pomiędzy
Perlem 5 a biblioteką UFC Crypt Michaela Glada.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/Crypt/Passwd.pm
%dir %{perl_vendorarch}/auto/Crypt/Passwd
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Passwd/Passwd.so
%{_mandir}/man3/*

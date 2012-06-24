%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Passwd
Summary:	Crypt::Passwd - interface to the UFC-Crypt library
Summary(pl):	Crypt::Passwd - interfejs do biblioteki UFC-Crypt
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	8
# same as perl and/or UFC-Crypt library
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66d9794442e27f33ad05685035082aa9
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Passwd Perl module provides an interface layer between Perl 5
and Michael Glad's UFC Crypt library.

%description -l pl
Modu� Perla Crypt::Passwd udost�pnia warstw� interfejsu pomi�dzy
Perlem 5 a bibliotek� UFC Crypt Michaela Glada.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Passwd.pm
%dir %{perl_vendorarch}/auto/Crypt/Passwd
%{perl_vendorarch}/auto/Crypt/Passwd/Passwd.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Passwd/Passwd.so
%{_mandir}/man3/*

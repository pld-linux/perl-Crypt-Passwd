%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Passwd
Summary:	Crypt::Passwd - Interface to the UFC-Crypt library
Summary(pl):	Crypt::Passwd - interfejs do biblioteki UFC-Crypt
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	8
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	66d9794442e27f33ad05685035082aa9
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Passwd Perl module - Interface to the UFC-Crypt library.

%description -l pl
Modu³ Perla Crypt::Passwd - interfejs do biblioteki UFC-Crypt.

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

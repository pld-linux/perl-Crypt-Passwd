%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Passwd
Summary:	Crypt::Passwd - Interface to the UFC-Crypt library
Summary(pl):	Crypt::Passwd - interfejs do biblioteki UFC-Crypt
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	7
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Passwd Perl module - Interface to the UFC-Crypt library.

%description -l pl
Modu³ Perla Crypt::Passwd - interfejs do biblioteki UFC-Crypt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Crypt/Passwd.pm
%dir %{perl_sitearch}/auto/Crypt/Passwd
%{perl_sitearch}/auto/Crypt/Passwd/Passwd.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Passwd/Passwd.so
%{_mandir}/man3/*

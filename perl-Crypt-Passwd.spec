%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-Passwd perl module
Summary(pl):	Modu³ perla Crypt-Passwd
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-Passwd-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-Passwd - Interface to the UFC-Crypt library.

%description -l pl
Crypt-Passwd - interfejs do biblioteki UFC-Crypt.

%prep
%setup -q -n Crypt-Passwd-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Crypt/Passwd.pm
%dir %{perl_sitearch}/auto/Crypt/Passwd
%{perl_sitearch}/auto/Crypt/Passwd/Passwd.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Passwd/Passwd.so
%{_mandir}/man3/*

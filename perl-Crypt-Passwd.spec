%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-Passwd perl module
Summary(pl):	Modu³ perla Crypt-Passwd
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-Passwd-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Crypt/Passwd/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Crypt/Passwd
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Crypt/Passwd.pm

%dir %{perl_sitearch}/auto/Crypt/Passwd
%{perl_sitearch}/auto/Crypt/Passwd/.packlist
%{perl_sitearch}/auto/Crypt/Passwd/Passwd.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Passwd/Passwd.so

%{_mandir}/man3/*

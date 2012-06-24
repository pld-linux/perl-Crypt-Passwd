%define	pdir	Crypt
%define	pnam	Passwd
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-Passwd perl module
Summary(pl):	Modu� perla Crypt-Passwd
Name:		perl-Crypt-Passwd
Version:	0.03
Release:	6

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-Passwd - Interface to the UFC-Crypt library.

%description -l pl
Crypt-Passwd - interfejs do biblioteki UFC-Crypt.

%prep
%setup -q -n Crypt-Passwd-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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

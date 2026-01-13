#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Handle-Util
Summary:	IO::Handle::Util - Functions for working with IO::Handle like objects.
Name:		perl-IO-Handle-Util
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a334bd3fc284d176e0aaccb1b65b4279
URL:		https://metacpan.org/release/IO-Handle-Util
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(asa)
BuildRequires:	perl-IO-String
BuildRequires:	perl-Sub-Exporter
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a number of helpful routines to manipulate or
create IO::Handle like objects.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--destdir=$RPM_BUILD_ROOT \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \
	--destdir=$RPM_BUILD_ROOT \
	--create_packlist=0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%dir %{perl_vendorlib}/IO/Handle
%{perl_vendorlib}/IO/Handle/*.pm
%{perl_vendorlib}/IO/Handle/Prototype
%{perl_vendorlib}/IO/Handle/Util
%{_mandir}/man3/*

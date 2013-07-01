%bcond_with pod

Name:           perl-Error
Version:        0.17017
Release:        7
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Error
Summary:        Error/exception handling in an OO-ish way
Url:            http://search.cpan.org/dist/Error/
Group:          Development/Libraries/Perl
#Source:         http://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-0.17016.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
Source1001: 	perl-Error.manifest
BuildRequires:  perl
BuildRequires:  perl(Module::Build)
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if %{with pod}
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(warnings)
Requires:       perl(Scalar::Util)
Requires:       perl(warnings)

%description
The 'Error' package provides two interfaces. Firstly 'Error' provides a
procedural interface to exception handling. Secondly 'Error' is a base
class for errors/exceptions that can either be thrown, for subsequent
catch, or can simply be recorded.

Errors in the class 'Error' should not be thrown directly, but the user
should throw errors from a sub-class of 'Error'.

%prep
%setup -q -n %{cpan_name}-%{version}
cp %{SOURCE1001} .

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%doc ChangeLog examples README

%changelog

#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working /dev/dsp)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	DSP
Summary:	Audio::DSP Perl module - interface to *NIX digital audio device
Summary(pl.UTF-8):	Moduł Perla Audio::DSP - interfejs do uniksowego cyfrowego urządzenia cyfrowego dźwiękowego
Name:		perl-Audio-DSP
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7c3027a732d14665d4ffec0aff4b548e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::DSP is built around the OSS (Open Sound System) API and allows
Perl to interface with a digital audio device. The Audio::DSP object
stores I/O parameters and also supplies temporary storage for raw
audio data.

%description -l pl.UTF-8
Moduł Audio::DSP jest oparty na API systemu OSS (Open Sound System) i
pozwala Perlowi na dostęp do urządzenia cyfrowego dźwięku. Obiekt
Audio::DSP przechowuje parametry wejścia/wyjścia oraz tymczasowo
surowe dane dźwiękowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/Audio/DSP.pm
%dir %{perl_vendorarch}/auto/Audio/DSP
%{perl_vendorarch}/auto/Audio/DSP/autosplit.ix
%{perl_vendorarch}/auto/Audio/DSP/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/DSP/*.so
%{_mandir}/man3/*

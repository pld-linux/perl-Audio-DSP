#
# Conditional build:
# _with_tests - perform "make test" (requires working /dev/dsp)
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	DSP
Summary:	Audio::DSP Perl module - interface to *NIX digital audio device
Summary(pl):	Modu³ Perla Audio::DSP - interfejs do *niksowego urz±dzenia cyfrowego d¼wiêku
Name:		perl-Audio-DSP
Version:	0.02
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::DSP is built around the OSS (Open Sound System) API and allows
Perl to interface with a digital audio device. The Audio::DSP object
stores I/O parameters and also supplies temporary storage for raw
audio data.

%description -l pl
Modu³ Audio::DSP jest oparty na API systemu OSS (Open Sound System) i
pozwala Perlowi na dostêp do urz±dzenia cyfrowego d¼wiêku. Obiekt
Audio::DSP przechowuje parametry wej¶cia/wyj¶cia oraz tymczasowo
surowe dane d¼wiêkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Audio/DSP.pm
%dir %{perl_sitearch}/auto/Audio/DSP
%{perl_sitearch}/auto/Audio/DSP/autosplit.ix
%{perl_sitearch}/auto/Audio/DSP/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/DSP/*.so
%{_mandir}/man3/*

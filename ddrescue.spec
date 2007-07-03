Summary:	Data copying in presence of I/O errors
Summary(pl.UTF-8):	Kopiowanie danych z błędami wejścia/wyjścia
Name:		ddrescue
Version:	1.5
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/ddrescue/%{name}-%{version}.tar.bz2
# Source0-md5:	91931e2b2163c8d7a5adc1959da3023f
Patch0:		%{name}-info.patch
Patch1:		http://guru.multimedia.cx/wp-content/uploads/2006/08/ddrescue-patch.txt
URL:		http://www.nongnu.org/ddrescue/ddrescue.html
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ddrescue copies data from one file or block device (hard disk, cdrom,
etc) to another, trying hard to rescue data in case of read errors.

ddrescue does not truncate the output file if not asked to. So,
everytime you run it on the same output file, it tries to fill in the
gaps.

If you have two or more copies of a damaged file, cdrom, etc, and run
ddrescue on all of them, one at a time, with the same output file, you
will probably obtain a complete and error-free file. This is so
because the probability of having damaged areas at the same places on
different input files is very low.

If you also use the bad blocks file feature of ddrescue, the data will
be rescued very efficiently. Also you can interrupt the rescue at any
time and resume it later.

%description -l pl.UTF-8
ddrescue kopiuje dane z jednego pliku lub urządzenia blokowego (dysku
twardego, płyty CD-ROM itp.) do innego, próbując usilnie uratować dane
w przypadku błędów odczytu.

ddrescue nie skraca pliku wyjściowego, jeśli nie zostanie o to
poproszony. Za każdym uruchomieniem na tym samym pliku wyjściowym
próbuje wypełnić luki.

Jeśli mamy dwie lub więcej kopii uszkodzonego pliku, płyty itp. i
uruchomimy ddrescue na wszystkich z nich z tym samym plikiem
wyjściowym, prawdopodobnie dostaniemy cały plik bez błędów. Stanie się
tak dlatego, że prawdopodobieństwo uszkodzenia pliku w tych samych
miejscach na różnych kopiach jest bardzo małe.

Jeśli użyjemy opcji obsługi pliku z listą złych bloków w ddrescue dane
będą odzyskiwane bardzo wydajnie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir}

%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ddrescue
%{_infodir}/*.info*
%{_mandir}/man1/*

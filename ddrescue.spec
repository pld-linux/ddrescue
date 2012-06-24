Summary:	Data copying in presence of I/O errors
Summary(pl):	Kopiowanie danych z b��dami wej�cia/wyj�cia
Name:		ddrescue
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/ddrescue/%{name}-%{version}.tar.bz2
# Source0-md5:	1178c44372a08c906cc5bb1141ae7baf
URL:		http://www.nongnu.org/ddrescue/ddrescue.html
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


%description -l pl
ddrescue kopiuje dane z jednego pliku lub urz�dzenia blokowego (dysku
twardego, p�yty CD-ROM itp.) do innego, pr�buj�c usilnie uratowa� dane
w przypadku b��d�w odczytu.

ddrescue nie skraca pliku wyj�ciowego, je�li nie zostanie o to
poproszony. Za ka�dym uruchomieniem na tym samym pliku wyj�ciowym
pr�buje wype�ni� luki.

Je�li mamy dwie lub wi�cej kopii uszkodzonego pliku, p�yty itp. i
uruchomimy ddrescue na wszystkich z nich z tym samym plikiem
wyj�ciowym, prawdopodobnie dostaniemy ca�y plik bez b��d�w. Stanie si�
tak dlatego, �e prawdopodobie�stwo uszkodzenia pliku w tych samych
miejscach na r�nych kopiach jest bardzo ma�e.

Je�li u�yjemy opcji obs�ugi pliku z list� z�ych blok�w w ddrescue dane
b�d� odzyskiwane bardzo wydajnie.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D ddrescue	$RPM_BUILD_ROOT%{_bindir}/ddrescue
install -D ddrescue.1	$RPM_BUILD_ROOT%{_mandir}/man1/ddrescue.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/ddrescue
%{_mandir}/man1/*

Summary:	Data copying in presence of I/O errors
Summary(pl):	Kopiowanie danych z b³êdami we/wy
Name:		ddrescue
Version:	0.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
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

if you also use the bad blocks file feature of ddrescue, the data will
be rescued very efficiently. ddrescue helps, when nobody else will:
Your disk has crashed and you try to copy it over to another one.
Standard Un*x tools like cp, cat, dd will abort on every I/O error.
dd_rescue won't.

%description -l pl
ddrescue pomaga tam, gdzie nic innego nie pomo¿e: kiedy dysk padnie i
próbujemy go skopiowaæ na inny. Standardowe narzêdzia uniksowe takie
jak cp, cat, dd koñcz± dzia³anie na ka¿dym b³êdzie we/wy. dd_rescue
tego nie robi.

%prep
%setup -q

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D ddrescue   $RPM_BUILD_ROOT%{_bindir}/ddrescue
install -D ddrescue.1 $RPM_BUILD_ROOT%{_mandir}/man1/ddrescue.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/ddrescue
%attr(644,root,root) %{_mandir}/man1/*

Summary:	Markdown parser library
Summary(pl.UTF-8):	Biblioteka parsera formatu Markdown
Name:		libsoldout
Version:	1.4
Release:	1
License:	ISC
Group:		Libraries
#Source0Download: http://fossil.instinctive.eu/index.html
Source0:	http://fossil.instinctive.eu/%{name}-%{version}.tar.bz2
# Source0-md5:	671a78763355608bbd8d664ae6d33903
URL:		http://fossil.instinctive.eu/libsoldout/home
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Markdown parser library.

%description -l pl.UTF-8
Biblioteka parsera formatu Markdown.

%package devel
Summary:	Header files for libsoldout library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsoldout
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsoldout library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsoldout.

%package static
Summary:	Static libsoldout library
Summary(pl.UTF-8):	Statyczna biblioteka libsoldout
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsoldout library.

%description static -l pl.UTF-8
Statyczna biblioteka libsoldout.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -Werror" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}/soldout,%{_mandir}/man{1,3}}

install mkd2html mkd2latex mkd2man $RPM_BUILD_ROOT%{_bindir}
install libsoldout.so.1 $RPM_BUILD_ROOT%{_libdir}
ln -sf libsoldout.so.1 $RPM_BUILD_ROOT%{_libdir}/libsoldout.so
cp -p libsoldout.a $RPM_BUILD_ROOT%{_libdir}
cp -p *.h $RPM_BUILD_ROOT%{_includedir}/soldout
cp -p mkd*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p soldout*.3 $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/mkd2html
%attr(755,root,root) %{_bindir}/mkd2latex
%attr(755,root,root) %{_bindir}/mkd2man
%attr(755,root,root) %{_libdir}/libsoldout.so.1
%{_mandir}/man1/mkd2html.1*
%{_mandir}/man1/mkd2latex.1*
%{_mandir}/man1/mkd2man.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoldout.so
%{_includedir}/soldout
%{_mandir}/man3/soldout*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsoldout.a

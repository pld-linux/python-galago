Summary:	Python bindings for Galago
Summary(pl.UTF-8):	Wiązania Pythona do Galago
Name:		python-galago
Version:	0.5.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://galago-project.org/files/releases/source/galago-python/galago-python-%{version}.tar.bz2
# Source0-md5:	27be31fcf2886aa21823caec15dc34aa
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
Requires:	libgalago
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Galago.

%description -l pl.UTF-8
Wiązania Pythona do Galago.

%prep
%setup -q -n galago-python-%{version}

%build
%{configure}
%{__make} \
	PYTHON="%{__python}" \
	PYTHONINCLUDE="%{py_incdir}" \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PYTHON="%{__python}" \
	PYTHONLIBDIR="%{py_sitedir}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/gtk-2.0/galago
%{py_sitedir}/gtk-2.0/galago/*.py*
%attr(755,root,root) %{py_sitedir}/gtk-2.0/galago/*.so
%{_datadir}/pygtk/*/defs/galago.defs
%{_pkgconfigdir}/*

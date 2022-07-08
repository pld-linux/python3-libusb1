#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Pure-python wrapper for libusb-1.0
Summary(pl.UTF-8):	Czysto pythonowy interfejs do libusb-1.0
Name:		python-libusb1
Version:	1.9.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/libusb1/
Source0:	https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
# Source0-md5:	d0bad54896a370b75f5c0e1579da4d62
URL:		https://pypi.org/project/libusb1/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:        sed >= 4.0
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure-python wrapper for libusb-1.0. Supports all transfer types, both
in synchronous and asynchronous mode.

%description -l pl.UTF-8
Czysto pythonowy interfejs do libusb-1.0. Obsługuje wszystkie rodzaje
transmisji, zarówno w trybie synchronicznym, jak i asynchronicznym.

%package -n python3-libusb1
Summary:	Pure-python wrapper for libusb-1.0
Summary(pl.UTF-8):	Czysto pythonowy interfejs do libusb-1.0
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-libusb1
Pure-python wrapper for libusb-1.0. Supports all transfer types, both
in synchronous and asynchronous mode.

%description -n python3-libusb1 -l pl.UTF-8
Czysto pythonowy interfejs do libusb-1.0. Obsługuje wszystkie rodzaje
transmisji, zarówno w trybie synchronicznym, jak i asynchronicznym.

%prep
%setup -q -n libusb1-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-libusb1-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-libusb1-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	$RPM_BUILD_ROOT%{_examplesdir}/python-libusb1-%{version}/*.py

# tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/usb1/testUSB1.py*
%py_postclean
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python3},' \
	$RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}/*.py

# tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/usb1/testUSB1.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/usb1/__pycache__/testUSB1.*
# duplicate of versioned dir?
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/libusb1.egg-info
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/libusb1.py[co]
%{py_sitescriptdir}/usb1
%{py_sitescriptdir}/libusb1-%{version}-py*.egg-info
%{_examplesdir}/python-libusb1-%{version}
%endif

%if %{with python3}
%files -n python3-libusb1
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/libusb1.py
%{py3_sitescriptdir}/__pycache__/libusb1.cpython-*.py[co]
%{py3_sitescriptdir}/usb1
%{py3_sitescriptdir}/libusb1-%{version}-py*.egg-info
%{_examplesdir}/python3-libusb1-%{version}
%endif

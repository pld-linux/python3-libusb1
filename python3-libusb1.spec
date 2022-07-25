#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pure-python wrapper for libusb-1.0
Summary(pl.UTF-8):	Czysto pythonowy interfejs do libusb-1.0
Name:		python3-libusb1
Version:	3.0.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/libusb1/
Source0:	https://files.pythonhosted.org/packages/source/l/libusb1/libusb1-%{version}.tar.gz
# Source0-md5:	ffbb02bf9aa49f973a6a58112aed7b06
URL:		https://pypi.org/project/libusb1/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.4
# python3-libusb1 3.0.0 by mistake was released as python-libusb1; last version with python2 support was 1.x
Obsoletes:	python-libusb1 == 3.0.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure-python wrapper for libusb-1.0. Supports all transfer types, both
in synchronous and asynchronous mode.

%description -l pl.UTF-8
Czysto pythonowy interfejs do libusb-1.0. Obsługuje wszystkie rodzaje
transmisji, zarówno w trybie synchronicznym, jak i asynchronicznym.

%prep
%setup -q -n libusb1-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python3},' \
	$RPM_BUILD_ROOT%{_examplesdir}/python3-libusb1-%{version}/*.py

# tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/usb1/testUSB1.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/usb1/__pycache__/testUSB1.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/libusb1.py
%{py3_sitescriptdir}/__pycache__/libusb1.cpython-*.py[co]
%{py3_sitescriptdir}/usb1
%{py3_sitescriptdir}/libusb1-%{version}-py*.egg-info
%{_examplesdir}/python3-libusb1-%{version}

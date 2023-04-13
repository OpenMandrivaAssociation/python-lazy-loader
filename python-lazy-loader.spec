Summary:	Populate library namespace without incurring immediate import costs
Name:		python-lazy-loader
Version:	0.2
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/lazy-loader/
Source0:	https://pypi.org/packages/source/l/lazy_loader/lazy_loader-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
lazy-loader makes it easy to load subpackages and functions on demand.

Motivation:

  * Allow subpackages to be made visible to users without incurring import costs.
  * Allow external libraries to be imported only when used, improving import
    times.

%files
%{py_sitedir}/lazy_loader
%{py_sitedir}/lazy_loader-*.*-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n lazy_loader-%{version}

%build
%py_build

%install
%py_install


%define module lazy-loader
%define oname lazy_loader

Name:		python-lazy-loader
Summary:	Populate library namespace without incurring immediate import costs
Version:	0.5
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/lazy-loader/
Source0:	https://pypi.org/packages/source/l/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:  python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
lazy-loader makes it easy to load subpackages and functions on demand.

Motivation:

Allow subpackages to be made visible to users without incurring import costs.
Allow external libraries to be imported only when used, improving import times.

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info

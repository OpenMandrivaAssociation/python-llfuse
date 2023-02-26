%define pypi_name llfuse
Name:               python-llfuse
Version:            1.4.2
Release:            1
Summary:            Python Bindings for the low-level FUSE API

Source0:            https://pypi.io/packages/source/l/%{name}/%{pypi_name}-%{version}.tar.gz
URL:                https://github.com/python-llfuse/python-llfuse
Group:              Development/Python
License:            LGPLv2+
BuildRequires:      pkgconfig(fuse)
BuildRequires:      pkgconfig(python)
BuildRequires:      python3dist(setuptools)
BuildRequires:      python3dist(cython)
BuildRequires:      python3dist(pip)
BuildRequires:      python3dist(wheel)

%description
LLFUSE is a set of Python bindings for the low level FUSE API. It requires at
least FUSE 2.8.0 and supports both Python 2.x and 3.x.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well. 

%prep
%setup -q -n llfuse-%{version}
%autopatch -p1

# drop bundled egg-info
rm -rf src/%{module}.egg-info

# re-generate sources
find . -type f -name "llfuse.c" -print -delete

%build
%py_build

rm doc/html/.buildinfo

%install
%py_install

%files
%license LICENSE
%doc Changes.rst doc/html
%{python_sitearch}/*



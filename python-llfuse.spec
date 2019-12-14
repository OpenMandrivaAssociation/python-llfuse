Name:               python-llfuse
Version:            1.3.6
Release:            1
Summary:            Python Bindings for the low-level FUSE API

Source0:            https://files.pythonhosted.org/packages/75/b4/5248459ec0e7e1608814915479cb13e5baf89034b572e3d74d5c9219dd31/llfuse-%{version}.tar.bz2
URL:                https://github.com/python-llfuse/python-llfuse
Group:              Development/Python
License:            LGPLv2+
BuildRequires:      pkgconfig(fuse)
BuildRequires:      python3-devel
BuildRequires:      python3dist(setuptools)
BuildRequires:      python3dist(cython)

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
%__python setup.py build_cython
%py_build

rm doc/html/.buildinfo

%install
%py_install

%files -n python-%{module}
%license LICENSE
%doc Changes.rst doc/html
%{python_sitearch}/*



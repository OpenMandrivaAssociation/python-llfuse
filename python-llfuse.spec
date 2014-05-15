Name:               python-llfuse
Version:            0.40
Release:            1
Summary:            Python Bindings for the low-level FUSE API

Source0:            http://python-llfuse.googlecode.com/files/llfuse-%{version}.tar.bz2
URL:                http://code.google.com/p/python-llfuse/
Group:              Development/Python
License:            LGPLv2+
BuildRequires:      attr-devel
BuildRequires:      fuse-devel >= 2.8.0
BuildRequires:      python-distribute >= 0.6.12
BuildRequires:      python-devel

%description
LLFUSE is a set of Python bindings for the low level FUSE API. It requires at
least FUSE 2.8.0 and supports both Python 2.x and 3.x.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well. 

%prep
%setup -q -n "llfuse-%{version}"
%__rm doc/html/.buildinfo

%build
%__python ./setup.py build

%install
%__python ./setup.py install \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"

%files
%doc Changes.txt doc/html
%{py_platsitedir}/*



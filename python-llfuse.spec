Name:               python-llfuse
Version:            0.37.1
Release:            1
Summary:            Python Bindings for the low-level FUSE API
Source0:            http://python-llfuse.googlecode.com/files/llfuse-%{version}.tar.bz2
URL:                http://code.google.com/p/python-llfuse/
Group:              Development/Python
License:            LGPLv2+
BuildRequires:      attr-devel
BuildRequires:      fuse-devel >= 2.8.0
BuildRequires:      python-setuptools
%py_requires -d

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
%{python_sitearch}/*


%changelog
* Sun Jan 22 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.37.1-1
+ Revision: 764912
- new version 0.37.1

* Tue Dec 06 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.37-1
+ Revision: 738418
- Update to 0.37

* Tue Nov 29 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.36-1
+ Revision: 735378
- imported package python-llfuse


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3A6A4DB839EAA6D7 (aacid@kde.org)
#
Name     : libspectre
Version  : 0.2.12
Release  : 13
URL      : https://libspectre.freedesktop.org/releases/libspectre-0.2.12.tar.gz
Source0  : https://libspectre.freedesktop.org/releases/libspectre-0.2.12.tar.gz
Source1  : https://libspectre.freedesktop.org/releases/libspectre-0.2.12.tar.gz.sig
Summary  : libgs wrapper library
Group    : Development/Tools
License  : GPL-2.0
Requires: libspectre-lib = %{version}-%{release}
Requires: libspectre-license = %{version}-%{release}
BuildRequires : ghostscript-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-png)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
What is libspectre
==================
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package dev
Summary: dev components for the libspectre package.
Group: Development
Requires: libspectre-lib = %{version}-%{release}
Provides: libspectre-devel = %{version}-%{release}
Requires: libspectre = %{version}-%{release}

%description dev
dev components for the libspectre package.


%package lib
Summary: lib components for the libspectre package.
Group: Libraries
Requires: libspectre-license = %{version}-%{release}

%description lib
lib components for the libspectre package.


%package license
Summary: license components for the libspectre package.
Group: Default

%description license
license components for the libspectre package.


%prep
%setup -q -n libspectre-0.2.12
cd %{_builddir}/libspectre-0.2.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676507759
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1676507759
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libspectre
cp %{_builddir}/libspectre-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libspectre/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libspectre/spectre-document.h
/usr/include/libspectre/spectre-exporter.h
/usr/include/libspectre/spectre-macros.h
/usr/include/libspectre/spectre-page.h
/usr/include/libspectre/spectre-render-context.h
/usr/include/libspectre/spectre-status.h
/usr/include/libspectre/spectre-version.h
/usr/include/libspectre/spectre.h
/usr/lib64/libspectre.so
/usr/lib64/pkgconfig/libspectre.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libspectre.so.1
/usr/lib64/libspectre.so.1.1.12

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libspectre/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

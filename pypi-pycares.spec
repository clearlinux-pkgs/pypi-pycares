#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-pycares
Version  : 4.3.0
Release  : 31
URL      : https://files.pythonhosted.org/packages/01/50/e3015e6e03a3cf64113f509e8b86b71af37169b59ccedfcb182f3d031329/pycares-4.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/50/e3015e6e03a3cf64113f509e8b86b71af37169b59ccedfcb182f3d031329/pycares-4.3.0.tar.gz
Summary  : Python interface for c-ares
Group    : Development/Tools
License  : MIT
Requires: pypi-pycares-license = %{version}-%{release}
Requires: pypi-pycares-python = %{version}-%{release}
Requires: pypi-pycares-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===========================

%package license
Summary: license components for the pypi-pycares package.
Group: Default

%description license
license components for the pypi-pycares package.


%package python
Summary: python components for the pypi-pycares package.
Group: Default
Requires: pypi-pycares-python3 = %{version}-%{release}

%description python
python components for the pypi-pycares package.


%package python3
Summary: python3 components for the pypi-pycares package.
Group: Default
Requires: python3-core
Provides: pypi(pycares)
Requires: pypi(cffi)

%description python3
python3 components for the pypi-pycares package.


%prep
%setup -q -n pycares-4.3.0
cd %{_builddir}/pycares-4.3.0
pushd ..
cp -a pycares-4.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683042945
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycares
cp %{_builddir}/pycares-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b || :
cp %{_builddir}/pycares-%{version}/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
/usr/share/package-licenses/pypi-pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

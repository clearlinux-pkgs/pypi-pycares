#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pycares
Version  : 4.2.2
Release  : 25
URL      : https://files.pythonhosted.org/packages/ac/a3/21594384c2398420dd7f6e8656aeb5a2c15128ddf2b85ef5f4403342e18d/pycares-4.2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/a3/21594384c2398420dd7f6e8656aeb5a2c15128ddf2b85ef5f4403342e18d/pycares-4.2.2.tar.gz
Summary  : Python interface for c-ares
Group    : Development/Tools
License  : MIT
Requires: pypi-pycares-filemap = %{version}-%{release}
Requires: pypi-pycares-lib = %{version}-%{release}
Requires: pypi-pycares-license = %{version}-%{release}
Requires: pypi-pycares-python = %{version}-%{release}
Requires: pypi-pycares-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cffi)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
===========================

%package filemap
Summary: filemap components for the pypi-pycares package.
Group: Default

%description filemap
filemap components for the pypi-pycares package.


%package lib
Summary: lib components for the pypi-pycares package.
Group: Libraries
Requires: pypi-pycares-license = %{version}-%{release}
Requires: pypi-pycares-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pycares package.


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
Requires: pypi-pycares-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pycares)
Requires: pypi(cffi)

%description python3
python3 components for the pypi-pycares package.


%prep
%setup -q -n pycares-4.2.2
cd %{_builddir}/pycares-4.2.2
pushd ..
cp -a pycares-4.2.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1660059563
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycares
cp %{_builddir}/pycares-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
cp %{_builddir}/pycares-%{version}/deps/c-ares/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pycares

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pycares/c4de206e0fa6c5d904eb6c7695f6ffb5d2d90a6b
/usr/share/package-licenses/pypi-pycares/e9c597f9b6cf935773ee731d4170b0c2ba142dbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nbdime
Version  : 3.1.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/e1/36/28232d030c1b4a25116799f1aa3cd26208964f302daa324c314fd576820a/nbdime-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/36/28232d030c1b4a25116799f1aa3cd26208964f302daa324c314fd576820a/nbdime-3.1.1.tar.gz
Summary  : Diff and merge of Jupyter Notebooks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-nbdime-bin = %{version}-%{release}
Requires: pypi-nbdime-data = %{version}-%{release}
Requires: pypi-nbdime-license = %{version}-%{release}
Requires: pypi-nbdime-python = %{version}-%{release}
Requires: pypi-nbdime-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(colorama)
BuildRequires : pypi(gitpython)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyter_server)
BuildRequires : pypi(jupyter_server_mathjax)
BuildRequires : pypi(jupyterlab)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(pygments)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tornado)
BuildRequires : pypi(wheel)

%description
**[Installation](#installation)** |
**[Documentation](#documentation)** |
**[Contributing](#contributing)** |
**[Development Install](#development-install)** |
**[Testing](#testing)** |
**[License](#license)** |
**[Getting help](#getting-help)**

%package bin
Summary: bin components for the pypi-nbdime package.
Group: Binaries
Requires: pypi-nbdime-data = %{version}-%{release}
Requires: pypi-nbdime-license = %{version}-%{release}

%description bin
bin components for the pypi-nbdime package.


%package data
Summary: data components for the pypi-nbdime package.
Group: Data

%description data
data components for the pypi-nbdime package.


%package license
Summary: license components for the pypi-nbdime package.
Group: Default

%description license
license components for the pypi-nbdime package.


%package python
Summary: python components for the pypi-nbdime package.
Group: Default
Requires: pypi-nbdime-python3 = %{version}-%{release}

%description python
python components for the pypi-nbdime package.


%package python3
Summary: python3 components for the pypi-nbdime package.
Group: Default
Requires: python3-core
Provides: pypi(nbdime)
Requires: pypi(colorama)
Requires: pypi(gitpython)
Requires: pypi(jinja2)
Requires: pypi(jupyter_server)
Requires: pypi(jupyter_server_mathjax)
Requires: pypi(nbformat)
Requires: pypi(pygments)
Requires: pypi(requests)
Requires: pypi(tornado)

%description python3
python3 components for the pypi-nbdime package.


%prep
%setup -q -n nbdime-3.1.1
cd %{_builddir}/nbdime-3.1.1
pushd ..
cp -a nbdime-3.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656392395
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nbdime
cp %{_builddir}/nbdime-3.1.1/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-nbdime/ff097755ecfcda288aeecae6768698bd7403f179
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
## Remove excluded files
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_notebook_config.d/nbdime.json
rm -f %{buildroot}*/usr/etc/jupyter/jupyter_server_config.d/nbdime.json
rm -f %{buildroot}*/usr/etc/jupyter/nbconfig/notebook.d/nbdime.json
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/git-nbdiffdriver
/usr/bin/git-nbdifftool
/usr/bin/git-nbmergedriver
/usr/bin/git-nbmergetool
/usr/bin/hg-nbdiff
/usr/bin/hg-nbdiffweb
/usr/bin/hg-nbmerge
/usr/bin/hg-nbmergeweb
/usr/bin/nbdiff
/usr/bin/nbdiff-web
/usr/bin/nbdime
/usr/bin/nbmerge
/usr/bin/nbmerge-web
/usr/bin/nbshow

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/lab/extensions/nbdime-jupyterlab-2.1.1.tgz
/usr/share/jupyter/labextensions/nbdime-jupyterlab/package.json
/usr/share/jupyter/labextensions/nbdime-jupyterlab/schemas/nbdime-jupyterlab/package.json.orig
/usr/share/jupyter/labextensions/nbdime-jupyterlab/schemas/nbdime-jupyterlab/plugin.json
/usr/share/jupyter/labextensions/nbdime-jupyterlab/static/568.1b78fd8776f786fbead6.js
/usr/share/jupyter/labextensions/nbdime-jupyterlab/static/663.6eafeabe4f43d5a1b512.js
/usr/share/jupyter/labextensions/nbdime-jupyterlab/static/remoteEntry.83c796749c1a515caea8.js
/usr/share/jupyter/labextensions/nbdime-jupyterlab/static/style.js
/usr/share/jupyter/labextensions/nbdime-jupyterlab/static/third-party-licenses.json
/usr/share/jupyter/nbextensions/nbdime/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nbdime/ff097755ecfcda288aeecae6768698bd7403f179

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

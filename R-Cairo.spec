#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Cairo
Version  : 1.5.9
Release  : 49
URL      : https://cran.r-project.org/src/contrib/Cairo_1.5-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Cairo_1.5-9.tar.gz
Summary  : R graphics device using cairo graphics library for creating
Group    : Development/Tools
License  : GPL-2.0
Requires: R-Cairo-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : cairo-dev
BuildRequires : gcc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(xt)
Patch1: build.patch

%description
No detailed description available

%package lib
Summary: lib components for the R-Cairo package.
Group: Libraries

%description lib
lib components for the R-Cairo package.


%prep
%setup -q -c -n Cairo
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552724799

%install
export SOURCE_DATE_EPOCH=1552724799
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cairo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cairo
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Cairo
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  Cairo || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Cairo/DESCRIPTION
/usr/lib64/R/library/Cairo/INDEX
/usr/lib64/R/library/Cairo/Meta/Rd.rds
/usr/lib64/R/library/Cairo/Meta/features.rds
/usr/lib64/R/library/Cairo/Meta/hsearch.rds
/usr/lib64/R/library/Cairo/Meta/links.rds
/usr/lib64/R/library/Cairo/Meta/nsInfo.rds
/usr/lib64/R/library/Cairo/Meta/package.rds
/usr/lib64/R/library/Cairo/NAMESPACE
/usr/lib64/R/library/Cairo/NEWS
/usr/lib64/R/library/Cairo/R/Cairo
/usr/lib64/R/library/Cairo/R/Cairo.rdb
/usr/lib64/R/library/Cairo/R/Cairo.rdx
/usr/lib64/R/library/Cairo/help/AnIndex
/usr/lib64/R/library/Cairo/help/Cairo.rdb
/usr/lib64/R/library/Cairo/help/Cairo.rdx
/usr/lib64/R/library/Cairo/help/aliases.rds
/usr/lib64/R/library/Cairo/help/paths.rds
/usr/lib64/R/library/Cairo/html/00Index.html
/usr/lib64/R/library/Cairo/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Cairo/libs/Cairo.so
/usr/lib64/R/library/Cairo/libs/Cairo.so.avx2
/usr/lib64/R/library/Cairo/libs/Cairo.so.avx512

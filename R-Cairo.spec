#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: e661f3a
#
Name     : R-Cairo
Version  : 1.6.2
Release  : 98
URL      : https://cran.r-project.org/src/contrib/Cairo_1.6-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Cairo_1.6-2.tar.gz
Summary  : R Graphics Device using Cairo Graphics Library for Creating
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-Cairo-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : cairo-dev
BuildRequires : gcc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(xt)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-Cairo package.
Group: Libraries

%description lib
lib components for the R-Cairo package.


%prep
%setup -q -n Cairo
pushd ..
cp -a Cairo buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701292854

%install
export SOURCE_DATE_EPOCH=1701292854
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

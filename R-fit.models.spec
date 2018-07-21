#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fit.models
Version  : 0.5.14
Release  : 1
URL      : https://cran.r-project.org/src/contrib/fit.models_0.5-14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fit.models_0.5-14.tar.gz
Summary  : Compare Fitted Models
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
print, summary, plot, etc.) were originally provided in the robust package to
  compare robustly and classically fitted model objects. The aim of the fit.models
  package is to separate this fitted model object comparison functionality from
  the robust package and to extend it to support fitting methods (e.g., classical,
  robust, Bayesian, regularized, etc.) more generally.

%prep
%setup -q -c -n fit.models

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532208975

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532208975
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fit.models
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fit.models
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fit.models
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fit.models|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fit.models/DESCRIPTION
/usr/lib64/R/library/fit.models/INDEX
/usr/lib64/R/library/fit.models/Meta/Rd.rds
/usr/lib64/R/library/fit.models/Meta/features.rds
/usr/lib64/R/library/fit.models/Meta/hsearch.rds
/usr/lib64/R/library/fit.models/Meta/links.rds
/usr/lib64/R/library/fit.models/Meta/nsInfo.rds
/usr/lib64/R/library/fit.models/Meta/package.rds
/usr/lib64/R/library/fit.models/NAMESPACE
/usr/lib64/R/library/fit.models/R/fit.models
/usr/lib64/R/library/fit.models/R/fit.models.rdb
/usr/lib64/R/library/fit.models/R/fit.models.rdx
/usr/lib64/R/library/fit.models/help/AnIndex
/usr/lib64/R/library/fit.models/help/aliases.rds
/usr/lib64/R/library/fit.models/help/fit.models.rdb
/usr/lib64/R/library/fit.models/help/fit.models.rdx
/usr/lib64/R/library/fit.models/help/paths.rds
/usr/lib64/R/library/fit.models/html/00Index.html
/usr/lib64/R/library/fit.models/html/R.css

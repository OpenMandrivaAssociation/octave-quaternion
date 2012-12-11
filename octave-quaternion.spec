%define	pkgname quaternion
%define name	octave-%{pkgname}
%define version 1.0.0

Summary:	Octave package for manipulation of quaternions
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/quaternion/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.1.0
BuildRequires:  octave-devel >= 3.1.0
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildArch:	noarch

%description
Octave package for manipulation of quaternions used for frame transformations.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}




%changelog
* Wed Jun 29 2011 Lev Givon <lev@mandriva.org> 1.0.0-1mdv2011.0
+ Revision: 688088
- import octave-quaternion



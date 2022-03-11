%global octpkg quaternion

Summary:	Octave package for manipulation of quaternions
Name:		octave-%{octpkg}
Version:	2.4.0
Release:	1
Url:		https://octave.sourceforge.io/%{octpkg}/
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:		octave-%{octpkg}-2.4.0-remove_deprecated_api.patch
License:	GPLv3+
Group:		Sciences/Mathematics

BuildRequires:	octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Quaternion package for GNU Octave, includes a quaternion class with
overloaded operators.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild


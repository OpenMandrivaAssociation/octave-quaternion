%global octpkg quaternion

Summary:	Octave package for manipulation of quaternions
Name:		octave-quaternion
Version:	2.4.0
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/quaternion/
Source0:	https://downloads.sourceforge.net/octave/quaternion-%{version}.tar.gz
Patch0:		octave-quaternion-2.4.0-remove_deprecated_api.patch

BuildRequires:  octave-devel >= 3.8.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Quaternion package for GNU Octave, includes a quaternion class with
overloaded operators.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

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


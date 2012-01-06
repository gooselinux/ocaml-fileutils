%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)
%define debug_package %{nil}

Name:           ocaml-fileutils
Version:        0.4.0
Release:        4.1%{?dist}
Summary:        OCaml library for common file and filename operations

Group:          Development/Libraries
License:        LGPLv2 with exceptions
URL:            http://www.gallu.homelinux.org/download/
Source0:        http://www.gallu.homelinux.org/download/ocaml-fileutils-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExcludeArch:    sparc64 s390 s390x

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-camlp4-devel

%define _use_internal_dependency_generator 0
%define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
%define __find_provides /usr/lib/rpm/ocaml-find-provides.sh

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q
%configure


%build
make


%install
rm -rf $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

# Set htmldir to current directory, then copy the docs (in api/)
# as a %doc rule.
make htmldir=. install


# Tests require ounit.
#%check
#make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/ocaml/fileutils
%if %opt
%exclude %{_libdir}/ocaml/fileutils/*.a
%exclude %{_libdir}/ocaml/fileutils/*.cmx
%exclude %{_libdir}/ocaml/fileutils/*.cmxa
%endif
%exclude %{_libdir}/ocaml/fileutils/*.ml
%exclude %{_libdir}/ocaml/fileutils/*.mli


%files devel
%defattr(-,root,root,-)
%doc COPYING AUTHOR CHANGELOG README TODO api
%if %opt
%{_libdir}/ocaml/fileutils/*.a
%{_libdir}/ocaml/fileutils/*.cmx
%{_libdir}/ocaml/fileutils/*.cmxa
%endif
%{_libdir}/ocaml/fileutils/*.ml
%{_libdir}/ocaml/fileutils/*.mli


%changelog
* Wed Jan 13 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-4.1
- Disable tests and hence remove BR ocaml-ounit.

* Mon Jan 11 2010 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-4
- Import package from Fedora Rawhide to support updated ocaml-gettext.

* Wed Dec 30 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-3
- Rebuild for OCaml 3.11.2.

* Thu Oct  8 2009 Richard W.M. Jones <rjones@redhat.com> - 0.4.0-2
- New upstream version 0.4.0.
- Upstream build system has been rationalized, so remove all the
  hacks we were using.
- Upstream now contains tests, run them.
- Needs ounit in order to carry out the tests.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 23 2009 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-10
- Rebuild for OCaml 3.11.1

* Thu Apr 16 2009 S390x secondary arch maintainer <fedora-s390x@lists.fedoraproject.org>
- ExcludeArch sparc64, s390, s390x as we don't have OCaml on those archs
  (added sparc64 per request from the sparc maintainer)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-8
- Rebuild for OCaml 3.11.0+rc1.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-7
- Rebuild for OCaml 3.11.0

* Wed Apr 23 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-5
- Rebuild for OCaml 3.10.2

* Sat Mar  1 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-4
- Rebuild for ppc64.

* Thu Feb 21 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-3
- Fixed grammar in the description section.
- License is LGPLv2 with exceptions
- Include license file with both RPMs.
- Include other documentation only in the -devel RPM.

* Tue Feb 12 2008 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-2
- Added BR ocaml-camlp4-devel.
- Build into tmp directory under the build root.

* Wed Aug  8 2007 Richard W.M. Jones <rjones@redhat.com> - 0.3.0-1
- Initial RPM release.

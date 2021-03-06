%global cartridgedir %{_libexecdir}/stickshift/cartridges/embedded/mongodb-2.0
%global frameworkdir %{_libexecdir}/stickshift/cartridges/mongodb-2.0

Name: cartridge-mongodb-2.0
Version: 0.20.4
Release: 1%{?dist}
Summary: Embedded mongodb support for OpenShift

Group: Network/Daemons
License: ASL 2.0
URL: http://openshift.redhat.com
Source0: http://mirror.openshift.com/pub/crankcase/source/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: git

Requires: stickshift-abstract
Requires: mongodb-server
Requires: mongodb-devel
Requires: libmongodb
Requires: mongodb


%description
Provides rhc mongodb cartridge support


%prep
%setup -q


%build
rm -rf git_template
cp -r template/ git_template/
cd git_template
git init
git add -f .
git config user.email "builder@example.com"
git config user.name "Template builder"
git commit -m 'Creating template'
cd ..
git clone --bare git_template git_template.git
rm -rf git_template
touch git_template.git/refs/heads/.gitignore


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{cartridgedir}
mkdir -p %{buildroot}%{cartridgedir}/info/data/
mkdir -p %{buildroot}/%{_sysconfdir}/stickshift/cartridges
cp LICENSE %{buildroot}%{cartridgedir}/
cp COPYRIGHT %{buildroot}%{cartridgedir}/
cp -r info %{buildroot}%{cartridgedir}/
cp -r git_template.git %{buildroot}%{cartridgedir}/info/data/
ln -s %{cartridgedir}/info/configuration/ %{buildroot}/%{_sysconfdir}/stickshift/cartridges/%{name}
ln -s %{cartridgedir} %{buildroot}/%{frameworkdir}
ln -s %{cartridgedir}/../../abstract/info/hooks/update-namespace %{buildroot}%{cartridgedir}/info/hooks/update-namespace


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%attr(0750,-,-) %{cartridgedir}/info/hooks/
%attr(0750,-,-) %{cartridgedir}/info/data/
%attr(0750,-,-) %{cartridgedir}/info/build/
%config(noreplace) %{cartridgedir}/info/configuration/
%attr(0755,-,-) %{cartridgedir}/info/bin/
%attr(0755,-,-) %{cartridgedir}/info/lib/
%attr(0755,-,-) %{cartridgedir}/info/connection-hooks/
%attr(0755,-,-) %{frameworkdir}
%{_sysconfdir}/stickshift/cartridges/%{name}
%{cartridgedir}/info/changelog
%{cartridgedir}/info/control
%{cartridgedir}/info/manifest.yml
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Tue May 22 2012 Dan McPherson <dmcphers@redhat.com> 0.20.4-1
- Merge branch 'master' of github.com:openshift/crankcase (rmillner@redhat.com)
- Merge branch 'master' of github.com:openshift/crankcase (rmillner@redhat.com)
- Merge branch 'master' of github.com:openshift/crankcase (rmillner@redhat.com)
- Fixup from merge (jhonce@redhat.com)
- Merge branch 'master' into US2109 (rmillner@redhat.com)
- Merge branch 'master' into US2109 (rmillner@redhat.com)
- Merge branch 'master' into US2109 (jhonce@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Merge branch 'master' into US2109 (ramr@redhat.com)
- Typeless gears - create app/ dir, rollback logs, manage repo, data and state.
  (ramr@redhat.com)

* Tue May 22 2012 Adam Miller <admiller@redhat.com> 0.20.3-1
- Fix cleanup. (mpatel@redhat.com)

* Tue May 22 2012 Adam Miller <admiller@redhat.com> 0.20.2-1
- Fix displayed connection info. (mpatel@redhat.com)
- %%build uses git, so BuildRequires: git (admiller@redhat.com)
- Address review comments. (mpatel@redhat.com)
- Changes to make mongodb run in standalone gear. (mpatel@redhat.com)

* Thu May 10 2012 Adam Miller <admiller@redhat.com> 0.20.1-1
- bumping spec versions (admiller@redhat.com)

* Mon May 07 2012 Adam Miller <admiller@redhat.com> 0.19.4-1
- Merge branch 'master' of github.com:openshift/crankcase (rmillner@redhat.com)
- Some of the ctl script were not sourcing util from abstract.
  (rmillner@redhat.com)

* Mon May 07 2012 Adam Miller <admiller@redhat.com> 0.19.3-1
- Add support for pre/post start/stop hooks to both web application service and
  embedded cartridges.   Include the cartridge name in the calling hook to
  avoid conflicts when typeless gears are implemented. (rmillner@redhat.com)

* Mon May 07 2012 Adam Miller <admiller@redhat.com> 0.19.2-1
- Fix for bugz 818377 - cleanup mongo shell history. (ramr@redhat.com)
- remove old obsoletes (dmcphers@redhat.com)
- clean specs (whearn@redhat.com)

* Thu Apr 26 2012 Adam Miller <admiller@redhat.com> 0.19.1-1
- bumping spec versions (admiller@redhat.com)

* Mon Apr 23 2012 Adam Miller <admiller@redhat.com> 0.18.5-1
- cleaning up spec files (dmcphers@redhat.com)

* Sat Apr 21 2012 Dan McPherson <dmcphers@redhat.com> 0.18.4-1
- new package built with tito

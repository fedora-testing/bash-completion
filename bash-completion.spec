Name:           bash-completion
Version:        20050112
Release:        1
Epoch:          0
Summary:        Programmable completion for Bash

Group:          System Environment/Shells
License:        GPL
URL:            http://www.caliban.org/bash/
Source0:     http://www.caliban.org/files/bash/bash-completion-20050112.tar.bz2
Source1:        %{name}.profile
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bash >= 0:2.05-12

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.


%prep
%setup -q -n bash_completion


%build


%install
rm -rf $RPM_BUILD_ROOT %{name}-ghosts.list
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 bash_completion $RPM_BUILD_ROOT%{_sysconfdir}
install -pm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/bash_completion.sh
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -pm 644 contrib/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
cd contrib
for f in * ; do
  ln -s %{_datadir}/%{name}/$f $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
  echo "%ghost %{_sysconfdir}/bash_completion.d/$f" >> ../%{name}-ghosts.list
done
cd -


%clean
rm -rf $RPM_BUILD_ROOT


%triggerin -- bittorrent
if [ ! -e %{_sysconfdir}/bash_completion.d/bittorrent ] ; then
  ln -s %{_datadir}/%{name}/bittorrent %{_sysconfdir}/bash_completion.d
fi
%triggerun -- bittorrent
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/bittorrent

%triggerin -- cksfv
if [ ! -e %{_sysconfdir}/bash_completion.d/cksfv ] ; then
  ln -s %{_datadir}/%{name}/cksfv %{_sysconfdir}/bash_completion.d
fi
%triggerun -- cksfv
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/cksfv

%triggerin -- freeciv
if [ ! -e %{_sysconfdir}/bash_completion.d/freeciv ] ; then
  ln -s %{_datadir}/%{name}/freeciv %{_sysconfdir}/bash_completion.d
fi
%triggerun -- freeciv
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/freeciv

%triggerin -- gkrellm
if [ ! -e %{_sysconfdir}/bash_completion.d/gkrellm ] ; then
  ln -s %{_datadir}/%{name}/gkrellm %{_sysconfdir}/bash_completion.d
fi
%triggerun -- gkrellm
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/gkrellm

%triggerin -- mailman
if [ ! -e %{_sysconfdir}/bash_completion.d/mailman ] ; then
  ln -s %{_datadir}/%{name}/mailman %{_sysconfdir}/bash_completion.d
fi
%triggerun -- mailman
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/mailman

%triggerin -- mcrypt
if [ ! -e %{_sysconfdir}/bash_completion.d/mcrypt ] ; then
  ln -s %{_datadir}/%{name}/mcrypt %{_sysconfdir}/bash_completion.d
fi
%triggerun -- mcrypt
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/mcrypt

%triggerin -- mtx
if [ ! -e %{_sysconfdir}/bash_completion.d/mtx ] ; then
  ln -s %{_datadir}/%{name}/mtx %{_sysconfdir}/bash_completion.d
fi
%triggerun -- mtx
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/mtx

%triggerin -- subversion
if [ ! -e %{_sysconfdir}/bash_completion.d/subversion ] ; then
  ln -s %{_datadir}/%{name}/subversion %{_sysconfdir}/bash_completion.d
fi
%triggerun -- subversion
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/subversion

%triggerin -- unace
if [ ! -e %{_sysconfdir}/bash_completion.d/unace ] ; then
  ln -s %{_datadir}/%{name}/unace %{_sysconfdir}/bash_completion.d
fi
%triggerun -- unace
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/unace

%triggerin -- unrar
if [ ! -e %{_sysconfdir}/bash_completion.d/unrar ] ; then
  ln -s %{_datadir}/%{name}/unrar %{_sysconfdir}/bash_completion.d
fi
%triggerun -- unrar
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/unrar


%files -f %{name}-ghosts.list
%defattr(0644,root,root,0755)
%doc BUGS Changelog COPYING README
%config %{_sysconfdir}/bash_completion
%attr(0755,root,root) %config %{_sysconfdir}/profile.d/*
%{_datadir}/%{name}
%dir %{_sysconfdir}/bash_completion.d


%changelog
* Thu Jan 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:20050112-1
- Update to 20050112, openssl patch applied upstream.

* Wed Jan  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:20050103-1
- Update to 20050103.

* Sat Nov 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:20041017-5
- Change version scheme, bump release to provide Extras upgrade path.

* Sat Nov  6 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.4.20041017
- Do the right thing with bash >= 3 too in profile.d snippet (bug 2228, thanks
  to Thorsten Leemhuis).

* Mon Oct 18 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20041017
- Update to 20041017, adds dhclient, lvm, and bittorrent completion.

* Mon Jul 12 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20040711
- Update to 20040711, patches applied upstream.

* Sun Jul  4 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20040704
- Update to 20040704.
- Change to symlinked /etc/bash_completion.d snippets, add patch to read them.

* Wed May 26 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20040526
- Update to 20040526.

* Thu Apr  1 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.3.20040331
- Add command-specific contrib snippet copying triggers.

* Thu Apr  1 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20040331
- Update to 20040331.

* Sun Feb 15 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20040214
- Update to 20040214.

* Wed Feb 11 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20040210
- Update to 20040210.

* Fri Jan  2 2004 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20040101
- Update to 20040101.
- Update %%description.

* Sat Dec 27 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20031225
- Update to 20031225.

* Sat Dec 20 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.2.20031215
- Don't pull in *.rpm* from %%{_sysconfdir}/bash_completion.d.

* Mon Dec 15 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20031215
- Update to 20031215.

* Sun Nov 30 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20031125
- Update to 20031125.

* Thu Nov 13 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20031112
- Update to 20031112.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20031022
- Update to 20031022.

* Tue Oct  7 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20031007
- Update to 20031007.

* Tue Sep 30 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20030929
- Update to 20030929.

* Fri Sep 12 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20030911
- Update to 20030911.

* Thu Aug 21 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20030821
- Update to 20030821.
- Drop .nosrc.rpm patch, already applied upstream.

* Sat Aug 16 2003 Ville Skyttä <ville.skytta at iki.fi> 0:0.0-0.fdr.1.20030811
- Update to 20030811.
- Patch to make rpm --rebuild work with .nosrc.rpm's.

* Sun Aug  3 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030803
- Update to 20030803.

* Wed Jul 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030721
- Update to 20030721.

* Sun Jul 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030713
- Update to 20030713.

* Mon Jun 30 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030630
- Update to 20030630.

* Sun Jun  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030607
- Update to 20030607.

* Tue May 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030527
- Update to 20030527.

* Sat May 24 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.0-0.fdr.1.20030505
- First build.

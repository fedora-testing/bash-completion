Name:           bash-completion
Version:        1.0
Release:        4%{?dist}
Epoch:          1
Summary:        Programmable completion for Bash

Group:          System Environment/Shells
License:        GPLv2+
URL:            http://bash-completion.alioth.debian.org/
Source0:        http://bash-completion.alioth.debian.org/files/%{name}-%{version}.tar.gz
Source1:        %{name}-mock
Source2:        %{name}-plague-client
Source3:        %{name}-repomanage
# http://git.debian.org/?p=bash-completion/bash-completion.git;a=commitdiff;h=1421e55aac075e13491cd212b796bdd453214a2c
Patch0:         %{name}-1.0-bash4quoting-490322.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       bash >= 2.05-12
# For symlinking in triggers, #490768
Requires:       coreutils

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash 2.


%prep
%setup -q
%patch0 -p1
install -pm 644 %{SOURCE1} contrib/mock
install -pm 644 %{SOURCE2} contrib/plague-client
install -pm 644 %{SOURCE3} contrib/repomanage
rm contrib/cowsay # cowsay ships an updated one


%build


%install
rm -rf $RPM_BUILD_ROOT %{name}-ghosts.list
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 bash_completion $RPM_BUILD_ROOT%{_sysconfdir}
install -pm 644 bash_completion.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
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


%define do_triggerin() if [ ! -e %{_sysconfdir}/bash_completion.d/%1 ] ; then ln -s %{_datadir}/%{name}/%1 %{_sysconfdir}/bash_completion.d || : ; fi
%define do_triggerun() [ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/%1 || :

# Not handled (yet?):
# apache2ctl, bitkeeper, harbour, larch, lisp, p4, povray

%triggerin -- bittorrent
%do_triggerin bittorrent
%triggerun -- bittorrent
%do_triggerun bittorrent

%triggerin -- bridge-utils
%do_triggerin brctl
%triggerun -- bridge-utils
%do_triggerun brctl

%triggerin -- cksfv
%do_triggerin cksfv
%triggerun -- cksfv
%do_triggerun cksfv

%triggerin -- clisp
%do_triggerin clisp
%triggerun -- clisp
%do_triggerun clisp

%triggerin -- dsniff
%do_triggerin dsniff
%triggerun -- dsniff
%do_triggerun dsniff

%triggerin -- freeciv
%do_triggerin freeciv
%triggerun -- freeciv
%do_triggerun freeciv

%triggerin -- gcc-gnat
%do_triggerin gnatmake
%triggerun -- gcc-gnat
%do_triggerun gnatmake

%triggerin -- gcl
%do_triggerin gcl
%triggerun -- gcl
%do_triggerun gcl

%triggerin -- gkrellm
%do_triggerin gkrellm
%triggerun -- gkrellm
%do_triggerun gkrellm

%triggerin -- gnupg2
%do_triggerin gpg2
%triggerun -- gnupg2
%do_triggerun gpg2

%triggerin -- lilypond
%do_triggerin lilypond
%triggerun -- lilypond
%do_triggerun lilypond

%triggerin -- lzma
%do_triggerin lzma
%triggerun -- lzma
%do_triggerun lzma

%triggerin -- lzop
%do_triggerin lzop
%triggerun -- lzop
%do_triggerun lzop

%triggerin -- mailman
%do_triggerin mailman
%triggerun -- mailman
%do_triggerun mailman

%triggerin -- mcrypt
%do_triggerin mcrypt
%triggerun -- mcrypt
%do_triggerun mcrypt

%triggerin -- minicom
%do_triggerin minicom
%triggerun -- minicom
%do_triggerun minicom

%triggerin -- mock
%do_triggerin mock
%triggerun -- mock
%do_triggerun mock

%triggerin -- monodevelop
%do_triggerin monodevelop
%triggerun -- monodevelop
%do_triggerun monodevelop

%triggerin -- mtx
%do_triggerin mtx
%triggerun -- mtx
%do_triggerun mtx

%triggerin -- net-tools
%do_triggerin net-tools
%triggerun -- net-tools
%do_triggerun net-tools

%triggerin -- openssh-clients
%do_triggerin ssh
%triggerun -- openssh-clients
%do_triggerun ssh

%triggerin -- perl-CPANPLUS
%do_triggerin cpan2dist
%triggerun -- perl-CPANPLUS
%do_triggerun cpan2dist

%triggerin -- perl-SVK
%do_triggerin svk
%triggerun -- perl-SVK
%do_triggerun svk

%triggerin -- plague-client
%do_triggerin plague-client
%triggerun -- plague-client
%do_triggerun plague-client

%triggerin -- qemu
%do_triggerin qemu
%triggerun -- qemu
%do_triggerun qemu

%triggerin -- quota
%do_triggerin quota-tools
%triggerun -- quota
%do_triggerun quota-tools

%triggerin -- qt
%do_triggerin qdbus
%triggerun -- qt
%do_triggerun qdbus

%triggerin -- rdesktop
%do_triggerin rdesktop
%triggerun -- rdesktop
%do_triggerun rdesktop

%triggerin -- ruby-ri
%do_triggerin ri
%triggerun -- ruby-ri
%do_triggerun ri

%triggerin -- sbcl
%do_triggerin sbcl
%triggerun -- sbcl
%do_triggerun sbcl

%triggerin -- sitecopy
%do_triggerin sitecopy
%triggerun -- sitecopy
%do_triggerun sitecopy

%triggerin -- snownews
%do_triggerin snownews
%triggerun -- snownews
%do_triggerun snownews

%triggerin -- subversion
%do_triggerin _subversion
%triggerun -- subversion
%do_triggerun _subversion

%triggerin -- unace
%do_triggerin unace
%triggerun -- unace
%do_triggerun unace

%triggerin -- unixODBC
%do_triggerin isql
%triggerun -- unixODBC
%do_triggerun isql

%triggerin -- unrar
%do_triggerin unrar
%triggerun -- unrar
%do_triggerun unrar

%triggerin -- yum-utils
%do_triggerin repomanage
%triggerun -- yum-utils
%do_triggerun repomanage

%triggerin -- vnc
%do_triggerin vncviewer
%triggerun -- vnc
%do_triggerun vncviewer


%files -f %{name}-ghosts.list
%defattr(-,root,root,-)
%doc AUTHORS CHANGES COPYING README TODO
%config(noreplace) %{_sysconfdir}/profile.d/bash_completion.sh
%{_sysconfdir}/bash_completion
%dir %{_sysconfdir}/bash_completion.d/
%{_datadir}/%{name}/


%changelog
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-3
- Do not install cowsay completion, an updated version is shipped with it.

* Tue Apr  7 2009 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-2
- Apply upstream patch to fix quoting issues with bash 4.x (#490322).

* Mon Apr  6 2009 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-1
- 1.0.

* Mon Mar 23 2009 Ville Skyttä <ville.skytta at iki.fi> - 20080705-4.20090314gitf4f0984
- Add dependency on coreutils for triggers (#490768).
- Update and improve mock completion.

* Sun Mar 15 2009 Ville Skyttä <ville.skytta at iki.fi> - 20080705-3.20090314gitf4f0984
- git snapshot f4f0984, fixes #484578 (another issue), #486998.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080705-3.20090211git47d0c5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Ville Skyttä <ville.skytta at iki.fi> - 20080705-2.20090211git47d0c5b
- git snapshot 47d0c5b, fixes #484578.
- lzop and repomanage completions included upstream.

* Sun Jan 18 2009 Ville Skyttä <ville.skytta at iki.fi> - 20080705-2.20090115bzr1252
- r1252 snapshot; all patches applied upstream.
- Do not install mercurial completion, an updated version is shipped with it.
- Improve lzop and repomanage completion.

* Tue Jan  6 2009 Ville Skyttä <ville.skytta at iki.fi> - 20080705-1
- 20080705; new upstream at http://bash-completion.alioth.debian.org/
- Perl, Debian, and scp patches applied upstream.
- Patch to improve man completion: more sections, better filename handling.
- Patch to speed up yum install/deplist completion (#478784).
- Patch to fix and speed up rpm installed packages completion.
- Update mock completion.

* Thu Sep 25 2008 Ville Skyttä <ville.skytta at iki.fi>
- More Matroska associations (#463829, based on patch from Yanko Kaneti).

* Thu Sep 11 2008 Ville Skyttä <ville.skytta at iki.fi> - 20060301-13
- Borrow/improve/adapt to Fedora some patches from Mandriva: improved support
  for getent and rpm --eval, better rpm backup file avoidance, lzma support.
- Patch/unpatch to fix gzip and bzip2 options completion.
- Patch to add --rsyncable to gzip options completion.
- Add and trigger-install support for lzop.
- Associate *.sqlite with sqlite3.

* Wed Jul 23 2008 Ville Skyttä <ville.skytta at iki.fi> - 20060301-12
- Fix plague-client completion install (#456355, Ricky Zhou).
- Trigger-install support for sitecopy.

* Tue Apr 29 2008 Ville Skyttä <ville.skytta at iki.fi> - 20060301-11
- Media player association improvements (#444467).

* Sat Feb 23 2008 Ville Skyttä <ville.skytta at iki.fi> - 20060301-10
- Patch to fix filename completion with svn (#430059).
- Trigger-install support for dsniff.
- Drop disttag.

* Mon Dec 31 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060301-8
- Associate VDR recording files with media players.
- Update mock completion.

* Fri Nov 16 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060301-7
- Add JPEG2000 extensions for display(1) (#304771).
- Update mock completion.

* Sat Sep 22 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060301-6
- Patch to improve perl completion (#299571, Jim Radford,
  http://use.perl.org/~Alias/journal/33508).

* Mon Aug 13 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060301-5
- License: GPLv2+

* Sun Jun 24 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> - 20060301-4
- Update triggers to work with older versions of RPM

* Wed Feb 28 2007 Ville Skyttä <ville.skytta at iki.fi> - 20060301-3
- Fix scp with single quotes (#217178).
- Borrow fix for bzip2 w/spaces, and apropos and whatis support from Debian.

* Thu Aug 31 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060301-2
- Trigger-install support for gcl, lilypond, mercurial and svk.
- Improve mock completion a bit.

* Thu Mar  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 20060301-1
- 20060301, patches and profile.d scriptlet applied/included upstream.
- Convert docs to UTF-8.

* Wed Feb  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050721-4
- Don't source ourselves in non-interactive shells (#180419, Behdad Esfahbod).
- Trigger-install snippets for clisp, gnatmake, isql, ri, sbcl, and snownews.

* Sat Feb  4 2006 Ville Skyttä <ville.skytta at iki.fi>
- Add mtr(8) completion using known hosts (#179918, Yanko Kaneti).

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 20050721-3
- Patch to hopefully fix quoting problems with bash 3.1 (#177056).

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050721-2
- Work around potential login problem in profile.d snippet (#174355).

* Sat Nov 26 2005 Ville Skyttä <ville.skytta at iki.fi>
- Don't mark the main source file as %%config.
- Make profile.d snippet non-executable (#35714) and noreplace.
- Add mock, plague-client and repomanage completion.
- Allow "cvs stat" completion.
- Macroize trigger creation.

* Fri Jul 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050721-1
- 20050721.

* Wed Jul 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050720-1
- 20050720, all patches applied upstream.

* Mon Jul 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 20050712-1
- 20050712.
- Add more OO.o2 extensions, and *.pdf for evince (#163520, Horst von Brand).
- Add/fix support for some multimedia formats and players.
- Fix tarball completion.

* Sat Jan 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 0:20050121-2
- Update to 20050121.

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

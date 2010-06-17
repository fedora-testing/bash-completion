Name:           bash-completion
Version:        1.2
Release:        1%{?dist}
Epoch:          1
Summary:        Programmable completion for Bash

Group:          System Environment/Shells
License:        GPLv2+
URL:            http://bash-completion.alioth.debian.org/
Source0:        http://bash-completion.alioth.debian.org/files/%{name}-%{version}.tar.bz2
Source1:        %{name}-plague-client
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  dejagnu
BuildRequires:  screen
BuildRequires:  tcllib
Requires:       bash >= 3.2
# For symlinking in triggers, #490768
Requires:       coreutils

%description
bash-completion is a collection of shell functions that take advantage
of the programmable completion feature of bash.


%prep
%setup -q
install -pm 644 %{SOURCE1} contrib/plague-client

# Updated completions shipped upstream:
rm contrib/cowsay
# mock too, but only in >= 1.1.1
# modules too, but only in >= 3.2.7
# subversion too, but only in >= 1.6.5-2
# yum-utils too, but only in >= 1.1.24
# yum too, but only in >= 3.2.25-2

# Combine to per-package files to work around #585384:
cd contrib
( echo ; cat update-alternatives ) >> chkconfig
rm update-alternatives
( echo ; cat sysctl ) >> procps
rm sysctl
( echo ; cat chsh ; echo ; cat mount ; echo ; cat rtcwake ) >> util-linux
rm chsh mount rtcwake
( echo ; cat xrandr ) >> xhost
mv xhost xorg-x11-server-utils ; rm xrandr
cd ..

# Not applicable to Fedora and derivatives:
rm contrib/apache2ctl
rm contrib/apt-build
rm contrib/aptitude
rm contrib/cardctl
rm contrib/heimdal
rm contrib/kldload
rm contrib/lilo
rm contrib/links
rm contrib/lintian
rm contrib/pkg_install
rm contrib/pkgtools
rm contrib/portupgrade
rm contrib/reportbug
rm contrib/sysv-rc

# Not handled due to other reasons (e.g. no known packages) (yet?):
rm contrib/larch
rm contrib/p4


%build
%configure
make bash_completion.sh


%install
rm -rf $RPM_BUILD_ROOT %{name}-ghosts.list

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -pm 644 bash_completion $RPM_BUILD_ROOT%{_sysconfdir}
install -pm 644 bash_completion.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -pm 644 contrib/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

# Always installed (not triggered) completions for practically always
# installed packages or non-triggerable common ones:
for f in bash-builtins configure coreutils dd getent iconv ifupdown \
    module-init-tools rpm service ; do
    mv $RPM_BUILD_ROOT{%{_datadir}/%{name}/$f,%{_sysconfdir}/bash_completion.d}
done

d=$(pwd)
# ghost list
cd $RPM_BUILD_ROOT%{_datadir}/%{name}
for f in * ; do
    ln -s %{_datadir}/%{name}/$f $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
    echo "%ghost %{_sysconfdir}/bash_completion.d/$f" >> $d/%{name}-ghosts.list
done
cd -


%check
# Should be done/fixed upstream
mkdir test/log test/tmp
# For some tests involving non-ASCII filenames
export LANG=en_US.UTF-8
# This stuff borrowed from dejagnu-1.4.4-17 (tests need a terminal)
tmpfile=$(mktemp)
screen -D -m sh -c '( make check ; echo $? ) >'$tmpfile
cat $tmpfile
result=$(tail -n 1 $tmpfile)
rm -f $tmpfile
exit 0 # $result, but we have some pretty certain failures in mock for now...


%clean
rm -rf $RPM_BUILD_ROOT


# Note that this *must* be %%define, not %%global, otherwise the %%{?2}/%%{!?2}
# conditional is apparently evaluated too early (at spec parse time when arg 2
# is never defined)?
%define bashcomp_trigger() \
%triggerin -- %{?2}%{!?2:%1}\
[ -e %{_sysconfdir}/bash_completion.d/%1 ] ||\
    ln -s %{_datadir}/%{name}/%1 %{_sysconfdir}/bash_completion.d || :\
%triggerun -- %{?2}%{!?2:%1}\
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/%1 || :\
%{nil}

%bashcomp_trigger abook
%bashcomp_trigger ant
%bashcomp_trigger apt
%bashcomp_trigger aptitude
%bashcomp_trigger aspell
%bashcomp_trigger autorpm
%bashcomp_trigger bind-utils
%bashcomp_trigger bitkeeper
%bashcomp_trigger bittorrent
%bashcomp_trigger bluez
%bashcomp_trigger brctl bridge-utils
%bashcomp_trigger bzip2
%bashcomp_trigger cfengine
%bashcomp_trigger chkconfig
%bashcomp_trigger cksfv
%bashcomp_trigger clisp
%bashcomp_trigger cpan2dist perl-CPANPLUS
%bashcomp_trigger cpio
%bashcomp_trigger cryptsetup cryptsetup-luks
%bashcomp_trigger cups
%bashcomp_trigger cvs
%bashcomp_trigger cvsps
%bashcomp_trigger dhclient
%bashcomp_trigger dict dictd
%bashcomp_trigger dpkg
%bashcomp_trigger dselect
%bashcomp_trigger dsniff
%bashcomp_trigger findutils
%bashcomp_trigger freeciv
%bashcomp_trigger fuse
%bashcomp_trigger gcc
%bashcomp_trigger gcl
%bashcomp_trigger gdb
%bashcomp_trigger genisoimage
%bashcomp_trigger gkrellm
%bashcomp_trigger gnatmake gcc-gnat
%bashcomp_trigger gpg gnupg
%bashcomp_trigger gpg2 gnupg2
%bashcomp_trigger gzip
%bashcomp_trigger hping2 hping3
%bashcomp_trigger imagemagick ImageMagick
%bashcomp_trigger info
%bashcomp_trigger ipmitool
%bashcomp_trigger ipsec openswan
%bashcomp_trigger iptables
%bashcomp_trigger ipv6calc
%bashcomp_trigger isql unixODBC
%bashcomp_trigger jar java-1.6.0-openjdk-devel
%bashcomp_trigger java java-1.6.0-openjdk
%bashcomp_trigger k3b
%bashcomp_trigger ldapvi
%bashcomp_trigger lftp
%bashcomp_trigger lisp cmucl
%bashcomp_trigger lvm lvm2
%bashcomp_trigger lzma xz-lzma-compat
%bashcomp_trigger lzop
%bashcomp_trigger mailman
%bashcomp_trigger make
%bashcomp_trigger man
%bashcomp_trigger mc
%bashcomp_trigger mcrypt
%bashcomp_trigger mdadm
%bashcomp_trigger medusa
%bashcomp_trigger minicom
%bashcomp_trigger mkinitrd

%triggerin -- mock
if [ -e %{_sysconfdir}/bash_completion.d/mock.bash ] ; then
    # Upstream completion in mock >= 1.1.1
    rm -f %{_sysconfdir}/bash_completion.d/_mock || :
elif [ ! -e %{_sysconfdir}/bash_completion.d/_mock ] ; then
    ln -s %{_datadir}/%{name}/_mock %{_sysconfdir}/bash_completion.d || :
fi
%triggerun -- mock
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/_mock || :

%triggerin -- environment-modules
if [ -e %{_datadir}/Modules/init/bash_completion ] ; then
    # Upstream completion in environment-modules >= 3.2.7
    rm -f %{_sysconfdir}/bash_completion.d/_modules || :
elif [ ! -e %{_sysconfdir}/bash_completion.d/_modules ] ; then
    ln -s %{_datadir}/%{name}/_modules %{_sysconfdir}/bash_completion.d || :
fi
%triggerun -- environment-modules
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/_modules || :

%bashcomp_trigger monodevelop
%bashcomp_trigger mplayer
%bashcomp_trigger msynctool
%bashcomp_trigger mtx
%bashcomp_trigger munin-node
%bashcomp_trigger mutt
%bashcomp_trigger mysqladmin mysql,MySQL-client-community
%bashcomp_trigger ncftp
%bashcomp_trigger net-tools
%bashcomp_trigger nmap
%bashcomp_trigger ntpdate
%bashcomp_trigger openldap openldap-clients
%bashcomp_trigger openssl
%bashcomp_trigger perl
%bashcomp_trigger pine
%bashcomp_trigger pkg-config pkgconfig
%bashcomp_trigger plague-client
%bashcomp_trigger pm-utils
%bashcomp_trigger postfix
%bashcomp_trigger postgresql
%bashcomp_trigger povray
%bashcomp_trigger procps
%bashcomp_trigger python
%bashcomp_trigger qdbus qt,kdelibs3
%bashcomp_trigger qemu
%bashcomp_trigger quota-tools quota
%bashcomp_trigger rcs
%bashcomp_trigger rdesktop
%bashcomp_trigger resolvconf
%bashcomp_trigger rfkill
%bashcomp_trigger ri ruby-ri
%bashcomp_trigger rpcdebug nfs-utils
%bashcomp_trigger rpmcheck
%bashcomp_trigger rrdtool
%bashcomp_trigger rsync
%bashcomp_trigger samba samba-common
%bashcomp_trigger sbcl
%bashcomp_trigger screen
%bashcomp_trigger shadow shadow-utils
%bashcomp_trigger sitecopy
%bashcomp_trigger smartctl smartmontools
%bashcomp_trigger snownews
%bashcomp_trigger ssh openssh-clients
%bashcomp_trigger sshfs fuse-sshfs
%bashcomp_trigger strace

%triggerin -- subversion
if [ -e %{_sysconfdir}/bash_completion.d/subversion ] ; then
    # Upstream completion in subversion >= 1.6.5-2
    rm -f %{_sysconfdir}/bash_completion.d/_subversion || :
elif [ ! -e %{_sysconfdir}/bash_completion.d/_subversion ] ; then
    ln -s %{_datadir}/%{name}/_subversion %{_sysconfdir}/bash_completion.d || :
fi
%triggerun -- subversion
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/_subversion || :

%bashcomp_trigger svk perl-SVK
%bashcomp_trigger tar
%bashcomp_trigger tcpdump
%bashcomp_trigger unace
%bashcomp_trigger unrar
%bashcomp_trigger util-linux util-linux-ng,util-linux
%bashcomp_trigger vncviewer tigervnc,vnc
%bashcomp_trigger vpnc
%bashcomp_trigger wireless-tools
%bashcomp_trigger wodim
%bashcomp_trigger wol
%bashcomp_trigger wtf bsd-games
%bashcomp_trigger wvdial
%bashcomp_trigger xm xen
%bashcomp_trigger xmllint libxml2
%bashcomp_trigger xmlwf expat
%bashcomp_trigger xmms
%bashcomp_trigger xorg-x11-server-utils
%bashcomp_trigger xsltproc libxslt
%bashcomp_trigger xz
%bashcomp_trigger yp-tools

%triggerin -- yum
if [ -e %{_sysconfdir}/bash_completion.d/yum.bash ] ; then
    # Upstream completion in yum >= 3.2.25-2
    rm -f %{_sysconfdir}/bash_completion.d/_yum || :
elif [ ! -e %{_sysconfdir}/bash_completion.d/_yum ] ; then
    ln -s %{_datadir}/%{name}/_yum %{_sysconfdir}/bash_completion.d || :
fi
%triggerun -- yum
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/_yum || :

%triggerin -- yum-utils
if [ -e %{_sysconfdir}/bash_completion.d/yum-utils.bash ] ; then
    # Upstream completion in yum-utils >= 1.1.24
    rm -f %{_sysconfdir}/bash_completion.d/_yum-utils || :
elif [ ! -e %{_sysconfdir}/bash_completion.d/_yum-utils ] ; then
    ln -s %{_datadir}/%{name}/_yum-utils %{_sysconfdir}/bash_completion.d || :
fi
%triggerun -- yum-utils
[ $2 -gt 0 ] || rm -f %{_sysconfdir}/bash_completion.d/_yum-utils || :

%bashcomp_trigger yum-arch


%files -f %{name}-ghosts.list
%defattr(-,root,root,-)
%doc AUTHORS CHANGES COPYING README TODO
%config(noreplace) %{_sysconfdir}/profile.d/bash_completion.sh
%{_sysconfdir}/bash_completion
%dir %{_sysconfdir}/bash_completion.d/
%{_sysconfdir}/bash_completion.d/bash-builtins
%{_sysconfdir}/bash_completion.d/configure
%{_sysconfdir}/bash_completion.d/coreutils
%{_sysconfdir}/bash_completion.d/dd
%{_sysconfdir}/bash_completion.d/getent
%{_sysconfdir}/bash_completion.d/iconv
%{_sysconfdir}/bash_completion.d/ifupdown
%{_sysconfdir}/bash_completion.d/module-init-tools
%{_sysconfdir}/bash_completion.d/rpm
%{_sysconfdir}/bash_completion.d/service
%{_datadir}/%{name}/


%changelog
* Wed Jun 16 2010 Ville Skyttä <ville.skytta@iki.fi> - 1:1.2-1
- Update to 1.2, all patches applied upstream.
- Fixes #444469, #538433, #541423, and #601813, works around #585384.

* Fri Mar 12 2010 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-7
- Autoinstall dpkg and dselect completions.

* Thu Mar 11 2010 Todd Zullinger <tmz@pobox.com> - 1:1.1-6
- Apply upstream post 1.1 service argument fix (#572794).

* Sat Dec 26 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-5
- Apply upstream post 1.1 generic vncviewer fixes.
- Autoinstall vncviewer completion also on tigervnc.
- Autoinstall chsh completion also on util-linux.

* Tue Dec 15 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-4
- Fix autoinstall of completions named other than the package (#546905).
- Use environment-modules upstream completion instead of ours if available.
- Autoinstall mysqladmin completion also on MySQL-client-community.

* Tue Nov 17 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-3
- Prepare for smooth coexistence with yum upstream completion.

* Sun Nov  8 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-2
- Use yum-utils completion instead of ours if available.

* Mon Oct 19 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.1-1
- Update to 1.1.
- bash 4 quoting fix, mock and repomanage completions included upstream.

* Sun Sep 20 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.0-5
- Use svn completion from subversion instead of ours if available (#496456).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.0-3
- Do not install cowsay completion, an updated version is shipped with it.

* Tue Apr  7 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.0-2
- Apply upstream patch to fix quoting issues with bash 4.x (#490322).

* Mon Apr  6 2009 Ville Skyttä <ville.skytta@iki.fi> - 1:1.0-1
- 1.0.

* Mon Mar 23 2009 Ville Skyttä <ville.skytta@iki.fi> - 20080705-4.20090314gitf4f0984
- Add dependency on coreutils for triggers (#490768).
- Update and improve mock completion.

* Sun Mar 15 2009 Ville Skyttä <ville.skytta@iki.fi> - 20080705-3.20090314gitf4f0984
- git snapshot f4f0984, fixes #484578 (another issue), #486998.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080705-3.20090211git47d0c5b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Ville Skyttä <ville.skytta@iki.fi> - 20080705-2.20090211git47d0c5b
- git snapshot 47d0c5b, fixes #484578.
- lzop and repomanage completions included upstream.

* Sun Jan 18 2009 Ville Skyttä <ville.skytta@iki.fi> - 20080705-2.20090115bzr1252
- r1252 snapshot; all patches applied upstream.
- Do not install mercurial completion, an updated version is shipped with it.
- Improve lzop and repomanage completion.

* Tue Jan  6 2009 Ville Skyttä <ville.skytta@iki.fi> - 20080705-1
- 20080705; new upstream at http://bash-completion.alioth.debian.org/
- Perl, Debian, and scp patches applied upstream.
- Patch to improve man completion: more sections, better filename handling.
- Patch to speed up yum install/deplist completion (#478784).
- Patch to fix and speed up rpm installed packages completion.
- Update mock completion.

* Thu Sep 25 2008 Ville Skyttä <ville.skytta@iki.fi>
- More Matroska associations (#463829, based on patch from Yanko Kaneti).

* Thu Sep 11 2008 Ville Skyttä <ville.skytta@iki.fi> - 20060301-13
- Borrow/improve/adapt to Fedora some patches from Mandriva: improved support
  for getent and rpm --eval, better rpm backup file avoidance, lzma support.
- Patch/unpatch to fix gzip and bzip2 options completion.
- Patch to add --rsyncable to gzip options completion.
- Add and trigger-install support for lzop.
- Associate *.sqlite with sqlite3.

* Wed Jul 23 2008 Ville Skyttä <ville.skytta@iki.fi> - 20060301-12
- Fix plague-client completion install (#456355, Ricky Zhou).
- Trigger-install support for sitecopy.

* Tue Apr 29 2008 Ville Skyttä <ville.skytta@iki.fi> - 20060301-11
- Media player association improvements (#444467).

* Sat Feb 23 2008 Ville Skyttä <ville.skytta@iki.fi> - 20060301-10
- Patch to fix filename completion with svn (#430059).
- Trigger-install support for dsniff.
- Drop disttag.

* Mon Dec 31 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060301-8
- Associate VDR recording files with media players.
- Update mock completion.

* Fri Nov 16 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060301-7
- Add JPEG2000 extensions for display(1) (#304771).
- Update mock completion.

* Sat Sep 22 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060301-6
- Patch to improve perl completion (#299571, Jim Radford,
  http://use.perl.org/~Alias/journal/33508).

* Mon Aug 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060301-5
- License: GPLv2+

* Sun Jun 24 2007 Jeff Sheltren <sheltren@cs.ucsb.edu> - 20060301-4
- Update triggers to work with older versions of RPM

* Wed Feb 28 2007 Ville Skyttä <ville.skytta@iki.fi> - 20060301-3
- Fix scp with single quotes (#217178).
- Borrow fix for bzip2 w/spaces, and apropos and whatis support from Debian.

* Thu Aug 31 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060301-2
- Trigger-install support for gcl, lilypond, mercurial and svk.
- Improve mock completion a bit.

* Thu Mar  2 2006 Ville Skyttä <ville.skytta@iki.fi> - 20060301-1
- 20060301, patches and profile.d scriptlet applied/included upstream.
- Convert docs to UTF-8.

* Wed Feb  8 2006 Ville Skyttä <ville.skytta@iki.fi> - 20050721-4
- Don't source ourselves in non-interactive shells (#180419, Behdad Esfahbod).
- Trigger-install snippets for clisp, gnatmake, isql, ri, sbcl, and snownews.

* Sat Feb  4 2006 Ville Skyttä <ville.skytta@iki.fi>
- Add mtr(8) completion using known hosts (#179918, Yanko Kaneti).

* Sun Jan  8 2006 Ville Skyttä <ville.skytta@iki.fi> - 20050721-3
- Patch to hopefully fix quoting problems with bash 3.1 (#177056).

* Mon Nov 28 2005 Ville Skyttä <ville.skytta@iki.fi> - 20050721-2
- Work around potential login problem in profile.d snippet (#174355).

* Sat Nov 26 2005 Ville Skyttä <ville.skytta@iki.fi>
- Don't mark the main source file as %%config.
- Make profile.d snippet non-executable (#35714) and noreplace.
- Add mock, plague-client and repomanage completion.
- Allow "cvs stat" completion.
- Macroize trigger creation.

* Fri Jul 22 2005 Ville Skyttä <ville.skytta@iki.fi> - 20050721-1
- 20050721.

* Wed Jul 20 2005 Ville Skyttä <ville.skytta@iki.fi> - 20050720-1
- 20050720, all patches applied upstream.

* Mon Jul 18 2005 Ville Skyttä <ville.skytta@iki.fi> - 20050712-1
- 20050712.
- Add more OO.o2 extensions, and *.pdf for evince (#163520, Horst von Brand).
- Add/fix support for some multimedia formats and players.
- Fix tarball completion.

* Sat Jan 22 2005 Ville Skyttä <ville.skytta@iki.fi> - 0:20050121-2
- Update to 20050121.

* Thu Jan 13 2005 Ville Skyttä <ville.skytta@iki.fi> - 0:20050112-1
- Update to 20050112, openssl patch applied upstream.

* Wed Jan  5 2005 Ville Skyttä <ville.skytta@iki.fi> - 0:20050103-1
- Update to 20050103.

* Sat Nov 27 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:20041017-5
- Change version scheme, bump release to provide Extras upgrade path.

* Sat Nov  6 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.4.20041017
- Do the right thing with bash >= 3 too in profile.d snippet (bug 2228, thanks
  to Thorsten Leemhuis).

* Mon Oct 18 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20041017
- Update to 20041017, adds dhclient, lvm, and bittorrent completion.

* Mon Jul 12 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20040711
- Update to 20040711, patches applied upstream.

* Sun Jul  4 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20040704
- Update to 20040704.
- Change to symlinked /etc/bash_completion.d snippets, add patch to read them.

* Wed May 26 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20040526
- Update to 20040526.

* Thu Apr  1 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.3.20040331
- Add command-specific contrib snippet copying triggers.

* Thu Apr  1 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20040331
- Update to 20040331.

* Sun Feb 15 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20040214
- Update to 20040214.

* Wed Feb 11 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20040210
- Update to 20040210.

* Fri Jan  2 2004 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20040101
- Update to 20040101.
- Update %%description.

* Sat Dec 27 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20031225
- Update to 20031225.

* Sat Dec 20 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.2.20031215
- Don't pull in *.rpm* from %%{_sysconfdir}/bash_completion.d.

* Mon Dec 15 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20031215
- Update to 20031215.

* Sun Nov 30 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20031125
- Update to 20031125.

* Thu Nov 13 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20031112
- Update to 20031112.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20031022
- Update to 20031022.

* Tue Oct  7 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20031007
- Update to 20031007.

* Tue Sep 30 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20030929
- Update to 20030929.

* Fri Sep 12 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20030911
- Update to 20030911.

* Thu Aug 21 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20030821
- Update to 20030821.
- Drop .nosrc.rpm patch, already applied upstream.

* Sat Aug 16 2003 Ville Skyttä <ville.skytta@iki.fi> 0:0.0-0.fdr.1.20030811
- Update to 20030811.
- Patch to make rpm --rebuild work with .nosrc.rpm's.

* Sun Aug  3 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030803
- Update to 20030803.

* Wed Jul 23 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030721
- Update to 20030721.

* Sun Jul 13 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030713
- Update to 20030713.

* Mon Jun 30 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030630
- Update to 20030630.

* Sun Jun  8 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030607
- Update to 20030607.

* Tue May 27 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030527
- Update to 20030527.

* Sat May 24 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:0.0-0.fdr.1.20030505
- First build.

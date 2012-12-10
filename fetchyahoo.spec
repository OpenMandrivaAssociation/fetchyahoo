Summary: Downloads mail from an Yahoo! webmail account
Name: fetchyahoo

Version: 2.14.2

Release: %mkrel 1
URL: http://fetchyahoo.twizzler.org
Source: http://fetchyahoo.twizzler.org/%{name}-%{version}.tar.gz
License: GPL
Group: Networking/Mail
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch
Requires: perl
Requires: perl-LWP-Protocol-https

%description
FetchYahoo is a Perl script that downloads mail from a Yahoo! webmail
account to a local mail spool, an mbox file, or to procmail. It is
meant to replace fetchmail for people using Yahoo! mail since Yahoo!'s
POP and email forwarding services are no longer free. It includes all
parts and attachments within the email. It can also forward the email
to a specified address.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1
cp -a fetchyahoo $RPM_BUILD_ROOT%_bindir/fetchyahoo
cp -a fetchyahoo.1 $RPM_BUILD_ROOT%_mandir/man1/fetchyahoo.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING INSTALL TODO index.html fetchyahoorc ChangeLog Credits
%_bindir/fetchyahoo
%_mandir/man1/fetchyahoo.*




%changelog
* Sun Jan 22 2012 Glen Ogilvie <nelg@mandriva.org> 2.14.2-1mdv2012.0
+ Revision: 764884
- Fix for bypassing opt-out screen

* Sat Jan 07 2012 Glen Ogilvie <nelg@mandriva.org> 2.14.1-1
+ Revision: 758582
- + New release: v2.14.1
- add support for SMTP authentication
- new configuration options
- updated support for Yahoo Mail

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.13.8-2mdv2011.0
+ Revision: 610423
- rebuild

* Mon Feb 08 2010 Frederik Himpe <fhimpe@mandriva.org> 2.13.8-1mdv2010.1
+ Revision: 502369
- update to new version 2.13.8

* Wed Sep 23 2009 Glen Ogilvie <nelg@mandriva.org> 2.13.7-1mdv2010.0
+ Revision: 447690
- fix retrieving messages (thanks Jon Baumgartner)

* Wed Aug 12 2009 Glen Ogilvie <nelg@mandriva.org> 2.13.6-1mdv2010.0
+ Revision: 415496
- fix getting message IDs for read messages

* Sat May 30 2009 Glen Ogilvie <nelg@mandriva.org> 2.13.5-1mdv2010.0
+ Revision: 381204
- updated to current version. All older releases do not work correctly with yahoo mail.

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 2.12.4-1mdv2009.1
+ Revision: 341533
- New upstream release

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.11.2-3mdv2009.0
+ Revision: 245104
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.11.2-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Jérôme Soyer <saispo@mandriva.org> 2.11.2-1mdv2008.0
+ Revision: 80722
- New release 2.11.2

* Fri Aug 31 2007 Jérôme Soyer <saispo@mandriva.org> 2.11.1-1mdv2008.0
+ Revision: 76844
- New release 2.11.1

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Thu Jul 20 2006 Jerome Soyer <saispo@mandriva.org> 2.10.3-1mdv200.7
- New release 2.10.3

* Mon Jan 23 2006 Jerome Soyer <saispo@mandriva.org> 2.10.2-1mdk
- New release 2.10.2
- Rebuild for new perl

* Tue Nov 16 2004 Jerome Soyer <saispo@mandrake.org> 2.8.6-2mdk
- Rebuild for new perl

* Tue Sep 28 2004 Jerome Soyer <saispo@mandrake.org> 2.8.6-1mdk
- 2.8.6

* Tue Sep 21 2004 Jerome Soyer <saispo@mandrake.org> 2.8.5-1mdk
- 2.8.5

* Sun Sep 05 2004 Jerome Soyer <saispo@mandrake.org> 2.8.3-1mdk
- 2.8.3

* Thu Aug 05 2004 Jerome Soyer <jeromesoyer@yahoo.fr> 2.8.2-1mdk
- 2.8.2

* Wed Apr 21 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.8.0-1mdk
- 2.8.0


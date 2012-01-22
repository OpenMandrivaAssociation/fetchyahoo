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



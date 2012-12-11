Name:         steak
Url:          http://www.informatik.uni-frankfurt.de/~razi/steak/steak.html
License:      GPLv2+
Group:        System/Internationalization
Summary:      English <-> German translator
Version:      1.7.3
Release: %mkrel 12
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Source0:      Steak.%version.tar.bz2
Patch0:       Steak-1.7.3-install.patch
Patch1:	      steak-1.7.3-aspell.patch
Patch2:	      Steak-recode-printbuffer-to-utf8.patch
BuildRequires:	X11-devel
BuildRequires:	recode
Requires: aspell-de
Requires: aspell-en
Requires: recode

%description
steak translates and explain words. You can use it to translate
between German and English on the command line. It will even translate
the word you've selected under X when you call steak without
arguments.

%prep
%setup -q -n Steak
%patch0 -p 0 -E
%patch1 -p0 -b .aspell
%patch2 -p1
find -type d | xargs chmod 755
perl -pi -e "s!xxxLIBDIRx!%_libdir!" steak_install.sh
recode l9..u8 iso2txt 
recode l9..u8 Datensatz/ger-eng.txt

%build
make X11LIBDIR="-L%{_prefix}/X11R6/%_lib"

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_libdir}/Steak/
echo | %makeinstall_std

cat > README.urpmi <<EOF
Anpassungen spezifisch für das Mandriva-Paket

Die Datenbank und das Programm wurden so umgestellt, dass es nur noch in der
UTF-8-Kodierung funktioniert, die inzwischen Standard ist. Die ursprüngliche
Version funktionierte nur mit ISO-8859-1.


Mandriva RPM specific notes

The database and the program were changed to work in the UTF-8 encoding only. 
This is the current default. The original version only worked in ISO-8859-1.
EOF


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README* INSTALL INSTALL.ger ChangeLog
%{_bindir}/*
%{_libdir}/Steak


%changelog
* Thu Dec 08 2011 Götz Waschk <waschk@mandriva.org> 1.7.3-12mdv2012.0
+ Revision: 738851
- yearly rebuild

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.7.3-11mdv2011.0
+ Revision: 614979
- the mass rebuild of 2010.1 packages

* Wed Jan 27 2010 Götz Waschk <waschk@mandriva.org> 1.7.3-10mdv2010.1
+ Revision: 496984
- convert everything to UTF-8
- add Mandriva specific README
- uncompress old patches

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 1.7.3-9mdv2010.0
+ Revision: 407719
- update the license
- update URL
- spec file fix

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.7.3-8mdv2009.0
+ Revision: 261172
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.7.3-7mdv2009.0
+ Revision: 253542
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.7.3-5mdv2008.1
+ Revision: 136523
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 1.7.3-5mdv2008.0
+ Revision: 55245
- Import steak



* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 1.7.3-5mdk
- Rebuild

* Mon Jan 09 2006 Götz Waschk <waschk@mandriva.org> 1.7.3-4mdk
- Rebuild
- use mkrel

* Sat Jan  8 2005 G�tz Waschk <waschk@linux-mandrake.com> 1.7.3-3mdk
- rebuild

* Tue Dec 16 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.7.3-2mdk
- require German and English dictionaries
- patch to use aspell instead of ispell

* Thu Nov 27 2003 G�tz Waschk <waschk@linux-mandrake.com> 1.7.3-1mdk
- initial Mandrake package based on a SUSE package

* Fri Feb 14 2003 - adrian@suse.de
- update to version 1.7.3
* Mon Nov 11 2002 - ro@suse.de
- use x-devel-packages in neededforbuild
* Fri Jul 26 2002 - adrian@suse.de
- fix build
* Wed Jul 24 2002 - adrian@suse.de
- clean #neededforbuild
- used BuildRoot
* Mon Jun 24 2002 - ro@suse.de
- fix directory permissions
* Mon May 27 2002 - ro@suse.de
- fix build for lib64 platforms
* Wed Jan 30 2002 - sf@suse.de
- added alpha.diff (changed return type from 'main' from void to int)
* Fri Feb 02 2001 - adrian@suse.de
- Spec file created from Steak.1.7.2.tar.bz2 by autospec

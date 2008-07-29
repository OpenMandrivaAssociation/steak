Name:         steak
Url:          http://www.tm.informatik.uni-frankfurt.de/~razi/steak/steak.html
License:      GPL
Group:        System/Internationalization
Summary:      English <-> German translator
Version:      1.7.3
Release: %mkrel 7
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Source0:      Steak.%version.tar.bz2
Patch0:       Steak-1.7.3-install.patch.bz2
Patch1:	      steak-1.7.3-aspell.patch.bz2	
BuildRequires:	X11-devel
Requires: aspell-de
Requires: aspell-en

%description
steak translates and explain words. You can use it to translate
between German and English on the command line. It will even translate
the word you've selected under X when you call steak without
arguments.

%prep
%setup -q -n Steak
%patch -p 0 -E
%patch1 -p0 -b .aspell
find -type d | xargs chmod 755
perl -pi -e "s!xxxLIBDIRx!%_libdir!" steak_install.sh

%build
make X11LIBDIR="-L%{_prefix}/X11R6/%_lib"

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%{_libdir}/Steak/
echo | %makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README README.eng INSTALL INSTALL.ger ChangeLog 
%{_bindir}/*
%{_libdir}/Steak

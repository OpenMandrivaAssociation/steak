Name:         steak
Url:          https://www.informatik.uni-frankfurt.de/~razi/steak/steak.html
License:      GPLv2+
Group:        System/Internationalization
Summary:      English <-> German translator
Version:      1.7.3
Release:      14
Source0:      Steak.%{version}.tar.bz2
Patch0:       Steak-1.7.3-install.patch
Patch1:	      steak-1.7.3-aspell.patch
Patch2:	      Steak-recode-printbuffer-to-utf8.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xt)
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
mkdir -p %{buildroot}%{_libdir}/Steak/
echo | %makeinstall_std

cat > README.urpmi <<EOF
Anpassungen spezifisch fÃ¼r das Mandriva-Paket

Die Datenbank und das Programm wurden so umgestellt, dass es nur noch in der
UTF-8-Kodierung funktioniert, die inzwischen Standard ist. Die ursprÃ¼ngliche
Version funktionierte nur mit ISO-8859-1.


Mandriva RPM specific notes

The database and the program were changed to work in the UTF-8 encoding only. 
This is the current default. The original version only worked in ISO-8859-1.
EOF


%files
%doc README* INSTALL INSTALL.ger ChangeLog
%{_bindir}/*
%{_libdir}/Steak

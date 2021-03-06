Summary:	Assembly Language Debugger
Summary(pl.UTF-8):	Debugger dla asemblera
Name:		ald
Version:	0.1.7
Release:	5
License:	GPL v2
Group:		Development
Source0:	http://dl.sourceforge.net/ald/%{name}-%{version}.tar.gz
# Source0-md5:	dc9839014ea9308146142ab84efbbd46
URL:		http://ald.sourceforge.net/
BuildRequires:	readline-devel >= 4.2
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Assembly Language Debugger is a tool for debugging executable
programs at the assembly level. It currently runs only on Intel x86
platforms.

%description -l pl.UTF-8
Assembly Language Debugger jest narzędziem służącym odpluskwianiu
wykonywalnych programów na poziomie asemblera. Obecnie działa jedynie
na platformie x86.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/%{name}.*

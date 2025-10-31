Name:           gnome-pass-search-provider
Version:        master
Release:        1
License:        GPL-3.0+
Summary:        Gnome Shell search provider for zx2c4/pass
Url:            https://github.com/jle64/gnome-pass-search-provider
Source:         https://github.com/jle64/%{name}/archive/master.tar.gz
Requires:       gnome-shell
Requires:       pass
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-Levenshtein
%if 0%{?fedora} >= 43
Requires:       python3-rapidfuzz
%else
Requires:       python3-fuzzywuzzy
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%global debug_package %{nil}

%description
A Gnome Shell passwords search provider for zx2c4/pass (passwordstore.org) or compatibles and Bitwarden/Vaultwarden that sends passwords to clipboard (or GPaste).

%prep
%setup -q -n %{name}-%{version}

%build

%install
sed -i -e 's|DATADIR=|DATADIR=$RPM_BUILD_ROOT|' install.sh
sed -i -e 's|LIBDIR=|LIBDIR=$RPM_BUILD_ROOT|' install.sh
./install.sh

%files
%defattr(-,root,root,-)
%doc README.md
%{_prefix}/lib/gnome-pass-search-provider/gnome-pass-search-provider.py
%{_prefix}/lib/systemd/user/org.gnome.Pass.SearchProvider.service
%{_prefix}/share/dbus-1/services/org.gnome.Pass.SearchProvider.service
%{_prefix}/share/applications/org.gnome.Pass.SearchProvider.desktop
%{_prefix}/share/gnome-shell/search-providers/org.gnome.Pass.SearchProvider.ini

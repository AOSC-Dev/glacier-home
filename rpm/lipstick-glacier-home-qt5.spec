# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       lipstick-glacier-home-qt5

# >> macros
# << macros

Summary:    A nice homescreen for Glacier experience
Version:    0.0.0
Release:    1
Group:      System/GUI/Other
License:    BSD
URL:        https://github.com/locusf/glacier-home
Source0:    %{name}-%{version}.tar.bz2
Source1:    lipstick.desktop
Source2:    lipstick.service
Source100:  lipstick-glacier-home-qt5.yaml
Requires:   lipstick-qt5 >= 0.17.0
Requires:   nemo-qml-plugin-configuration-qt5
Requires:   nemo-qml-plugin-time-qt5
Requires:   qt5-qtdeclarative-import-window2
Requires:   qt5-qtquickcontrols-nemo
Requires:   nemo-qml-plugin-contextkit-qt5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(lipstick-qt5) >= 0.12.0
BuildRequires:  pkgconfig(Qt5Compositor)
Conflicts:   lipstick-example-home

%description
A homescreen for Nemo Mobile

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install
mkdir -p %{buildroot}%{_libdir}/systemd/user/
cp -a %{SOURCE2} %{buildroot}%{_libdir}/systemd/user/


# >> install post
install -D -m 644 %{SOURCE1} %{buildroot}/etc/xdg/autostart/lipstick.desktop
mkdir -p %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/
ln -s ../lipstick.service %{buildroot}%{_libdir}/systemd/user/user-session.target.wants/lipstick.service
# << install post

%files
%defattr(-,root,root,-)
%{_bindir}/lipstick
%{_libdir}/systemd/user/lipstick.service
%config /etc/xdg/autostart/*.desktop
%{_datadir}/lipstick/lipstick.conf
%{_libdir}/systemd/user/user-session.target.wants/lipstick.service
# >> files
# << files

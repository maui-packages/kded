# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-kded

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 3 addon with KDE Daemon
Version:    5.0.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kded.yaml
Source101:  kf5-kded-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kinit-devel
BuildRequires:  kf5-kservice-devel

%description
KDE Frameworks 5 Tier 3 addon with KDE Daemon


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-kconfig-devel
Requires:   kf5-kcoreaddons-devel
Requires:   kf5-kcrash-devel
Requires:   kf5-kdbusaddons-devel
Requires:   kf5-kdoctools-devel
Requires:   kf5-kinit-devel
Requires:   kf5-kservice-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_bindir}/kded5
%{_kf5_libdir}/libkdeinit5_kded5.so
%{_kf5_datadir}/dbus-1/services/*.service
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_mandir}/man8/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/cmake/KDED
%{_kf5_datadir}/dbus-1/interfaces/*.xml
# >> files devel
# << files devel

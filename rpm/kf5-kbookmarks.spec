%global kf5_version 5.105.0
%global framework kbookmarks

Name: opt-kf5-%{framework}
Version: 5.105.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 3 addon for bookmarks manipulation

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}
Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros
BuildRequires: opt-kf5-kcodecs-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfig-devel >= %{kf5_version}
BuildRequires: opt-kf5-kconfigwidgets-devel >= %{kf5_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
BuildRequires: opt-kf5-kxmlgui-devel >= %{kf5_version}

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-kf5-kcodecs >= %{kf5_version}
Requires: opt-kf5-kconfig >= %{kf5_version}
Requires: opt-kf5-kconfigwidgets >= %{kf5_version}
Requires: opt-kf5-kcoreaddons >= %{kf5_version}
Requires: opt-kf5-kwidgetsaddons >= %{kf5_version}

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: opt-qt5-qtbase-devel
Requires: opt-kf5-kwidgetsaddons-devel >= %{kf5_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../

%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kbookmarks5_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_opt_kf5_libdir}/libKF5Bookmarks.so.*
%{_opt_kf5_datadir}/locale/

%files devel

%{_opt_kf5_includedir}/KF5/KBookmarks/
%{_opt_kf5_libdir}/libKF5Bookmarks.so
%{_opt_kf5_libdir}/cmake/KF5Bookmarks/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KBookmarks.pri


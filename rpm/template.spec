Name:           ros-indigo-eus-assimp
Version:        0.1.13
Release:        0%{?dist}
Summary:        ROS eus_assimp package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-assimp-devel
Requires:       ros-indigo-roseus
BuildRequires:  pkgconfig
BuildRequires:  ros-indigo-assimp-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-euslisp

%description
eus_assimp

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Aug 31 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.13-0
- Autogenerated by Bloom

* Thu May 07 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.12-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.11-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.10-0
- Autogenerated by Bloom

* Thu Apr 02 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.9-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.8-0
- Autogenerated by Bloom

* Fri Dec 19 2014 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.7-1
- Autogenerated by Bloom

* Fri Dec 19 2014 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.7-0
- Autogenerated by Bloom

* Fri Dec 19 2014 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.6-0
- Autogenerated by Bloom


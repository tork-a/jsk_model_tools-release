Name:           ros-jade-jsk-model-tools
Version:        0.2.1
Release:        3%{?dist}
Summary:        ROS jsk_model_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_model_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-eus-assimp
Requires:       ros-jade-euscollada
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains model_tools package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Dec 08 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.1-3
- Autogenerated by Bloom

* Mon Dec 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.1-2
- Autogenerated by Bloom

* Thu Dec 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.1-1
- Autogenerated by Bloom

* Mon Nov 30 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Nov 05 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.13-4
- Autogenerated by Bloom

* Wed Nov 04 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.13-3
- Autogenerated by Bloom

* Tue Nov 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.13-2
- Autogenerated by Bloom

* Tue Nov 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.13-1
- Autogenerated by Bloom


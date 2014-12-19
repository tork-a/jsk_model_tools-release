Name:           ros-indigo-euscollada
Version:        0.1.7
Release:        0%{?dist}
Summary:        ROS euscollada package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/euscollada
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       qhull-devel
Requires:       ros-indigo-assimp-devel
Requires:       ros-indigo-collada-parser
Requires:       ros-indigo-collada-urdf
Requires:       ros-indigo-resource-retriever
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospack
Requires:       ros-indigo-tf
Requires:       ros-indigo-urdf
Requires:       urdfdom-devel
Requires:       yaml-cpp-devel
BuildRequires:  collada-dom-devel
BuildRequires:  qhull-devel
BuildRequires:  ros-indigo-assimp-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-collada-parser
BuildRequires:  ros-indigo-collada-urdf
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-resource-retriever
BuildRequires:  ros-indigo-rosboost-cfg
BuildRequires:  ros-indigo-rosbuild
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospack
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  yaml-cpp-devel

%description
euscollada

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
* Fri Dec 19 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.7-0
- Autogenerated by Bloom

* Fri Dec 19 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.6-0
- Autogenerated by Bloom


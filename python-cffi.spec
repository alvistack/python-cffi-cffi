# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-cffi
Epoch: 100
Version: 1.15.1
Release: 1%{?dist}
Summary: Foreign Function Interface for Python to call C code
License: MIT
URL: https://github.com/python-cffi/cffi/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: libffi-devel
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-cffi
Summary: Foreign Function Interface for Python to call C code
Requires: python3
Requires: python3-pycparser
Provides: python3-cffi = %{epoch}:%{version}-%{release}
Provides: python3dist(cffi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cffi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cffi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cffi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cffi) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%files -n python%{python3_version_nodots}-cffi
%license LICENSE
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-cffi
Summary: Foreign Function Interface for Python to call C code
Requires: python3
Requires: python3-pycparser
Provides: python3-cffi = %{epoch}:%{version}-%{release}
Provides: python3dist(cffi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cffi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cffi) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cffi = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cffi) = %{epoch}:%{version}-%{release}

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.

%files -n python3-cffi
%license LICENSE
%{python3_sitearch}/_cffi_backend.*.so
%{python3_sitearch}/cffi*
%endif

%changelog

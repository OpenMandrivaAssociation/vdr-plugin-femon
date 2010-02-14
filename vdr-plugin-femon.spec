
%define plugin	femon
%define name	vdr-plugin-%plugin
%define version	1.6.7
%define rel	4

Summary:	VDR plugin: DVB Signal Information Monitor (OSD)
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://www.saunalahti.fi/~rahrenbe/vdr/femon/
Source:		http://www.saunalahti.fi/~rahrenbe/vdr/femon/files/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
DVB Frontend Status Monitor is a plugin that displays some signal information
parameters of the current tuned channel on OSD. You can zap through all your
channels and the plugin should be monitoring always the right frontend. The
transponder and stream information are also available in advanced display
modes.

The plugin is based on a neat console frontend status monitor application
called 'femon' by Johannes Stezenbach (see DVB-apps/szap/femon.c for further
information). The bitrate calculation trick originates from the 'dvbstream'
application by Dave Chapman and the stream information routines are taken from
the 'libdvb' library by Metzler Brothers.

%package -n vdr-%plugin-devel
Summary:	Development headers of femon VDR plugin
Group:		Development/C++
Requires:	vdr-devel

%description -n vdr-%plugin-devel
Headers for developing VDR plugins that use services provided by femon.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build STRIP=/bin/true

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_includedir}/vdr/%{plugin}
install -m644 femonservice.h %{buildroot}%{_includedir}/vdr/%{plugin}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY

%files -n vdr-%plugin-devel
%defattr(-,root,root)
%dir %{_includedir}/vdr/%{plugin}
%{_includedir}/vdr/%{plugin}/femonservice.h


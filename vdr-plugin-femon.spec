
%define plugin	femon
%define name	vdr-plugin-%plugin
%define version	1.1.3
%define rel	4

Summary:	VDR plugin: DVB Signal Information Monitor (OSD)
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.saunalahti.fi/~rahrenbe/vdr/femon/
Source:		http://www.saunalahti.fi/~rahrenbe/vdr/femon/files/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.4.1-6
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

%prep
%setup -q -n %plugin-%version

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY



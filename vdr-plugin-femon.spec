
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



%changelog
* Sun Feb 14 2010 Anssi Hannula <anssi@mandriva.org> 1.6.7-4mdv2010.1
+ Revision: 505937
- add vdr-femon-devel subpackage containing service header
- rebuild due to BS building the previous release against wrong VDR on i586

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 1.6.7-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Tue Jul 14 2009 Anssi Hannula <anssi@mandriva.org> 1.6.7-1mdv2010.0
+ Revision: 395753
- new version
- update license tag

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 1.6.0-3mdv2009.1
+ Revision: 359317
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-2mdv2009.0
+ Revision: 197929
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 1.6.0-1mdv2009.0
+ Revision: 197663
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix debug packages

* Sun Jan 20 2008 Anssi Hannula <anssi@mandriva.org> 1.1.5-1mdv2008.1
+ Revision: 155386
- new version

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 1.1.3-5mdv2008.1
+ Revision: 145095
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 1.1.3-4mdv2008.1
+ Revision: 103094
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 1.1.3-3mdv2008.0
+ Revision: 50000
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 1.1.3-2mdv2008.0
+ Revision: 42086
- rebuild for new vdr

* Sat May 19 2007 Anssi Hannula <anssi@mandriva.org> 1.1.3-1mdv2008.0
+ Revision: 28390
- 1.1.3

* Fri May 11 2007 Anssi Hannula <anssi@mandriva.org> 1.1.2-1mdv2008.0
+ Revision: 26320
- 1.1.2

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 1.1.1-2mdv2008.0
+ Revision: 22671
- rebuild for new vdr


* Sun Jan 21 2007 Anssi Hannula <anssi@mandriva.org> 1.1.1-1mdv2007.0
+ Revision: 111461
- 1.1.1

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 1.1.0-2mdv2007.1
+ Revision: 90922
- rebuild for new vdr

* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 1.1.0-1mdv2007.1
+ Revision: 76321
- 1.1.0

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-7mdv2007.1
+ Revision: 74010
- rebuild for new vdr
- Import vdr-plugin-femon

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-2mdv2007.0
- rebuild for new vdr

* Mon Jun 12 2006 Anssi Hannula <anssi@mandriva.org> 1.0.1-1mdv2007.0
- 1.0.1

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-2mdv2007.0
- rebuild for new vdr

* Thu Jun 01 2006 Anssi Hannula <anssi@mandriva.org> 1.0.0-1mdv2007.0
- initial Mandriva release


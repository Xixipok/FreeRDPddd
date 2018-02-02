#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : FreeRDP
Version  : 11103818168438249615884
Release  : 8
URL      : https://github.com/FreeRDP/FreeRDP/archive/bbd11eef1d03f81f8f168c43afda824961f5884a.tar.gz
Source0  : https://github.com/FreeRDP/FreeRDP/archive/bbd11eef1d03f81f8f168c43afda824961f5884a.tar.gz
Summary  : Free implementation of the Remote Desktop Protocol (RDP)
Group    : Development/Tools
License  : Apache-2.0
Requires: FreeRDP-bin
Requires: FreeRDP-lib
Requires: FreeRDP-doc
BuildRequires : alsa-lib-dev
BuildRequires : cmake
BuildRequires : glib-dev
BuildRequires : gst-plugins-base
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : libSM-dev
BuildRequires : libXinerama-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libxkbfile-dev
BuildRequires : libxshmfence
BuildRequires : libxslt-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : systemd-dev
Patch1: no-rc4.patch

%description
FreeRDP is a open and free implementation of the Remote Desktop Protocol (RDP).
This package provides nightly master builds of all components.

%package bin
Summary: bin components for the FreeRDP package.
Group: Binaries

%description bin
bin components for the FreeRDP package.


%package dev
Summary: dev components for the FreeRDP package.
Group: Development
Requires: FreeRDP-lib
Requires: FreeRDP-bin
Provides: FreeRDP-devel

%description dev
dev components for the FreeRDP package.


%package doc
Summary: doc components for the FreeRDP package.
Group: Documentation

%description doc
doc components for the FreeRDP package.


%package lib
Summary: lib components for the FreeRDP package.
Group: Libraries

%description lib
lib components for the FreeRDP package.


%prep
%setup -q -n FreeRDP-bbd11eef1d03f81f8f168c43afda824961f5884a
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506108978
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DWITH_FFMPEG=OFF
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1506108978
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientConfig.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientTargets.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPConfig.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPConfigVersion.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPTargets.cmake
/usr/lib64/cmake/WinPR2/WinPRConfig.cmake
/usr/lib64/cmake/WinPR2/WinPRConfigVersion.cmake
/usr/lib64/cmake/WinPR2/WinPRTargets-relwithdebinfo.cmake
/usr/lib64/cmake/WinPR2/WinPRTargets.cmake
/usr/lib64/cmake/uwac0/uwac-relwithdebinfo.cmake
/usr/lib64/cmake/uwac0/uwac.cmake
/usr/lib64/cmake/uwac0/uwacConfig.cmake
/usr/lib64/cmake/uwac0/uwacConfigVersion.cmake

%files bin
%defattr(-,root,root,-)
/usr/bin/winpr-hash
/usr/bin/winpr-makecert
/usr/bin/wlfreerdp
/usr/bin/xfreerdp

%files dev
%defattr(-,root,root,-)
/usr/include/freerdp2/freerdp/addin.h
/usr/include/freerdp2/freerdp/altsec.h
/usr/include/freerdp2/freerdp/api.h
/usr/include/freerdp2/freerdp/assistance.h
/usr/include/freerdp2/freerdp/autodetect.h
/usr/include/freerdp2/freerdp/build-config.h
/usr/include/freerdp2/freerdp/cache/bitmap.h
/usr/include/freerdp2/freerdp/cache/brush.h
/usr/include/freerdp2/freerdp/cache/cache.h
/usr/include/freerdp2/freerdp/cache/glyph.h
/usr/include/freerdp2/freerdp/cache/nine_grid.h
/usr/include/freerdp2/freerdp/cache/offscreen.h
/usr/include/freerdp2/freerdp/cache/palette.h
/usr/include/freerdp2/freerdp/cache/pointer.h
/usr/include/freerdp2/freerdp/channels/audin.h
/usr/include/freerdp2/freerdp/channels/channels.h
/usr/include/freerdp2/freerdp/channels/cliprdr.h
/usr/include/freerdp2/freerdp/channels/encomsp.h
/usr/include/freerdp2/freerdp/channels/log.h
/usr/include/freerdp2/freerdp/channels/rail.h
/usr/include/freerdp2/freerdp/channels/rdpdr.h
/usr/include/freerdp2/freerdp/channels/rdpei.h
/usr/include/freerdp2/freerdp/channels/rdpgfx.h
/usr/include/freerdp2/freerdp/channels/rdpsnd.h
/usr/include/freerdp2/freerdp/channels/remdesk.h
/usr/include/freerdp2/freerdp/channels/tsmf.h
/usr/include/freerdp2/freerdp/channels/wtsvc.h
/usr/include/freerdp2/freerdp/client.h
/usr/include/freerdp2/freerdp/client/audin.h
/usr/include/freerdp2/freerdp/client/channels.h
/usr/include/freerdp2/freerdp/client/cliprdr.h
/usr/include/freerdp2/freerdp/client/cmdline.h
/usr/include/freerdp2/freerdp/client/disp.h
/usr/include/freerdp2/freerdp/client/drdynvc.h
/usr/include/freerdp2/freerdp/client/encomsp.h
/usr/include/freerdp2/freerdp/client/file.h
/usr/include/freerdp2/freerdp/client/rail.h
/usr/include/freerdp2/freerdp/client/rdpei.h
/usr/include/freerdp2/freerdp/client/rdpgfx.h
/usr/include/freerdp2/freerdp/client/rdpsnd.h
/usr/include/freerdp2/freerdp/client/remdesk.h
/usr/include/freerdp2/freerdp/client/tsmf.h
/usr/include/freerdp2/freerdp/codec/audio.h
/usr/include/freerdp2/freerdp/codec/bitmap.h
/usr/include/freerdp2/freerdp/codec/bulk.h
/usr/include/freerdp2/freerdp/codec/clear.h
/usr/include/freerdp2/freerdp/codec/color.h
/usr/include/freerdp2/freerdp/codec/dsp.h
/usr/include/freerdp2/freerdp/codec/h264.h
/usr/include/freerdp2/freerdp/codec/interleaved.h
/usr/include/freerdp2/freerdp/codec/jpeg.h
/usr/include/freerdp2/freerdp/codec/mppc.h
/usr/include/freerdp2/freerdp/codec/ncrush.h
/usr/include/freerdp2/freerdp/codec/nsc.h
/usr/include/freerdp2/freerdp/codec/planar.h
/usr/include/freerdp2/freerdp/codec/progressive.h
/usr/include/freerdp2/freerdp/codec/region.h
/usr/include/freerdp2/freerdp/codec/rfx.h
/usr/include/freerdp2/freerdp/codec/xcrush.h
/usr/include/freerdp2/freerdp/codec/zgfx.h
/usr/include/freerdp2/freerdp/codecs.h
/usr/include/freerdp2/freerdp/constants.h
/usr/include/freerdp2/freerdp/crypto/ber.h
/usr/include/freerdp2/freerdp/crypto/certificate.h
/usr/include/freerdp2/freerdp/crypto/crypto.h
/usr/include/freerdp2/freerdp/crypto/der.h
/usr/include/freerdp2/freerdp/crypto/er.h
/usr/include/freerdp2/freerdp/crypto/per.h
/usr/include/freerdp2/freerdp/crypto/tls.h
/usr/include/freerdp2/freerdp/dvc.h
/usr/include/freerdp2/freerdp/error.h
/usr/include/freerdp2/freerdp/event.h
/usr/include/freerdp2/freerdp/extension.h
/usr/include/freerdp2/freerdp/freerdp.h
/usr/include/freerdp2/freerdp/gdi/bitmap.h
/usr/include/freerdp2/freerdp/gdi/dc.h
/usr/include/freerdp2/freerdp/gdi/gdi.h
/usr/include/freerdp2/freerdp/gdi/gfx.h
/usr/include/freerdp2/freerdp/gdi/pen.h
/usr/include/freerdp2/freerdp/gdi/region.h
/usr/include/freerdp2/freerdp/gdi/shape.h
/usr/include/freerdp2/freerdp/graphics.h
/usr/include/freerdp2/freerdp/input.h
/usr/include/freerdp2/freerdp/listener.h
/usr/include/freerdp2/freerdp/locale/keyboard.h
/usr/include/freerdp2/freerdp/locale/locale.h
/usr/include/freerdp2/freerdp/log.h
/usr/include/freerdp2/freerdp/message.h
/usr/include/freerdp2/freerdp/metrics.h
/usr/include/freerdp2/freerdp/peer.h
/usr/include/freerdp2/freerdp/pointer.h
/usr/include/freerdp2/freerdp/primary.h
/usr/include/freerdp2/freerdp/primitives.h
/usr/include/freerdp2/freerdp/rail.h
/usr/include/freerdp2/freerdp/scancode.h
/usr/include/freerdp2/freerdp/secondary.h
/usr/include/freerdp2/freerdp/server/audin.h
/usr/include/freerdp2/freerdp/server/channels.h
/usr/include/freerdp2/freerdp/server/cliprdr.h
/usr/include/freerdp2/freerdp/server/drdynvc.h
/usr/include/freerdp2/freerdp/server/echo.h
/usr/include/freerdp2/freerdp/server/encomsp.h
/usr/include/freerdp2/freerdp/server/rdpdr.h
/usr/include/freerdp2/freerdp/server/rdpei.h
/usr/include/freerdp2/freerdp/server/rdpgfx.h
/usr/include/freerdp2/freerdp/server/rdpsnd.h
/usr/include/freerdp2/freerdp/server/remdesk.h
/usr/include/freerdp2/freerdp/server/shadow.h
/usr/include/freerdp2/freerdp/session.h
/usr/include/freerdp2/freerdp/settings.h
/usr/include/freerdp2/freerdp/svc.h
/usr/include/freerdp2/freerdp/types.h
/usr/include/freerdp2/freerdp/update.h
/usr/include/freerdp2/freerdp/utils/msusb.h
/usr/include/freerdp2/freerdp/utils/passphrase.h
/usr/include/freerdp2/freerdp/utils/pcap.h
/usr/include/freerdp2/freerdp/utils/profiler.h
/usr/include/freerdp2/freerdp/utils/ringbuffer.h
/usr/include/freerdp2/freerdp/utils/signal.h
/usr/include/freerdp2/freerdp/utils/stopwatch.h
/usr/include/freerdp2/freerdp/version.h
/usr/include/freerdp2/freerdp/window.h
/usr/include/uwac0/uwac/uwac-tools.h
/usr/include/uwac0/uwac/uwac.h
/usr/include/winpr2/winpr/asn1.h
/usr/include/winpr2/winpr/bcrypt.h
/usr/include/winpr2/winpr/bitstream.h
/usr/include/winpr2/winpr/clipboard.h
/usr/include/winpr2/winpr/cmdline.h
/usr/include/winpr2/winpr/collections.h
/usr/include/winpr2/winpr/comm.h
/usr/include/winpr2/winpr/credentials.h
/usr/include/winpr2/winpr/credui.h
/usr/include/winpr2/winpr/crt.h
/usr/include/winpr2/winpr/crypto.h
/usr/include/winpr2/winpr/debug.h
/usr/include/winpr2/winpr/dsparse.h
/usr/include/winpr2/winpr/endian.h
/usr/include/winpr2/winpr/environment.h
/usr/include/winpr2/winpr/error.h
/usr/include/winpr2/winpr/file.h
/usr/include/winpr2/winpr/handle.h
/usr/include/winpr2/winpr/heap.h
/usr/include/winpr2/winpr/image.h
/usr/include/winpr2/winpr/ini.h
/usr/include/winpr2/winpr/input.h
/usr/include/winpr2/winpr/interlocked.h
/usr/include/winpr2/winpr/intrin.h
/usr/include/winpr2/winpr/io.h
/usr/include/winpr2/winpr/library.h
/usr/include/winpr2/winpr/locale.h
/usr/include/winpr2/winpr/memory.h
/usr/include/winpr2/winpr/midl.h
/usr/include/winpr2/winpr/ndr.h
/usr/include/winpr2/winpr/nt.h
/usr/include/winpr2/winpr/ntlm.h
/usr/include/winpr2/winpr/pack.h
/usr/include/winpr2/winpr/path.h
/usr/include/winpr2/winpr/pipe.h
/usr/include/winpr2/winpr/platform.h
/usr/include/winpr2/winpr/pool.h
/usr/include/winpr2/winpr/print.h
/usr/include/winpr2/winpr/registry.h
/usr/include/winpr2/winpr/rpc.h
/usr/include/winpr2/winpr/sam.h
/usr/include/winpr2/winpr/schannel.h
/usr/include/winpr2/winpr/security.h
/usr/include/winpr2/winpr/shell.h
/usr/include/winpr2/winpr/smartcard.h
/usr/include/winpr2/winpr/spec.h
/usr/include/winpr2/winpr/ssl.h
/usr/include/winpr2/winpr/sspi.h
/usr/include/winpr2/winpr/sspicli.h
/usr/include/winpr2/winpr/stream.h
/usr/include/winpr2/winpr/string.h
/usr/include/winpr2/winpr/synch.h
/usr/include/winpr2/winpr/sysinfo.h
/usr/include/winpr2/winpr/tchar.h
/usr/include/winpr2/winpr/thread.h
/usr/include/winpr2/winpr/timezone.h
/usr/include/winpr2/winpr/tools/makecert.h
/usr/include/winpr2/winpr/user.h
/usr/include/winpr2/winpr/version.h
/usr/include/winpr2/winpr/windows.h
/usr/include/winpr2/winpr/winhttp.h
/usr/include/winpr2/winpr/winpr.h
/usr/include/winpr2/winpr/winsock.h
/usr/include/winpr2/winpr/wlog.h
/usr/include/winpr2/winpr/wnd.h
/usr/include/winpr2/winpr/wtsapi.h
/usr/include/winpr2/winpr/wtypes.h
/usr/lib64/libfreerdp-client2.so
/usr/lib64/libfreerdp2.so
/usr/lib64/libuwac0.so
/usr/lib64/libwinpr-tools2.so
/usr/lib64/libwinpr2.so
/usr/lib64/pkgconfig/freerdp-client2.pc
/usr/lib64/pkgconfig/freerdp2.pc
/usr/lib64/pkgconfig/uwac0.pc
/usr/lib64/pkgconfig/winpr-tools2.pc
/usr/lib64/pkgconfig/winpr2.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man7/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreerdp-client2.so.2
/usr/lib64/libfreerdp-client2.so.2.0.0
/usr/lib64/libfreerdp2.so.2
/usr/lib64/libfreerdp2.so.2.0.0
/usr/lib64/libuwac0.so.0
/usr/lib64/libuwac0.so.0.0.1
/usr/lib64/libwinpr-tools2.so.2
/usr/lib64/libwinpr-tools2.so.2.0.0
/usr/lib64/libwinpr2.so.2
/usr/lib64/libwinpr2.so.2.0.0
Summary:	Atrac3+ decoder used to decode audio by PPSSPP (Sony PSP emulator)
Name:		ppsspp-at3plus-plugin
Version:	0.1.2
Release:	1
License:	LGPLv2.1+
Group:		Sound
Url:		https://sourceforge.net/projects/maiat3plusdec/
Source0:	http://sourceforge.net/projects/maiat3plusdec/files/MaiAT3PlusDecoder/MaiAT3PlusDecoder_%{version}.zip
# cmake project and some other additional files taken from
# https://github.com/emulibraries/maiatrac3plus
Patch0:		at3plus-1.2-cmake.patch
BuildRequires:	cmake
Suggests:	ppsspp

%description
Mai Atrac3+ decoder used to decode audio by PPSSPP (Sony PSP emulator).
PPSSPP loads it as plugin. Atrac3+ is a Sony Audio format, similar to MP3
but different enough that until recently, nobody really knew how to decode
it. Many PSP games use this format for music playback.

This package is in Restricted repository because the code was possibly
created with reverse engineering.

%prep
%setup -q -n MaiAT3PlusDecoder
%patch0 -p1

%build
%cmake
%make

%install
mkdir -p %{buildroot}%{_libdir}/ppsspp
install -m 0755 build/lib/libat3plusdecoder.so %{buildroot}%{_libdir}/ppsspp/libat3plusdecoder.so

%files
%{_libdir}/ppsspp/libat3plusdecoder.so
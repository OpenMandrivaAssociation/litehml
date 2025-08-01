%define		libname		%mklibname %{name}
%define		develname	%mklibname %{name} -d
%global		__requires_exclude_from ^%{_libdir}/cmake/litehtml/.*$

Name:		litehtml
Version:	0.9
Release:	1
Source0:	https://github.com/litehtml/litehtml/archive/v%{version}/%{name}-%{version}.tar.gz
Summary:	litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support
URL:		https://github.com/litehtml/litehtml
License:	BSD-3-Clause
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	pkgconfig(gumbo)
BuildSystem:	cmake
BuildOption:	-DBUILD_GMOCK=OFF
BuildOption:	-DEXTERNAL_GUMBO=ON
BuildOption:	-DFETCH_CONTENT_FULLY_DISCONNECTED=ON
BuildOption:	-DFETCH_CONTENT_QUIET=OFF
BuildOption:	-DINSTALL_GTEST=OFF
BuildOption:	-DLITEHTML_BUILD_TESTING=OFF

%description
litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support

%package -n %{libname}
Summary: litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support
Group:		System/Libraries

%description -n %{libname}
litehtml is the lightweight HTML rendering engine with CSS2/CSS3 support. Note
that litehtml itself does not draw any text, pictures or other graphics and
that litehtml does not depend on any image/draw/font library. You are free to
use any library to draw images, fonts and any other graphics. litehtml just
parses HTML/CSS and places the HTML elements into the correct positions
(renders HTML). To draw the HTML elements you have to implement the simple
callback interface document_container. This interface is really simple, check
it out! The document_container implementation is required to render HTML
correctly.

litehtml can be used when you need to show HTML formatted text or even to
create a mini-browser, but using it as a full-featured HTML engine is not
recommended. Usually you don't need something like WebKit to show simple HTML
tooltips or HTML-formatted text, litehtml is much better for these as it's more
lightweight and easier to integrate into your application.

litehtml uses the gumbo-parser to parse HTML. Gumbo is an implementation of the
HTML5 parsing algorithm implemented as a pure C99 library with no outside
dependencies. It's designed to serve as a building block for other tools and
libraries such as linters, validators, templating languages, and refactoring
and analysis tools.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(gumbo)

%description -n %{develname}
Development files and headers for %{name}.

%prep
%autosetup -p1

%files -n %{libname}
%{_libdir}/lib%{name}.so*
%license LICENSE
%doc	 README.md

%files -n %{develname}
%{_includedir}/%{name}/*.h
%{_libdir}/cmake/%{name}/%{name}*.cmake

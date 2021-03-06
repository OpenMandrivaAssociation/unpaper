Summary:	Post-processing scanned and photocopied book pages
Name:		unpaper
Version:	6.1
Release:	2
License:	GPL
Group:		Graphics
# the newest version is 0.3, the old one was 1.1. Epoch is needed.
Epoch:		1
Source:		http://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
Url:		http://unpaper.berlios.de/
BuildRequires:  xsltproc
BuildRequires:	netpbm
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavutil)

%description
unpaper is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies.  The main purpose is to make scanned book pages
better readable on screen after conversion to PDF. Additionally,
unpaper might be useful to enhance the quality of scanned pages before
performing optical character recognition (OCR).

unpaper tries to clean scanned images by removing dark edges that
appeared through scanning or copying on areas outside the actual page
content (e.g.  dark areas between the left-hand-side and the
right-hand-side of a double- sided book-page scan).  The program also
tries to detect disaligned centering and rotation of pages and will
automatically straighten each page by rotating it to the correct
angle. This is called "deskewing".  Note that the automatic processing
will sometimes fail. It is always a good idea to manually control the
results of unpaper and adjust the parameter settings according to the
requirements of the input. Each processing step can also be disabled
individually for each sheet.

Input and output files can be in either .pbm or .pgm format, as also
used by the Linux scanning tools scanimage and scanadf.  Conversion to
PDF can e.g. be achieved with the Linux tools pgm2tiff, tiffcp and
tiff2pdf.


%prep
%setup -q


%build
%configure2_5x
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc doc/img doc/*.md README.md COPYING
%{_bindir}/*
%{_mandir}/man1/*

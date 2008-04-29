Summary:	Post-processing scanned and photocopied book pages
Name:		unpaper
Version:	0.3
Release:	%mkrel 1
License:	GPL
Group:		Graphics
# the newest version is 0.3, the old one was 1.1. Epoch is needed.
Epoch:		1
Source:		http://download.berlios.de/unpaper/unpaper-%{version}.tar.gz

Url:		http://unpaper.berlios.de/
BuildRoot:	%_tmppath/%name-%version-%release-root

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
gcc ${CFLAGS} -lm -o unpaper src/unpaper.c



%install
install -d %buildroot%{_bindir}
install -m 755 unpaper %buildroot%{_bindir}



%clean
rm -fr %buildroot



%files
%defattr(-,root,root)
%doc doc/img doc/index.html doc/unpaper.html README LICENSE
%_bindir/*

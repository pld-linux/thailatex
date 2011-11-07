# TODO: unpackaged file: /usr/share/emacs/site-lisp/thai-latex-setup.el
Summary:	Enable typesetting Thai with LaTeX standard document classes
Summary(pl.UTF-8):	Umożliwienie składu tajskiego przy użyciu standardowych klas dokumentów LaTeXa
Name:		thailatex
Version:	0.4.6
Release:	1
License:	LPPL v1.3+
Group:		Applications/Publishing
Source0:	http://linux.thai.net/pub/thailinux/software/thailatex/%{name}-%{version}.tar.gz
# Source0-md5:	ec825bc15527ee90d52a0f02868e8e80
URL:		http://linux.thai.net/projects/thailatex
BuildRequires:	texlive-format-pdflatex
BuildRequires:	texlive-latex
Requires(post,postun):	texlive
Requires:	texlive-latex
Requires:	texlive-tex-babel
Suggests:	swath
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
thailatex is a Thai package which enables typesetting Thai with LaTeX
standard document classes. It is meant to become a part of "babel", a
multilingual package for LaTeX which supports a lot of non-American
languages.

%description -l pl.UTF-8
thailatex to pakiet umożliwiający skład tajski przy użyciu
standardowych klas dokumentów LaTeXa. Ma się stać częścią pakietu
"bebel" - pakietu wielojęzycznego dla LaTeXa, obsługującego wiele
języków nieamerykańskich.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/{tfm,type1,vf}/public

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/texhash

%postun
umask 022
%{_bindir}/texhash

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog HISTORY NEWS README TODO
%attr(755,root,root) %{_bindir}/tlatex
%attr(755,root,root) %{_sbindir}/sync-babel
%attr(755,root,root) %{_sbindir}/sync-thailatex
# XXX common dirs - should belong to texlive?
%dir %{_datadir}/texmf/fonts/afm
%dir %{_datadir}/texmf/fonts/afm/public
%dir %{_datadir}/texmf/fonts/tfm
%dir %{_datadir}/texmf/fonts/tfm/public
%dir %{_datadir}/texmf/fonts/type1
%dir %{_datadir}/texmf/fonts/type1/public
%dir %{_datadir}/texmf/fonts/vf
%dir %{_datadir}/texmf/fonts/vf/public
%dir %{_datadir}/texmf/tex/generic/babel
# XXX common dirs end
%{_datadir}/texmf/fonts/afm/public/thai
%{_datadir}/texmf/fonts/enc/dvips/thai
%{_datadir}/texmf/tex/generic/babel/lthenc.def
%{_datadir}/texmf/tex/generic/babel/thai.ldf
%{_datadir}/texmf/tex/generic/babel/thswitch.sty
%{_datadir}/texmf/tex/generic/babel/tis620.def

Name:		texlive-germbib
Version:	15878
Release:	1
Summary:	German variants of standard BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/germbib
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/germbib.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A development of the (old) german.sty, this bundle provides
German packages, BibTeX styles and documentary examples, for
writing documents with bibliographies. The author has since
developed the babelbib bundle, which (he asserts) supersedes
germbib.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/germbib/gerabbrv.bst
%{_texmfdistdir}/bibtex/bst/germbib/geralpha.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerapali.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerplain.bst
%{_texmfdistdir}/bibtex/bst/germbib/gerunsrt.bst
%{_texmfdistdir}/tex/latex/germbib/bibgerm.sty
%{_texmfdistdir}/tex/latex/germbib/mynormal.sty
%doc %{_texmfdistdir}/doc/bibtex/germbib/README.bibgerm
%doc %{_texmfdistdir}/doc/bibtex/germbib/apalike.doc
%doc %{_texmfdistdir}/doc/bibtex/germbib/apalike.germbib_sty
%doc %{_texmfdistdir}/doc/bibtex/germbib/apalike.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/btxdoc.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/btxhak.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/gerbibtx.bib
%doc %{_texmfdistdir}/doc/bibtex/germbib/gerbibtx.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/gerxampl.bib
%doc %{_texmfdistdir}/doc/bibtex/germbib/schaum.bib
%doc %{_texmfdistdir}/doc/bibtex/germbib/testbibgerm.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/testgerb.tex
%doc %{_texmfdistdir}/doc/bibtex/germbib/xampl.bib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}

%global tl_name germbib
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	German variants of standard BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/germbib
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/germbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/germbib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A development of the (old) german.sty, this bundle provides German
packages, BibTeX styles and documentary examples, for writing documents
with bibliographies. The author has since developed the babelbib bundle,
which (he asserts) supersedes germbib.


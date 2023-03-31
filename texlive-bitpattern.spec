Name:		texlive-bitpattern
Version:	39073
Release:	2
Summary:	Typeset bit pattern diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bitpattern
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitpattern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitpattern.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bitpattern.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package to typeset bit pattern diagrams such as those used to
describe hardware, data format or protocols.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bitpattern
%{_texmfdistdir}/tex/latex/bitpattern
%doc %{_texmfdistdir}/doc/latex/bitpattern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

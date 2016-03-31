Summary:	A small utility which generates Go code from any file
Name:		go-bindata
Version:	3.0.7
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/jteeuwen/go-bindata/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a65ad66927be41885614c5ddd1728b34
URL:		http://github.com/jteeuwen/go-bindata
BuildRequires:	golang >= 1.3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# go stuff
%define _enable_debug_packages 0
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%define import_path github.com/tools/godep

%description
This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally
gzip compressed before being converted to a raw byte slice.

%prep
%setup -q

install -d _build/src/github.com/jteeuwen
ln -s $(pwd) _build/src/github.com/jteeuwen/go-bindata

%build
export GOPATH=$(pwd)/_build
cd go-bindata
go build .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p go-bindata/go-bindata $RPM_BUILD_ROOT%{_bindir}/go-bindata

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/go-bindata

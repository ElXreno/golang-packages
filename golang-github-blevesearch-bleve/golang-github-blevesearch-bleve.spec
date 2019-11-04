%global goipath         github.com/blevesearch/bleve
%global commit          05d86ea8f6e30456949f612cf68cf4a27ce8c9c5
%global scm             git

%gometa

%global common_description %{expand:
Modern text indexing in go
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Modern text indexing in go

License:                Apache-2.0
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging

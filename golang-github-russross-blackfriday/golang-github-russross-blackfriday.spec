%global goipath         github.com/russross/blackfriday
%global commit          11635eb403ff09dbc3a6b5a007ab5ab09151c229
%global scm             git

%gometa

%global common_description %{expand:
Blackfriday is a Markdown processor implemented in Go.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Blackfriday is a Markdown processor implemented in Go.

License:                BSD
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

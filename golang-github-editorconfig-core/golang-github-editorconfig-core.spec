%global goipath         github.com/editorconfig/editorconfig-core-go
%global commit          81ebce5c23dfd25c6c67194b37d3dd3f338c98b1
%global scm             git

%gometa

%global common_description %{expand:
A Editorconfig file parser and manipulator for Go
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                A Editorconfig file parser and manipulator for Go

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}

Provides:               golang(gopkg.in/editorconfig/editorconfig-core-go.v1)


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

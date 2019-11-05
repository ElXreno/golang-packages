%global globalversion   1.3.0

%global goipath         github.com/editorconfig/editorconfig-core-go
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
A Editorconfig file parser and manipulator for Go.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                A Editorconfig file parser and manipulator for Go.

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

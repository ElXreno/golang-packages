%global globalversion   1.49.0

%global goipath         github.com/markbates/goth
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Goth provides a simple, clean, and idiomatic way to write authentication packages for Go web applications
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Goth provides a simple, clean, and idiomatic way to write authentication packages for Go web applications

License:                MIT
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

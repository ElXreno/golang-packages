%global globalversion   2.5.0

%global goipath         github.com/go-testfixtures/testfixtures
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Rails-like test fixtures for Go
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Rails-like test fixtures for Go

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}

Provides:               golang(gopkg.in/testfixtures.v2)


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

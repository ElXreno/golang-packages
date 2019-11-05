%global globalversion   24.0.1

%global goipath         github.com/google/go-github/v24
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Go client library for accessing the GitHub API v3.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Go client library for accessing the GitHub API v3.

License:                BSDv3-Clause
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

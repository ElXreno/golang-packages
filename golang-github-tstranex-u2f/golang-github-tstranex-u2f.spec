%global globalversion   1.0.0

%global goipath         github.com/tstranex/u2f
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
Go package implements the parts of the FIDO U2F
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                Go package implements the parts of the FIDO U2F

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

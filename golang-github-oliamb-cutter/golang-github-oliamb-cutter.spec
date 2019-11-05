%global globalversion   0.2.2

%global goipath         github.com/oliamb/cutter
%global tag             v%{globalversion}
%global scm             git

%gometa

%global common_description %{expand:
A Go library to crop images.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                %{globalversion}
Release:                1%{?dist}
Summary:                A Go library to crop images.

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
